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
from Model.models import Field24Table
from Model.models import Field2Table
from Model.models import Field3Table
from Model2.models import Field37Table
from Model3 import Business, DB
from Model3.models import DataTable, Field71Table

COLUMN_NAMES = ['auto_id', 'field1', 'field2', 'field3',
                'field24',
                'field23', 'field46', 'field47', 'field48',
                'field49',
                'field37', 'field50', 'field51', 'field52',
                'field53',
                'field54', 'field55', 'field56', 'field57',
                'field58',
                'field59', 'field60', 'field61', 'field62',
                'field71',
                'field72', 'field73', 'field74', 'field75',
                'field76',
                'field77', 'field78', 'field79', 'field80',
                'field81',
                'field82', 'field83', 'field84', 'field63',
                'field64', 'field65', 'field66', 'field67',
                'field68',
                'field69', ]


def select_html(request):
    data_dict = dict()

    # 查询下拉框
    data_dict['field1'] = Pub.select_column(Field1Table, 'field1')
    data_dict['field2'] = Pub.select_column(Field2Table, 'field1')
    data_dict['field3'] = Pub.select_column(Field3Table, 'field1')
    data_dict['field24'] = Pub.select_column(Field24Table, 'field1')
    data_dict['field23'] = Pub.select_column(Field23Table, 'field1')
    data_dict['field37'] = Pub.select_column(Field37Table, 'field1')
    data_dict['field71'] = Pub.select_column(Field71Table, 'field1')

    select_field1 = Pub.request_data(request, 'GET', 'select_field1', '')
    select_field2 = Pub.request_data(request, 'GET', 'select_field2', '')
    select_field3 = Pub.request_data(request, 'GET', 'select_field3', '')
    select_field23 = Pub.request_data(request, 'GET', 'select_field23', '')
    select_field24 = Pub.request_data(request, 'GET', 'select_field24', '')
    select_field37 = Pub.request_data(request, 'GET', 'select_field37', '')
    select_field48 = Pub.request_data(request, 'GET', 'select_field48', '')
    select_field49 = Pub.request_data(request, 'GET', 'select_field49', '')
    select_field50 = Pub.request_data(request, 'GET', 'select_field50', '')
    select_field52 = Pub.request_data(request, 'GET', 'select_field52', '')
    select_field71 = Pub.request_data(request, 'GET', 'select_field71', '')
    select_field72 = Pub.request_data(request, 'GET', 'select_field72', '')
    select_field55 = Pub.request_data(request, 'GET', 'select_field55', '')
    select_field57 = Pub.request_data(request, 'GET', 'select_field57', '')
    select_field59 = Pub.request_data(request, 'GET', 'select_field59', '')
    select_field61 = Pub.request_data(request, 'GET', 'select_field61', '')
    select_field54 = Pub.request_data(request, 'GET', 'select_field54', '')

    pagesize = int(Pub.request_data(request, 'GET', 'pagesize', Pub.PAGESIZE))
    current_page = int(Pub.request_data(request, 'GET', 'current_page', Pub.CURRENT_PAGE))

    data_dict['current_field1'] = select_field1
    data_dict['current_field2'] = select_field2
    data_dict['current_field3'] = select_field3
    data_dict['current_field24'] = select_field24
    data_dict['current_field23'] = select_field23
    data_dict['current_field37'] = select_field37
    data_dict['current_field48'] = select_field48
    data_dict['current_field49'] = select_field49
    data_dict['current_field50'] = select_field50
    data_dict['current_field52'] = select_field52
    data_dict['current_field71'] = select_field71
    data_dict['current_field72'] = select_field72
    data_dict['current_field55'] = select_field55
    data_dict['current_field57'] = select_field57
    data_dict['current_field59'] = select_field59
    data_dict['current_field61'] = select_field61
    data_dict['current_field54'] = select_field54

    filter_data = DB.select_business(DataTable, field1=select_field1, field2=select_field2,
                                     field3=select_field3,
                                     field23=select_field23, field24=select_field24,
                                     field37=select_field37, field48=select_field48,
                                     field49=select_field49, field71=select_field71,
                                     field50=select_field50, field52=select_field52,
                                     field72=select_field72, field55=select_field55,
                                     field57=select_field57, field59=select_field59,
                                     field61=select_field61, field54=select_field54,
                                     column_names=COLUMN_NAMES)
    remove_data = Business.remove_index_for_data(filter_data)
    sort_data = Business.sort_data(filter_data)
    remove_sort_data = Business.sort_data(remove_data)

    # 分页
    paginator = Paginator(remove_sort_data, pagesize)
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

    folder = '/three/data_{}.xls'.format(Pub.get_time())
    save_path = Pub.EXPORT_FOLDER + folder
    data_dict['file'] = Pub.STATIC_EXPORT_FOLDER + folder
    write_data = Pub.change_auto_id(sort_data)
    source_file = os.path.join(Pub.EXPORT_TEMPLATE_FOLDER, u'ZPW导出模板.xls')
    Pub.append_xls(source_file, save_path, write_data)

    return render(request, 'three/select.html', data_dict)


