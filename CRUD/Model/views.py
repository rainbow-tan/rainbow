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
from Model import DB, Business
from Model.models import DataTable
from Model.models import Field1Table
from Model.models import Field24Table
from Model.models import Field25Table
from Model.models import Field26Table
from Model.models import Field27Table
from Model.models import Field2Table
from Model.models import Field3Table

COLUMN_NAMES = ['auto_id', 'field1', 'field2', 'field3', 'field4', 'field5',
                'field6', 'field7', 'field8', 'field9', 'field70', 'field10', 'field11',
                'field12', 'field13', 'field14', 'field15', 'field16', 'field17',
                'field18', 'field19', 'field20', 'field21', 'field22',
                'field24', 'field25', 'field26', 'field27', 'field28', 'field29', ]


def import_html(request):
    return render(request, 'one/import.html')


def select_html(request):
    data_dict = dict()

    # 查询下拉框
    data_dict['field1'] = Pub.select_column(Field1Table, 'field1')
    data_dict['field2'] = Pub.select_column(Field2Table, 'field1')
    data_dict['field3'] = Pub.select_column(Field3Table, 'field1')
    data_dict['field24'] = Pub.select_column(Field24Table, 'field1')
    data_dict['field25'] = Pub.select_column(Field25Table, 'field1')
    data_dict['field26'] = Pub.select_column(Field26Table, 'field1')
    data_dict['field27'] = Pub.select_column(Field27Table, 'field1')

    select_field1 = Pub.request_data(request, 'GET', 'select_field1', '')
    select_field2 = Pub.request_data(request, 'GET', 'select_field2', '')
    select_field3 = Pub.request_data(request, 'GET', 'select_field3', '')
    select_field4 = Pub.request_data(request, 'GET', 'select_field4', '')
    select_field16 = Pub.request_data(request, 'GET', 'select_field16', '')
    select_field17 = Pub.request_data(request, 'GET', 'select_field17', '')
    select_field18 = Pub.request_data(request, 'GET', 'select_field18', '')
    select_field24 = Pub.request_data(request, 'GET', 'select_field24', '')
    select_field25 = Pub.request_data(request, 'GET', 'select_field25', '')
    select_field26 = Pub.request_data(request, 'GET', 'select_field26', '')
    select_field27 = Pub.request_data(request, 'GET', 'select_field27', '')
    select_field28 = Pub.request_data(request, 'GET', 'select_field28', '')
    over_limit = Pub.request_data(request, 'GET', 'over_limit', '')

    pagesize = int(Pub.request_data(request, 'GET', 'pagesize', Pub.PAGESIZE))
    current_page = int(Pub.request_data(request, 'GET', 'current_page', Pub.CURRENT_PAGE))

    data_dict['current_field1'] = select_field1
    data_dict['current_field2'] = select_field2
    data_dict['current_field3'] = select_field3
    data_dict['current_field4'] = select_field4
    data_dict['current_field16'] = select_field16
    data_dict['current_field17'] = select_field17
    data_dict['current_field18'] = select_field18
    data_dict['current_field24'] = select_field24
    data_dict['current_field25'] = select_field25
    data_dict['current_field26'] = select_field26
    data_dict['current_field27'] = select_field27
    data_dict['current_field28'] = select_field28
    data_dict['over_limit'] = over_limit

    # 默认不查询
    if select_field1 == '' and select_field2 == '' and select_field3 == '' and select_field4 == '' \
            and select_field16 == '' and select_field17 == '' and select_field18 == '' \
            and select_field24 == '' and select_field25 == '' \
            and select_field26 == '' and select_field27 == '' and select_field28 == '' \
            and over_limit == '':
        filter_data = []
    else:
        filter_data = DB.select_business(DataTable, select_field1, select_field2, select_field3,
                                         select_field4,
                                         select_field16, select_field17, select_field18,
                                         select_field24, select_field25, select_field26,
                                         select_field27, select_field28, over_limit, COLUMN_NAMES)
    sort_filter_data = Business.sort_data(filter_data)
    remove_sort_filter_data = Business.remove_index_for_data(sort_filter_data)  # 移除四个不显示字段
    # 分页
    paginator = Paginator(remove_sort_filter_data, pagesize)
    if current_page > paginator.num_pages:  # 当前页大于总分页默认最后一页
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

    # 前一页
    if current_page - 1 > 0:
        previous_page = current_page - 1
    else:
        previous_page = 1
    # 后一页
    if current_page + 1 < paginator.num_pages:
        next_page = current_page + 1
    else:
        next_page = paginator.num_pages
    data_dict['data'] = show_data
    data_dict['count'] = len(filter_data)  # 数据总条数
    data_dict['pagesize'] = str(pagesize)
    data_dict['previous_page'] = previous_page
    data_dict['current_page'] = str(current_page)
    data_dict['next_page'] = next_page
    data_dict['last_page'] = paginator.num_pages

    folder = '/one/data_{}.xls'.format(Pub.get_time())
    save_path = Pub.EXPORT_FOLDER + folder
    data_dict['file'] = Pub.STATIC_EXPORT_FOLDER + folder
    write_data = Pub.change_auto_id(sort_filter_data)
    source_file = os.path.join(Pub.EXPORT_TEMPLATE_FOLDER, u'限界导出模板.xls')
    Pub.append_xls(source_file, save_path, write_data)
    return render(request, 'one/select.html', data_dict)


