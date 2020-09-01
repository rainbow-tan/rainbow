# -*- coding: utf-8 -*-
import os
from datetime import datetime

import xlrd
from xlrd import xldate_as_tuple
from xlutils.copy import copy

from CRUD.settings import BASE_DIR


def save_file(filename, file_handler):
    """
    保存前端传来的文件
    :param filename: 保存的路径
    :param file_handler: 前端handler
    :return: 
    """
    path = os.path.dirname(filename)
    if path != '' and not os.path.exists(path):
        os.makedirs(path)
    with open(filename, 'wb+') as f:
        for chunk in file_handler.chunks():
            f.write(chunk)


def append_xls(filename, data_list):
    """
    保存数据到xls或xlsx文件
    :param filename: 保存的路径
    :param data_list: [['47','a','b'],['48','a','b'],['49','a','b']]
    :return: 
    """
    excel_template = BASE_DIR + '/templates/files/excel/导出模板.xlsx'
    if os.path.isfile(excel_template):
        path = os.path.dirname(filename)
        if path != '' and not os.path.exists(path):
            os.makedirs(path)
        f = xlrd.open_workbook(excel_template)  # 打开Excel为xlrd对象
        old_sheet = f.sheet_by_index(0)  # 取到第一个旧表
        old_sheet_rows = old_sheet.nrows  # 第一个旧表的行数，下面追加就得在这个后面写入数据
        copy_read = copy(f)  # 把xlrd对象转为xlwt对象
        exist_sheet = copy_read.get_sheet(0)  # 取旧表
        for one_data in data_list:
            for index, data in enumerate(one_data):
                exist_sheet.write(old_sheet_rows, index, str(data))
            old_sheet_rows += 1
        copy_read.save(filename)
    else:
        print('未找到导出模板文件:{}'.format(excel_template))


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


def read_xls(filename):
    """
    读取xls或xlsx文件
    :param filename: 文件路径
    :return: 去除表头的list [['47','a','b'],['48','a','b'],['49','a','b']]
    """
    all_data = []
    if os.path.isfile(filename):
        f = xlrd.open_workbook(filename)  # 打开Excel
        all_sheets = f.sheets()  # 找到所有的表
        if len(all_sheets) >= 1:
            sheet1 = all_sheets[0]
            rows = sheet1.nrows
            lines = sheet1.ncols
            for row in range(rows):
                row_data = []
                for line in range(lines):
                    data_type = sheet1.cell(row, line).ctype
                    if data_type == 3:
                        val = sheet1.cell(row, line).value
                        data = datetime(*xldate_as_tuple(val, 0)).strftime('%Y-%m-%d')
                    else:
                        data = sheet1.cell(row, line).value
                    row_data.append(data)
                all_data.append(row_data)  # 一行一行遍历
    else:
        print('未找到文件:{}'.format(filename))
    if len(all_data) > 0:  # 去除表头
        all_data.pop(0)
    return all_data


def get_folder_files(folder):
    all_files = []
    if os.path.exists(folder):
        for root, dirs, files in os.walk(folder):
            for one_file in files:
                all_files.append(os.path.join(root, one_file))
    else:
        print('未找到文件夹:{}'.format(folder))
    return all_files


def delete_folder(folder, max_size):
    # 判断大小删除文件夹文件
    all_files = get_folder_files(folder)
    size = 0
    for file in all_files:
        size += os.path.getsize(file)
    if size > max_size:
        for file in all_files:
            os.remove(file)


def remove_index_for_data(data_list, remove_index=[10, 11, 12, 13, 14, 15, ]):
    new_data = []
    for one_data in data_list:
        new_one_data = []
        for index, data in enumerate(one_data):
            if index not in remove_index:
                new_one_data.append(data)
        new_data.append(new_one_data)
    return new_data


def request_data(request, mode, key, default):
    value = default
    if mode == 'POST' and request.POST.get(key) is not None:
        value = request.POST.get(key)
    elif mode == 'GET' and request.GET.get(key) is not None:
        value = request.GET.get(key)
    else:
        pass
    return value


# 排序
def sort_data(data):
    data.sort(key=lambda x: (x[1], x[2], x[3]))
    return data


# 判断*标数据
def can_import(data, index=[1, 2, 3, 4, 6, 7, 23, 24, 25, 26, 27, 28, 29]):
    for one_data in data:
        for need_index in index:
            if one_data[need_index] == '':
                print('下标:{}数据为空'.format(need_index))
                return False
    return True


if __name__ == '__main__':
    pass
