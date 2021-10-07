# -*- encoding=utf-8 -*-
import os

import xlwt


def create_folder(folder):
    folder = os.path.abspath(folder)
    if not os.path.isdir(folder):
        try:
            os.makedirs(folder)
        except Exception as e:
            print('创建文件夹失败:{}'.format(e))


def set_style():
    align = xlwt.Alignment()
    align.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
    align.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中

    font = xlwt.Font()  # 字体基本设置
    font.name = u'新宋体'
    font.colour_index = 32764  # 字体颜色
    font.height = 160  # 字体大小

    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN  # 添加边框
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN

    style = xlwt.XFStyle()
    style.font = font
    style.alignment = align
    style.borders = borders
    return style


def merge_write(filename, title, data_dict):
    filename = os.path.abspath(filename)
    path = os.path.dirname(filename)
    create_folder(path)
    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet')
    style = set_style()
    sheet.write_merge(0, 0, 0, 10, title, style)
    name = ['序号', '项目', '工作内容分类', '工作月份', '工作周期', '工作要求说明', '单位', '', '数量']
    index = 0
    for info in name:
        sheet.write_merge(1, 2, index, index, info, style)
        index += 1

    head = data_dict.get('head', [])
    chejian_start_col = index
    chezhan_col = index
    chezhan_index = index
    for one in head:
        # 写车间
        chezhan_col = chejian_start_col
        chejian_end_col = chejian_start_col + len(one['chezhan']) - 1
        sheet.write_merge(1, 1, chejian_start_col, chejian_end_col, one['chejian'], style)
        chejian_start_col = chejian_end_col + 1
        # 写车站
        for chezhan_index, chezhan in enumerate(one['chezhan']):
            sheet.write(2, chezhan_col + chezhan_index, chezhan, style)
    for i in range(chezhan_col + chezhan_index):
        sheet.col(i).width = 256 * 20
    xiangmus = []
    body = data_dict.get('body', {})
    for one in body:
        one_xiangmu = one['xiangmu']
        if one_xiangmu not in xiangmus:
            xiangmus.append(one_xiangmu)
    xiangmu_tongji = {}
    for one in body:
        if one['xiangmu'] not in xiangmu_tongji:
            xiangmu_tongji[one['xiangmu']] = 1
        else:
            xiangmu_tongji[one['xiangmu']] = xiangmu_tongji[one['xiangmu']] + 1
    xiangmu_start = 3
    for i in xiangmus:
        xiangmu_end = xiangmu_tongji[i] * 3 + xiangmu_start - 1
        sheet.write_merge(xiangmu_start, xiangmu_end, 1, 1, i, style)
        xiangmu_start = xiangmu_end + 1
        pass
    xuhao_start = 3
    heji_start = 3
    tongji_start = 3
    jihua_benyuewancheng_leijiwancheng = ['计划数',
                                          '本月完成',
                                          '累计完成'
                                          ]
    for one in body:
        xuhao_end = xuhao_start + 2
        sheet.write_merge(xuhao_start, xuhao_end, 0, 0, one['auto_id'], style)
        sheet.write_merge(xuhao_start, xuhao_end, 2, 2, one['fenlei'], style)
        sheet.write_merge(xuhao_start, xuhao_end, 3, 3, one['yuefen'], style)
        sheet.write_merge(xuhao_start, xuhao_end, 4, 4, one['zhouqi'], style)
        sheet.write_merge(xuhao_start, xuhao_end, 5, 5, one['neirongshuoming'], style)
        sheet.write_merge(xuhao_start, xuhao_end, 6, 6, one['danwei'], style)
        xuhao_start = xuhao_end + 1
        for i in range(3):
            sheet.write(heji_start, 7, jihua_benyuewancheng_leijiwancheng[i], style)
            heji_start += 1
        for j in range(len(one['renwuliang'])):
            sheet.write(tongji_start, j + 8, one['renwuliang'][j], style)
        for j in range(len(one['benyuewancheng'])):
            sheet.write(tongji_start + 1, j + 8, one['benyuewancheng'][j], style)
        for j in range(len(one['leijiwancheng'])):
            sheet.write(tongji_start + 2, j + 8, one['leijiwancheng'][j], style)
        tongji_start += 3
    book.save(filename)
