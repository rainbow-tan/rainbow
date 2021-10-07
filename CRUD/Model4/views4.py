# -*- encoding=utf-8 -*-
import json
import time

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from CRUD import Pub
from CRUD import database
from CRUD.Pub import CURRENT_PAGE
from CRUD.Pub import PAGESIZE
from CRUD.settings import BASE_DIR
from Model.models import Field1Table
from Model.models import Field24Table
from Model.models import Field2Table
from Model.models import Field3Table
from Model2.models import Field37Table
from Model4 import Business
from Model4 import DB
from Model4.models import DataTable

COLUMN_NAMES = ['auto_id', 'field1', 'field2', 'field3', 'field48', 'field37', 'field50', 'field54',
                'field85', 'field86', 'field87', 'field88', 'field89', 'field90', 'field91',
                'field92', 'field93', 'field94', 'field95', 'field96', 'field97', 'field98',
                'field99', 'field100', 'field101', 'field102', 'field103', 'field104', 'field105',
                'field106', 'field107', 'field108', 'field109', 'field110', ]


def select_html(request):
    data_dict = dict()

    # 查询下拉框
    data_dict['field1'] = Pub.select_column(Field1Table, 'field1')
    data_dict['field2'] = Pub.select_column(Field2Table, 'field1')
    data_dict['field3'] = Pub.select_column(Field3Table, 'field1')
    data_dict['field24'] = Pub.select_column(Field24Table, 'field1')
    data_dict['field37'] = Pub.select_column(Field37Table, 'field1')

    select_field1 = Pub.request_data(request, 'GET', 'select_field1', '')
    select_field2 = Pub.request_data(request, 'GET', 'select_field2', '')
    select_field3 = Pub.request_data(request, 'GET', 'select_field3', '')
    select_field24 = Pub.request_data(request, 'GET', 'select_field24', '')
    select_field37 = Pub.request_data(request, 'GET', 'select_field37', '')
    select_field48 = Pub.request_data(request, 'GET', 'select_field48', '')
    select_field50 = Pub.request_data(request, 'GET', 'select_field50', '')
    select_field54 = Pub.request_data(request, 'GET', 'select_field54', '')

    pagesize = int(Pub.request_data(request, 'GET', 'pagesize', PAGESIZE))
    current_page = int(Pub.request_data(request, 'GET', 'current_page', CURRENT_PAGE))
    data_dict['current_field1'] = select_field1
    data_dict['current_field2'] = select_field2
    data_dict['current_field3'] = select_field3
    data_dict['current_field24'] = select_field24
    data_dict['current_field37'] = select_field37
    data_dict['current_field48'] = select_field48
    data_dict['current_field50'] = select_field50
    data_dict['current_field54'] = select_field54

    filter_data = DB.select_business(DataTable, field1=select_field1, field2=select_field2,
                                     field3=select_field3, field24=select_field24,
                                     field37=select_field37, field48=select_field48,
                                     field50=select_field50, field54=select_field54,
                                     column_names=COLUMN_NAMES)
    sort_filter_data = Business.sort_data(filter_data)
    database.paging(sort_filter_data, pagesize, current_page, data_dict)  # 分页
    database.export(sort_filter_data, data_dict, u'移频轨道电路测试导出模板.xls', '4')  # 导出

    return render(request, 'Model4/select.html', data_dict)


def add(request):
    Pub.insert_db(DataTable,
                  field1=request.POST['add_field1'],
                  field2=request.POST['add_field2'],
                  field3=request.POST['add_field3'],
                  field48=request.POST['add_field48'],
                  field37=request.POST['add_field37'],
                  field50=request.POST['add_field50'],
                  field54=request.POST['add_field54'],
                  field85=request.POST['add_field85'],
                  field86=request.POST['add_field86'],
                  field87=request.POST['add_field87'],
                  field88=request.POST['add_field88'],
                  field89=request.POST['add_field89'],
                  field90=request.POST['add_field90'],
                  field91=request.POST['add_field91'],
                  field92=request.POST['add_field92'],
                  field93=request.POST['add_field93'],
                  field94=request.POST['add_field94'],
                  field95=request.POST['add_field95'],
                  field96=request.POST['add_field96'],
                  field97=request.POST['add_field97'],
                  field98=request.POST['add_field98'],
                  field99=request.POST['add_field99'],
                  field100=request.POST['add_field100'],
                  field101=request.POST['add_field101'],
                  field102=request.POST['add_field102'],
                  field103=request.POST['add_field103'],
                  field104=request.POST['add_field104'],
                  field105=request.POST['add_field105'],
                  field106=request.POST['add_field106'],
                  field107=request.POST['add_field107'],
                  field108=request.POST['add_field108'],
                  field109=request.POST['add_field109'],
                  field110=request.POST['add_field110'],
                  )
    return redirect("/Model4/select.html/")