def add(request):
    Pub.insert_db(DataTable,
                  field1=request.POST['add_field1'],
                  field2=request.POST['add_field2'],
                  field3=request.POST['add_field3'],
                  field24=request.POST['add_field24'],
                  field23=request.POST['add_field23'],
                  field46=request.POST['add_field46'],
                  field47=request.POST['add_field47'],
                  field48=request.POST['add_field48'],
                  field49=request.POST['add_field49'],
                  field37=request.POST['add_field37'],
                  field50=request.POST['add_field50'],
                  field51=request.POST['add_field51'],
                  field52=request.POST['add_field52'],
                  field53=request.POST['add_field53'],
                  field54=request.POST['add_field54'],
                  field55=request.POST['add_field55'],
                  field56=request.POST['add_field56'],
                  field57=request.POST['add_field57'],
                  field58=request.POST['add_field58'],
                  field59=request.POST['add_field59'],
                  field60=request.POST['add_field60'],
                  field61=request.POST['add_field61'],
                  field62=request.POST['add_field62'],
                  field63=request.POST['add_field63'],
                  field64=request.POST['add_field64'],
                  field65=request.POST['add_field65'],
                  field66=request.POST['add_field66'],
                  field67=request.POST['add_field67'],
                  field68=request.POST['add_field68'],
                  field69=request.POST['add_field69'],
                  field71=request.POST['add_field71'],
                  field72=request.POST['add_field72'],
                  field73=request.POST['add_field73'],
                  field74=request.POST['add_field74'],
                  field75=request.POST['add_field75'],
                  field76=request.POST['add_field76'],
                  field77=request.POST['add_field77'],
                  field78=request.POST['add_field78'],
                  field79=request.POST['add_field79'],
                  field80=request.POST['add_field80'],
                  field81=request.POST['add_field81'],
                  field82=request.POST['add_field82'],
                  field83=request.POST['add_field83'],
                  field84=request.POST['add_field84'],
                  )
    return redirect("/three/select.html/")


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
                  field24=request.POST['update_field24'],
                  field23=request.POST['update_field23'],
                  field46=request.POST['update_field46'],
                  field47=request.POST['update_field47'],
                  field48=request.POST['update_field48'],
                  field49=request.POST['update_field49'],
                  field37=request.POST['update_field37'],
                  field50=request.POST['update_field50'],
                  field51=request.POST['update_field51'],
                  field52=request.POST['update_field52'],
                  field53=request.POST['update_field53'],
                  field54=request.POST['update_field54'],
                  field55=request.POST['update_field55'],
                  field56=request.POST['update_field56'],
                  field57=request.POST['update_field57'],
                  field58=request.POST['update_field58'],
                  field59=request.POST['update_field59'],
                  field60=request.POST['update_field60'],
                  field61=request.POST['update_field61'],
                  field62=request.POST['update_field62'],
                  field63=request.POST['update_field63'],
                  field64=request.POST['update_field64'],
                  field65=request.POST['update_field65'],
                  field66=request.POST['update_field66'],
                  field67=request.POST['update_field67'],
                  field68=request.POST['update_field68'],
                  field69=request.POST['update_field69'],
                  field71=request.POST['update_field71'],
                  field72=request.POST['update_field72'],
                  field73=request.POST['update_field73'],
                  field74=request.POST['update_field74'],
                  field75=request.POST['update_field75'],
                  field76=request.POST['update_field76'],
                  field77=request.POST['update_field77'],
                  field78=request.POST['update_field78'],
                  field79=request.POST['update_field79'],
                  field80=request.POST['update_field80'],
                  field81=request.POST['update_field81'],
                  field82=request.POST['update_field82'],
                  field83=request.POST['update_field83'],
                  field84=request.POST['update_field84'],
                  )
    return redirect("/three/select.html/")


