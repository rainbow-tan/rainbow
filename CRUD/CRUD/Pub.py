import os
import time
from datetime import datetime

import xlrd
import xlwt
from django.db.models import Q
from xlrd import xldate_as_tuple
from xlutils.copy import copy

from CRUD.settings import BASE_DIR

PAGESIZE = 100  # 默认每页显示记录条数
CURRENT_PAGE = 1  # 默认显示第一页
IMPORT_FOLDER = os.path.join(BASE_DIR, 'templates/files/import')  # 导入文件保存位置
EXPORT_FOLDER = os.path.join(BASE_DIR, 'templates/files/export')  # 导出文件保存位置
STATIC_EXPORT_FOLDER = '/static/files/export'  # 前端接受导出文件url
EXPORT_TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates/ExportTemplate')  # 导出模板文件保存位置
SAVE_FOLDER_SIZE = 1024 * 1024 * 3  # 默认保存大小


def get_time():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())


def request_data(request, mode, key, default):
    """
    获取前端传来的数据，没有则返回默认值
    :param request: request
    :param mode: 方式GET或者POST
    :param key: 参数名
    :param default: 默认值
    :return:
    """
    return getattr(request, mode).get(key, default)


def create_folder(folder):
    folder = os.path.abspath(folder)
    if not os.path.exists(folder):
        try:
            os.makedirs(folder)
        except Exception as e:
            print('创建文件夹失败:{}'.format(e))


def save_file(filename, file_handler):
    """
    保存前端传来的文件
    :param filename: 保存的路径
    :param file_handler: 前端handler
    :return:
    """
    filename = os.path.abspath(filename)
    folder = os.path.dirname(filename)
    create_folder(folder)
    with open(filename, 'wb+') as f:
        for chunk in file_handler.chunks():
            f.write(chunk)


# 文件夹
def get_folder_files(folder):
    """
     查找文件夹中所有文件
    :param folder: 文件夹目录
    :return: [[],[],[]]
    """
    all_files = []
    if os.path.exists(folder):
        for root, dirs, files in os.walk(folder):
            for one_file in files:
                all_files.append(os.path.join(root, one_file))
    else:
        print('未找到文件夹:{}'.format(folder))
    return all_files


def delete_folder(folder, max_size):
    # 判断所有文件大小删除文件夹文件
    all_files = get_folder_files(folder)
    size = 0
    for file in all_files:
        size += os.path.getsize(file)
    if size > max_size:
        for file in all_files:
            try:
                os.remove(file)
            except Exception as e:
                print('删除文件失败:{}'.format(e))


# 其他
def change_auto_id(data_list):
    """
    改变下标为1,2,3自动增加
    :param data_list: [['47','a1','b'],['48','ag','b'],['49','a','bn']]
    :return: [['1','a1','b'],['2','ag','b'],['3','a','bn']]
    """
    new_data_list = []
    for index_data_list, one_data in enumerate(data_list):
        new_data = []
        for index, data in enumerate(one_data):
            if index != 0:
                new_data.append(data)
            else:
                new_data.append(str(index_data_list + 1))
        new_data_list.append(new_data)
    return new_data_list


def pop_first(data_list):
    """
    移除第一个元素(顺号)
    :param data_list: [['47','b1',','c'],['12','b2',','c'],['1','b3',','c']]
    :return: [['b1',','c'],['b2',','c'],['b3',','c']]
    """
    new_data_list = []
    for data in data_list:
        one_data = []
        for i, j in enumerate(data):
            if i != 0:
                one_data.append(j)
        new_data_list.append(one_data)
    return new_data_list