def add(request):
    Pub.insert_db(DataTable,
                  field1=request.POST['add_field1'],
                  field2=request.POST['add_field2'],
                  field3=request.POST['add_field3'],
                  field4=request.POST['add_field4'],
                  field5=request.POST['add_field5'],
                  field6=request.POST['add_field6'],
                  field7=request.POST['add_field7'],
                  field8=request.POST['add_field8'],
                  field9=request.POST['add_field9'],
                  field70=request.POST['add_field70'],
                  field10=request.POST['add_field10'],
                  field11=request.POST['add_field11'],
                  field12=request.POST['add_field12'],
                  field13=request.POST['add_field13'],
                  field14=request.POST['add_field14'],
                  field15=request.POST['add_field15'],
                  field16=request.POST['add_field16'],
                  field17=request.POST['add_field17'],
                  field18=request.POST['add_field18'],
                  field19=request.POST['add_field19'],
                  field20=request.POST['add_field20'],
                  field21=request.POST['add_field21'],
                  field22=request.POST['add_field22'],
                  field24=request.POST['add_field24'],
                  field25=request.POST['add_field25'],
                  field26=request.POST['add_field26'],
                  field27=request.POST['add_field27'],
                  field28=request.POST['add_field28'],
                  field29=request.POST['add_field29'])
    return redirect("/one/select.html/")


def update(request):
    Pub.update_db(DataTable, request.POST['update_id'],
                  field1=request.POST['update_field1'],
                  field2=request.POST['update_field2'],
                  field3=request.POST['update_field3'],
                  field4=request.POST['update_field4'],
                  field5=request.POST['update_field5'],
                  field6=request.POST['update_field6'],
                  field7=request.POST['update_field7'],
                  field8=request.POST['update_field8'],
                  field9=request.POST['update_field9'],
                  field70=request.POST['update_field70'],
                  field10=request.POST['update_field10'],
                  field11=request.POST['update_field11'],
                  field12=request.POST['update_field12'],
                  field13=request.POST['update_field13'],
                  field14=request.POST['update_field14'],
                  field15=request.POST['update_field15'],
                  field16=request.POST['update_field16'],
                  field17=request.POST['update_field17'],
                  field18=request.POST['update_field18'],
                  field19=request.POST['update_field19'],
                  field20=request.POST['update_field20'],
                  field21=request.POST['update_field21'],
                  field22=request.POST['update_field22'],
                  field24=request.POST['update_field24'],
                  field25=request.POST['update_field25'],
                  field26=request.POST['update_field26'],
                  field27=request.POST['update_field27'],
                  field28=request.POST['update_field28'],
                  field29=request.POST['update_field29'])
    return redirect("/one/select.html/")


def delete(request):
    delete_ids = request.GET['delete_ids']
    ids = delete_ids.split('_')
    ids.pop(len(ids) - 1)  # 去除最后的空串
    for delete_id in ids:
        Pub.delete_db(DataTable, delete_id)
    return redirect("/one/select.html/")


def select_for_update(request):  # 为了修改查询数据
    data_dict = dict()
    data = Pub.select_db_one(DataTable, request.GET['update_id'], COLUMN_NAMES)
    for index, column_name in enumerate(COLUMN_NAMES):
        data_dict['src_update_{}'.format(column_name)] = data[index]
    return HttpResponse(json.dumps(data_dict), content_type="application/json")


def check_data(request):
    data_dict = dict()
    remove_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = BASE_DIR + '/templates/files/import/data_{}.xls'.format(
            time.strftime("%Y%m%d%H%M%S", time.localtime()))
        Pub.save_file(filename, file)
        try:
            file_data = Pub.read_xls(filename, 5)
            deal_data = Business.calculation_line(file_data)
            sorted_data = Business.sort_data(deal_data)
            remove_data = Business.remove_index_for_data(sorted_data)
            data_dict['success'] = '查看成功'
        except Exception as e:
            print('查看文件数据失败:{}'.format(e))
            data_dict['success'] = '查看失败->{}'.format(e)
    data_dict['data'] = remove_data
    return render(request, 'one/import.html', data_dict)


def import_data(request):  # 导入
    data_dict = dict()
    remove_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = BASE_DIR + '/templates/files/import/data_{}.xls'.format(
            time.strftime("%Y%m%d%H%M%S", time.localtime()))
        Pub.save_file(filename, file)
        try:
            file_data = Pub.read_xls(filename, 5)
            deal_data = Business.calculation_line(file_data)
            sorted_data = Business.sort_data(deal_data)
            ret, msg = Business.can_import(sorted_data)
            if ret is True:
                pop_data = Pub.pop_first(sorted_data)
                for one_data in pop_data:
                    Pub.insert_db(DataTable,
                                  field1=one_data[0],
                                  field2=one_data[1],
                                  field3=one_data[2],
                                  field4=one_data[3],
                                  field5=one_data[4],
                                  field6=one_data[5],
                                  field7=one_data[6],
                                  field8=one_data[7],
                                  field9=one_data[8],
                                  field70=one_data[9],
                                  field10=one_data[10],
                                  field11=one_data[11],
                                  field12=one_data[12],
                                  field13=one_data[13],
                                  field14=one_data[14],
                                  field15=one_data[15],
                                  field16=one_data[16],
                                  field17=one_data[17],
                                  field18=one_data[18],
                                  field19=one_data[19],
                                  field20=one_data[20],
                                  field21=one_data[21],
                                  field22=one_data[22],
                                  field24=one_data[23],
                                  field25=one_data[24],
                                  field26=one_data[26 - 1],
                                  field27=one_data[27 - 1],
                                  field28=one_data[28 - 1],
                                  field29=one_data[29 - 1], )
                remove_data = Business.remove_index_for_data(sorted_data)  # 移除不显示字段
                data_dict['success'] = '导入成功'
            else:
                data_dict['success'] = '导入失败->{}'.format(msg)
        except Exception as e:
            print('导入文件失败:{}'.format(e))
            data_dict['success'] = '导入失败->{}'.format(e)
    data_dict['data'] = remove_data
    return render(request, 'one/import.html', data_dict)
