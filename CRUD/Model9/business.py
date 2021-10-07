# -*- encoding=utf-8 -*-
import datetime
import os

import xlrd
from xlrd import xldate_as_tuple


def deal_xls_data(data):
    can_import = True
    message = ''
    return can_import, message


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
                        data = datetime.datetime(*xldate_as_tuple(val, 0)).strftime('%Y-%m-%d')
                    else:
                        data = sheet1.cell(row, line).value
                    row_data.append(data)
                all_data.append(row_data)
    else:
        print('未找到文件:{}'.format(filename))
    return all_data


def debug():
    pass


if __name__ == '__main__':
    pass
    debug()
