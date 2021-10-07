# -*- encoding=utf-8 -*-
import datetime
import os
from datetime import datetime

import xlrd
from xlrd import xldate_as_tuple


def read_xls(filename, read_begin_row=1):
    """读取xls文件"""
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
                        data = float(sheet1.cell(row, line).value)
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


def deal_xls(file_data):
    """
    保留两位小数和一位小数
    :param file_data:
    :return:
    """
    file_data.sort(key=lambda x: (x[0]), reverse=True)
    for row_data in file_data:
        if row_data[16] != '':
            row_data[16] = '{:0.2f}'.format(float(row_data[16]))
        if row_data[17] != '':
            row_data[17] = '{:0.2f}'.format(float(row_data[17]))
        if row_data[18] != '':
            row_data[18] = '{:0.2f}'.format(float(row_data[18]))
        if row_data[19] != '':
            row_data[19] = '{:0.2f}'.format(float(row_data[19]))
        if row_data[20] != '':
            row_data[20] = '{:0.1f}'.format(float(row_data[20]))
        if row_data[21] != '':
            row_data[21] = '{:0.1f}'.format(float(row_data[21]))
        if row_data[23] != '':  # 使用时间
            row_data[23] = int(float(row_data[23]))
        if row_data[9] != '':  # 载频
            try:
                row_data[9] = int(float(row_data[9]))
            except Exception as e:
                print('处理载频失败:{}'.format(e))