def delete(request):
    delete_ids = request.GET['delete_ids']
    ids = delete_ids.split('_')
    ids.pop(len(ids) - 1)  # 去除最后的空串
    for delete_id in ids:
        Pub.delete_db(DataTable, delete_id)
    return redirect("/three/select.html/")


def import_html(request):
    return render(request, 'three/import.html')


def import_data(request):  # 导入
    data_dict = dict()
    calculate_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = BASE_DIR + '/templates/files/import/data_two_{}.xls'.format(
            time.strftime("%Y%m%d%H%M%S", time.localtime()))
        Pub.save_file(filename, file)
        try:
            file_data = Pub.read_xls(filename, 5)
            sorted_data = Business.sort_data(file_data)
            calculate_data = Business.all_row(sorted_data)
            ret, msg = Business.can_import(calculate_data)
            if ret is True:
                pop_data = Pub.pop_first(calculate_data)
                for one_data in pop_data:
                    Pub.insert_db(DataTable,
                                  field1=one_data[0],
                                  field2=one_data[1],
                                  field3=one_data[2],
                                  field24=one_data[3],
                                  field23=one_data[4],
                                  field46=one_data[5],
                                  field47=one_data[6],
                                  field48=one_data[7],
                                  field49=one_data[8],
                                  field37=one_data[9],
                                  field50=one_data[10],
                                  field51=one_data[11],
                                  field52=one_data[12],
                                  field53=one_data[13],
                                  field54=one_data[14],
                                  field55=one_data[15],
                                  field56=one_data[16],
                                  field57=one_data[17],
                                  field58=one_data[18],
                                  field59=one_data[19],
                                  field60=one_data[20],
                                  field61=one_data[21],
                                  field62=one_data[22],
                                  field71=one_data[23],
                                  field72=one_data[24],
                                  field73=one_data[25],
                                  field74=one_data[26],
                                  field75=one_data[27],
                                  field76=one_data[28],
                                  field77=one_data[29],
                                  field78=one_data[30],
                                  field79=one_data[31],
                                  field80=one_data[32],
                                  field81=one_data[33],
                                  field82=one_data[34],
                                  field83=one_data[35],
                                  field63=one_data[36],
                                  field64=one_data[37],
                                  field65=one_data[38],
                                  field66=one_data[39],
                                  field67=one_data[40],
                                  field68=one_data[41],
                                  field69=one_data[42], )
                data_dict['success'] = '导入成功'
            else:
                data_dict['success'] = '导入失败->{}'.format(msg)
        except Exception as e:
            data_dict['success'] = '导入失败->{}'.format(e)
            print('导入文件失败:{}'.format(e))
    data_dict['data'] = calculate_data
    return render(request, 'three/import.html', data_dict)


def check_data(request):
    data_dict = dict()
    calculate_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = BASE_DIR + '/templates/files/import/data_two_{}.xls'.format(
            time.strftime("%Y%m%d%H%M%S", time.localtime()))
        Pub.save_file(filename, file)
        try:
            file_data = Pub.read_xls(filename, 5)
            sorted_data = Business.sort_data(file_data)
            calculate_data = Business.all_row(sorted_data)
            data_dict['success'] = '查看成功'
        except Exception as e:
            data_dict['success'] = '查看失败'
            print('查看文件数据失败:{}'.format(e))
    data_dict['data'] = calculate_data
    return render(request, 'three/import.html', data_dict)