def select_for_update(request):  # 为了修改查询数据
    data_dict = dict()
    one_data = Pub.select_db_one(DataTable, request.GET['update_id'], COLUMN_NAMES)
    for index, column_name in enumerate(COLUMN_NAMES):
        data_dict['src_update_{}'.format(column_name)] = one_data[index]
    return HttpResponse(json.dumps(data_dict), content_type="application/json")


def update(request):
    Pub.update_db(DataTable, request.POST['update_id'],
                  field1=request.POST['update_field1'],
                  field2=request.POST['update_field2'],
                  field3=request.POST['update_field3'],
                  field48=request.POST['update_field48'],
                  field37=request.POST['update_field37'],
                  field50=request.POST['update_field50'],
                  field54=request.POST['update_field54'],
                  field85=request.POST['update_field85'],
                  field86=request.POST['update_field86'],
                  field87=request.POST['update_field87'],
                  field88=request.POST['update_field88'],
                  field89=request.POST['update_field89'],
                  field90=request.POST['update_field90'],
                  field91=request.POST['update_field91'],
                  field92=request.POST['update_field92'],
                  field93=request.POST['update_field93'],
                  field94=request.POST['update_field94'],
                  field95=request.POST['update_field95'],
                  field96=request.POST['update_field96'],
                  field97=request.POST['update_field97'],
                  field98=request.POST['update_field98'],
                  field99=request.POST['update_field99'],
                  field100=request.POST['update_field100'],
                  field101=request.POST['update_field101'],
                  field102=request.POST['update_field102'],
                  field103=request.POST['update_field103'],
                  field104=request.POST['update_field104'],
                  field105=request.POST['update_field105'],
                  field106=request.POST['update_field106'],
                  field107=request.POST['update_field107'],
                  field108=request.POST['update_field108'],
                  field109=request.POST['update_field109'],
                  field110=request.POST['update_field110'],
                  )
    return redirect("/Model4/select.html/")


def delete(request):
    delete_ids = request.GET['delete_ids']
    ids = delete_ids.split('_')
    ids.pop(len(ids) - 1)  # 去除最后的空串
    for delete_id in ids:
        Pub.delete_db(DataTable, delete_id)
    return redirect("/Model4/select.html/")


def import_html(request):
    return render(request, 'Model4/import.html')


def import_data(request):  # 导入
    data_dict = dict()
    calculate_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = BASE_DIR + '/templates/files/import/data_four_{}.xls'.format(
                time.strftime("%Y%m%d%H%M%S", time.localtime()))
        Pub.save_file(filename, file)
        try:
            file_data = Pub.read_xls(filename, 3)
            sorted_data = Business.sort_data(file_data)
            calculate_data = sorted_data
            ret, msg = Business.can_import(calculate_data)
            if ret is True:
                pop_data = Pub.pop_first(calculate_data)
                for one_data in pop_data:
                    Pub.insert_db(DataTable,
                                  field1=one_data[0],
                                  field2=one_data[1],
                                  field3=one_data[2],
                                  field48=one_data[3],
                                  field37=one_data[4],
                                  field50=one_data[5],
                                  field54=one_data[6],
                                  field85=one_data[7],
                                  field86=one_data[8],
                                  field87=one_data[9],
                                  field88=one_data[10],
                                  field89=one_data[11],
                                  field90=one_data[12],
                                  field91=one_data[13],
                                  field92=one_data[14],
                                  field93=one_data[15],
                                  field94=one_data[16],
                                  field95=one_data[17],
                                  field96=one_data[18],
                                  field97=one_data[19],
                                  field98=one_data[20],
                                  field99=one_data[21],
                                  field100=one_data[22],
                                  field101=one_data[23],
                                  field102=one_data[24],
                                  field103=one_data[25],
                                  field104=one_data[26],
                                  field105=one_data[27],
                                  field106=one_data[28],
                                  field107=one_data[29],
                                  field108=one_data[30],
                                  field109=one_data[31],
                                  field110=one_data[32],
                                  )
                data_dict['success'] = '导入成功'
            else:
                data_dict['success'] = '导入失败->{}'.format(msg)
        except Exception as e:
            data_dict['success'] = '导入失败->{}'.format(e)
            print('导入文件失败:{}'.format(e))
    data_dict['data'] = calculate_data
    return render(request, 'Model4/import.html', data_dict)


def check_data(request):
    data_dict = dict()
    sorted_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = BASE_DIR + '/templates/files/import/data_four_{}.xls'.format(
                time.strftime("%Y%m%d%H%M%S", time.localtime()))
        Pub.save_file(filename, file)
        try:
            file_data = Pub.read_xls(filename, 3)
            sorted_data = Business.sort_data(file_data)
            # calculate_data = Business.all_row(sorted_data)
            data_dict['success'] = '查看成功'
        except Exception as e:
            data_dict['success'] = '查看失败'
            print('查看文件数据失败:{}'.format(e))
    data_dict['data'] = sorted_data
    return render(request, 'Model4/import.html', data_dict)
