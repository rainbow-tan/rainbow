# -*- coding: utf-8 -*-
import os
from datetime import datetime

from xlrd import xldate_as_tuple

from CRUD.settings import BASE_DIR
import xlrd
from xlutils.copy import copy


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


def write_xls(filename, data_list):
    """
    保存数据到xls或xlsx文件
    :param filename: 保存的路径
    :param data_list: [['47','a','b'],['48','a','b'],['49','a','b']]
    :return: 
    """
    excel_template = BASE_DIR + '/templates/excel/template.xlsx'
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
        print('未找到文件:{}'.format(excel_template))


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



