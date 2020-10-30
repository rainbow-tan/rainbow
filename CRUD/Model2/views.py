# -*- encoding=utf-8 -*-
import json
import os
import time

from django.core.paginator import EmptyPage
from django.core.paginator import InvalidPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from CRUD import Pub
from CRUD.settings import BASE_DIR
from Model.models import Field1Table
from Model.models import Field23Table
from Model.models import Field2Table
from Model.models import Field3Table
from Model2 import Business
from Model2.models import DataTable
from Model2.models import Field36Table
from Model2.models import Field37Table
from Model2.models import Field41Table
from Model2.models import Field42Table

COLUMN_NAMES = ['auto_id', 'field30', 'field1', 'field2', 'field23', 'field31', 'field32',
                'field33', 'field3', 'field34', 'field35', 'field36', 'field37', 'field38',
                'field39', 'field40', 'field41', 'field42', 'field43', 'field44', 'field45']


def select_html(request):
    data_dict = dict()

    # 查询下拉框
    data_dict['field1'] = Pub.select_column(Field1Table, 'field1')
    data_dict['field2'] = Pub.select_column(Field2Table, 'field1')
    data_dict['field23'] = Pub.select_column(Field23Table, 'field1')
    data_dict['field3'] = Pub.select_column(Field3Table, 'field1')
    data_dict['field36'] = Pub.select_column(Field36Table, 'field1')
    data_dict['field37'] = Pub.select_column(Field37Table, 'field1')
    data_dict['field41'] = Pub.select_column(Field41Table, 'field1')
    data_dict['field42'] = Pub.select_column(Field42Table, 'field1')

    select_field1 = Pub.request_data(request, 'GET', 'select_field1', '')
    select_field2 = Pub.request_data(request, 'GET', 'select_field2', '')
    select_field23 = Pub.request_data(request, 'GET', 'select_field23', '')
    select_field3 = Pub.request_data(request, 'GET', 'select_field3', '')
    select_field36 = Pub.request_data(request, 'GET', 'select_field36', '')
    select_field37 = Pub.request_data(request, 'GET', 'select_field37', '')
    select_field41 = Pub.request_data(request, 'GET', 'select_field41', '')
    select_field42 = Pub.request_data(request, 'GET', 'select_field42', '')
    select_field30 = Pub.request_data(request, 'GET', 'select_field30', '')
    select_field45 = Pub.request_data(request, 'GET', 'select_field45', '')

    pagesize = int(Pub.request_data(request, 'GET', 'pagesize', Pub.PAGESIZE))
    current_page = int(Pub.request_data(request, 'GET', 'current_page', Pub.CURRENT_PAGE))

    data_dict['current_field1'] = select_field1
    data_dict['current_field2'] = select_field2
    data_dict['current_field23'] = select_field23
    data_dict['current_field3'] = select_field3
    data_dict['current_field36'] = select_field36
    data_dict['current_field37'] = select_field37
    data_dict['current_field41'] = select_field41
    data_dict['current_field42'] = select_field42
    data_dict['current_field30'] = select_field30
    data_dict['current_field45'] = select_field45
    filter_data = Pub.select_filter_and_or(DataTable, 'AND',
                                           {'field1': select_field1, 'field2': select_field2,
                                            'field23': select_field23, 'field3': select_field3,
                                            'field36': select_field36, 'field37': select_field37,
                                            'field41': select_field41, 'field42': select_field42,
                                            'field30': select_field30, 'field45': select_field45},
                                           column_names=COLUMN_NAMES)
    sort_data = Business.sort_data(filter_data)

    # 分页
    paginator = Paginator(sort_data, pagesize)
    if current_page > paginator.num_pages:
        current_page = paginator.num_pages
    try:
        show_data = paginator.page(current_page)
    except PageNotAnInteger:
        show_data = paginator.page(1)
    except EmptyPage:
        show_data = paginator.page(paginator.num_pages)
    except InvalidPage:
        show_data = paginator.page(1)
    except Exception as e:
        show_data = paginator.page(1)
        print('分页失败:{}'.format(e))

    if current_page - 1 > 0:
        previous_page = current_page - 1
    else:
        previous_page = 1
    if current_page + 1 < paginator.num_pages:
        next_page = current_page + 1
    else:
        next_page = paginator.num_pages
    data_dict['data'] = show_data
    data_dict['count'] = len(filter_data)
    data_dict['pagesize'] = str(pagesize)
    data_dict['previous_page'] = previous_page
    data_dict['current_page'] = str(current_page)
    data_dict['next_page'] = next_page
    data_dict['last_page'] = paginator.num_pages

    folder = '/two/data_{}.xls'.format(Pub.get_time())
    save_path = Pub.EXPORT_FOLDER + folder
    data_dict['file'] = Pub.STATIC_EXPORT_FOLDER + folder
    write_data = Pub.change_auto_id(sort_data)
    source_file = os.path.join(Pub.EXPORT_TEMPLATE_FOLDER, u'自闭档案导出模板.xls')
    Pub.append_xls(source_file, save_path, write_data)

    return render(request, 'two/select.html', data_dict)