# xls
def read_xls(filename, read_begin_row=1):
    all_data = []
    if os.path.isfile(filename):
        f = xlrd.open_workbook(filename)  # 打开Excel
        all_sheets = f.sheets()  # 找到所有的表
        if len(all_sheets) >= 1:
            sheet1 = all_sheets[0]
            rows = sheet1.nrows  # 行
            lines = sheet1.ncols  # 列
            for row in range(read_begin_row, rows):
                row_data = []
                for line in range(lines):
                    data_type = sheet1.cell(row, line).ctype
                    if data_type == 2:  # number
                        data = int(float(sheet1.cell(row, line).value))
                    elif data_type == 3:  # 日期
                        val = sheet1.cell(row, line).value
                        data = datetime(*xldate_as_tuple(val, 0)).strftime('%Y-%m-%d')
                    else:
                        data = sheet1.cell(row, line).value
                    row_data.append(data)
                all_data.append(row_data)
    else:
        print('未找到文件:{}'.format(filename))
    return all_data


def append_xls(source_file, filename, write_data):
    if os.path.isfile(source_file):
        path = os.path.dirname(filename)
        create_folder(path)
        f = xlrd.open_workbook(source_file, formatting_info=True)  # 打开Excel为xlrd对象
        old_sheet = f.sheet_by_index(0)  # 取到第一个旧表
        old_sheet_rows = old_sheet.nrows  # 第一个旧表的行数，下面追加就得在这个后面写入数据
        copy_read = copy(f)  # 把xlrd对象转为xlwt对象
        exist_sheet = copy_read.get_sheet(0)  # 取旧表

        align = xlwt.Alignment()
        align.horz = xlwt.Alignment.HORZ_CENTER
        align.vert = xlwt.Alignment.VERT_CENTER

        font = xlwt.Font()  # 字体基本设置
        font.name = u'新宋体'
        font.color = 'black'
        font.height = 160  # 字体大小

        borders = xlwt.Borders()  # Create borders
        borders.left = xlwt.Borders.THIN  # 添加边框
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN

        style = xlwt.XFStyle()
        style.font = font
        style.alignment = align
        style.borders = borders
        for one_data in write_data:
            for index, data in enumerate(one_data):
                exist_sheet.write(old_sheet_rows, index, data, style)
            old_sheet_rows += 1
        copy_read.save(filename)
    else:
        print('未找到导出模板文件:{}'.format(source_file))


def select_column(table_name, column_name):
    data = table_name.objects.values_list(column_name, flat=True).distinct()
    return data


def select_db_one(table_name, auto_id, column_names):
    """
    根据auto_id查询一条数据
    :param table_name: 表名
    :param auto_id: auto_id
    :param column_names: 列名
    :return:[]
    """
    select_data = table_name.objects.get(auto_id=auto_id)
    data = list()
    for arg in column_names:
        data.append(select_data.__dict__[arg])
    return data


def select_filter_and_or(table_name, connector, select_conditions, column_names, order_by_names=[]):
    """
    与或条件查询
    :param table_name: 表名
    :param connector: AND 或者 OR
    :param select_conditions: 查询的条件 {key:value,key1:value1}
    :param column_names: 列名 []
    :return: [[],[],[]]
    """
    q = Q()
    q.connector = connector
    for select_key, select_value in select_conditions.items():
        if select_value != '':
            q.children.append((select_key, select_value))
    select_data = table_name.objects.filter(q)
    for order_by_name in order_by_names:
        select_data = select_data.order_by(order_by_name)
    all_data = []
    for data in select_data:
        one_data = list()
        for column_name in column_names:
            one_data.append(data.__dict__[column_name])
        all_data.append(one_data)
    return all_data


def insert_db(table_name, **kwargs):
    """
    数据库insert
    :param table_name: 表名
    :param kwargs: 列名以及值 field1='value',filed2='value2'
    :return: None
    """
    table_name(**kwargs).save()


def update_db(table_name, auto_id, **kwargs):
    """
    根据 auto_id 进行修改数据库
    :param table_name: 表名
    :param auto_id: auto_id
    :param kwargs: 列名以及值 field1='value',filed2='value2'
    :return: None
    """
    table_object = table_name.objects.get(auto_id=auto_id)
    for key, value in kwargs.items():
        table_object.__dict__[key] = value
    table_object.save()


def delete_db(table_name, auto_id):
    """
    删除表中某一条数据
    :param table_name: 表名
    :param auto_id: auto_id
    :return: None
    """
    table_name.objects.get(auto_id=auto_id).delete()
