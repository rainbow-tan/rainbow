# -*- encoding=utf-8 -*-
import datetime
import os

import xlrd
from xlrd import xldate_as_tuple


def mistiming_now(time_str):
    """
    计算距离下次检查时间还有多久
    :param time_str:
    :return:
    """
    days = -1
    time1 = datetime.datetime.now()
    try:
        time2 = datetime.datetime.strptime(time_str, '%Y-%m-%d')
        miss = time2 - time1
        days = miss.days
    except Exception as e:
        print('计算距离下次检查时间还有多久失败:{}'.format(e))
    return days


def next_date(riqi, zhouqi):
    """
    计算下次检查日期(单个)
    :param riqi:
    :param zhouqi:
    :return:
    """
    xiaciriqi_str = ''
    try:
        date_riqi = datetime.datetime.strptime(riqi, '%Y-%m-%d')
        date_zhouqi = datetime.timedelta(days=30 * int(zhouqi))
        xiaciriqi = date_riqi + date_zhouqi
        xiaciriqi_str = xiaciriqi.strftime('%Y-%m-%d')
    except Exception as e:
        print('计算下次检查日期失败:{}'.format(e))
    return xiaciriqi_str


def deal_xls_data(data):
    """计算下次检查日期(所有)"""
    can_import = True
    message = ''
    for row_data in data:
        riqi = row_data[13]
        zhouqi = row_data[15]
        xiaciriqi_str = next_date(riqi, zhouqi)
        if xiaciriqi_str:
            row_data[14] = xiaciriqi_str
            days = mistiming_now(xiaciriqi_str)
            if days <= 0:
                row_data[16] = '超期'
            elif 0 < days <= 30:
                row_data[16] = '即将超期'
            else:
                row_data[16] = '正常'
        else:
            row_data[16] = ''
        try:
            row_data[15] = int(float(row_data[15]))
        except Exception as e:
            print('保存周期为整数失败:{}'.format(e))
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