def add(request):
    Pub.insert_db(DataTable,
                  field30=request.POST['add_field30'],
                  field1=request.POST['add_field1'],
                  field2=request.POST['add_field2'],
                  field23=request.POST['add_field23'],
                  field31=request.POST['add_field31'],
                  field32=request.POST['add_field32'],
                  field33=request.POST['add_field33'],
                  field3=request.POST['add_field3'],
                  field34=request.POST['add_field34'],
                  field35=request.POST['add_field35'],
                  field36=request.POST['add_field36'],
                  field37=request.POST['add_field37'],
                  field38=request.POST['add_field38'],
                  field39=request.POST['add_field39'],
                  field40=request.POST['add_field40'],
                  field41=request.POST['add_field41'],
                  field42=request.POST['add_field42'],
                  field43=request.POST['add_field43'],
                  field44=request.POST['add_field44'],
                  field45=request.POST['add_field45'])
    return redirect("/two/select.html/")


def select_for_update(request):  # 为了修改查询数据
    data_dict = dict()
    one_data = Pub.select_db_one(DataTable, request.GET['update_id'], COLUMN_NAMES)
    for index, column_name in enumerate(COLUMN_NAMES):
        data_dict['src_update_{}'.format(column_name)] = one_data[index]
    return HttpResponse(json.dumps(data_dict), content_type="application/json")


def update(request):
    Pub.update_db(DataTable, request.POST['update_id'],
                  field30=request.POST['update_field30'],
                  field1=request.POST['update_field1'],
                  field2=request.POST['update_field2'],
                  field23=request.POST['update_field23'],
                  field31=request.POST['update_field31'],
                  field32=request.POST['update_field32'],
                  field33=request.POST['update_field33'],
                  field3=request.POST['update_field3'],
                  field34=request.POST['update_field34'],
                  field35=request.POST['update_field35'],
                  field36=request.POST['update_field36'],
                  field37=request.POST['update_field37'],
                  field38=request.POST['update_field38'],
                  field39=request.POST['update_field39'],
                  field40=request.POST['update_field40'],
                  field41=request.POST['update_field41'],
                  field42=request.POST['update_field42'],
                  field43=request.POST['update_field43'],
                  field44=request.POST['update_field44'],
                  field45=request.POST['update_field45'])
    return redirect("/two/select.html/")


def delete(request):
    delete_ids = request.GET['delete_ids']
    ids = delete_ids.split('_')
    ids.pop(len(ids) - 1)  # 去除最后的空串
    for delete_id in ids:
        Pub.delete_db(DataTable, delete_id)
    return redirect("/two/select.html/")


def import_html(request):
    return render(request, 'two/import.html')


def import_data(request):  # 导入
    data_dict = dict()
    sorted_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = BASE_DIR + '/templates/files/import/data_two_{}.xls'.format(
            time.strftime("%Y%m%d%H%M%S", time.localtime()))
        Pub.save_file(filename, file)
        try:
            file_data = Pub.read_xls(filename, 2)
            sorted_data = Business.sort_data(file_data)
            # to_int_data = Business.float_to_int(sorted_data)
            ret, msg = Business.can_import(sorted_data)
            if ret is True:
                pop_data = Pub.pop_first(sorted_data)
                for one_data in pop_data:
                    Pub.insert_db(DataTable,
                                  field30=one_data[0],
                                  field1=one_data[1],
                                  field2=one_data[2],
                                  field23=one_data[3],
                                  field31=one_data[4],
                                  field32=one_data[5],
                                  field33=one_data[6],
                                  field3=one_data[7],
                                  field34=one_data[8],
                                  field35=one_data[9],
                                  field36=one_data[10],
                                  field37=one_data[11],
                                  field38=one_data[12],
                                  field39=one_data[13],
                                  field40=one_data[14],
                                  field41=one_data[15],
                                  field42=one_data[16],
                                  field43=one_data[17],
                                  field44=one_data[18],
                                  field45=one_data[19])
                data_dict['success'] = '导入成功'
            else:
                data_dict['success'] = '导入失败->{}'.format(msg)
        except Exception as e:
            data_dict['success'] = '导入失败->{}'.format(e)
            print('导入文件失败:{}'.format(e))
    data_dict['data'] = sorted_data
    return render(request, 'two/import.html', data_dict)


def check_data(request):
    data_dict = dict()
    sorted_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = BASE_DIR + '/templates/files/import/data_two_{}.xls'.format(
            time.strftime("%Y%m%d%H%M%S", time.localtime()))
        Pub.save_file(filename, file)
        try:
            file_data = Pub.read_xls(filename, 2)
            sorted_data = Business.sort_data(file_data)
            # to_int_data = Business.float_to_int(sorted_data)
            data_dict['success'] = '查看成功'
        except Exception as e:
            data_dict['success'] = '查看失败'
            print('查看文件数据失败:{}'.format(e))
    data_dict['data'] = sorted_data
    return render(request, 'two/import.html', data_dict)
