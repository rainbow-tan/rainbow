# -*- encoding=utf-8 -*-
import json
import time

from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from CRUD.settings import BASE_DIR
from DataManagement import Business
from DataManagement import PublicMode
from Model import DB


def login_html(request):
    return render(request, 'login.html')


def index_html(request):
    return render(request, 'index.html')


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    if username == 'admin' and password == 'admin':
        response = redirect("/index.html/")
        response.set_cookie("is_admin", True)
    elif username == 'root' and password == 'root':
        response = redirect("/index.html/")
        response.set_cookie("is_admin", False)
    else:
        response = redirect("/login.html/")
    # debug
    # response = redirect("/index.html/")
    return response


def select_html(request):
    data_dict = dict()

    # 查询下拉框
    data_dict['field1'] = DB.select_column('Field1Table', 'field1')
    data_dict['field2'] = DB.select_column('Field2Table', 'field1')
    data_dict['field3'] = DB.select_column('Field3Table', 'field1')
    data_dict['field23'] = DB.select_column('Field23Table', 'field1')
    data_dict['field24'] = DB.select_column('Field24Table', 'field1')
    data_dict['field25'] = DB.select_column('Field25Table', 'field1')
    data_dict['field26'] = DB.select_column('Field26Table', 'field1')
    data_dict['field27'] = DB.select_column('Field27Table', 'field1')
    select_field1 = PublicMode.request_data(request, 'GET', 'select_field1', '')
    select_field2 = PublicMode.request_data(request, 'GET', 'select_field2', '')
    select_field3 = PublicMode.request_data(request, 'GET', 'select_field3', '')
    select_field23 = PublicMode.request_data(request, 'GET', 'select_field23', '')
    select_field24 = PublicMode.request_data(request, 'GET', 'select_field24', '')
    select_field25 = PublicMode.request_data(request, 'GET', 'select_field25', '')
    select_field26 = PublicMode.request_data(request, 'GET', 'select_field26', '')
    select_field27 = PublicMode.request_data(request, 'GET', 'select_field27', '')
    select_field16 = PublicMode.request_data(request, 'GET', 'select_field16', '')
    select_field17 = PublicMode.request_data(request, 'GET', 'select_field17', '')
    over_limit = PublicMode.request_data(request, 'GET', 'over_limit', '')
    pagesize = 20
    current_page = 1
    try:
        pagesize = int(PublicMode.request_data(request, 'GET', 'pagesize', pagesize))
        current_page = int(PublicMode.request_data(request, 'GET', 'current_page', current_page))
    except Exception as e:
        print('未获取到分页信息:{}'.format(e))
        print('使用默认,每页显示数据条数:{}'.format(pagesize))
        print('使用默认,当前页:{}'.format(current_page))
    data_dict['current_field1'] = select_field1
    data_dict['current_field2'] = select_field2
    data_dict['current_field3'] = select_field3
    data_dict['current_field16'] = select_field16
    data_dict['current_field17'] = select_field17
    data_dict['current_field23'] = select_field23
    data_dict['current_field24'] = select_field24
    data_dict['current_field25'] = select_field25
    data_dict['current_field26'] = select_field26
    data_dict['current_field27'] = select_field27
    data_dict['over_limit'] = over_limit

    # 没有条件时查出来就是所有
    if over_limit == '':
        filter_data = DB.select_filter_and('DataTable', 29, '', select_field1, select_field2,
                                           select_field3, '', '', '', '', '', '', '', '', '', '',
                                           '', '', select_field16, select_field17, '', '', '', '',
                                           '', select_field23, select_field24, select_field25,
                                           select_field26, select_field27, '', '', )
    elif over_limit == '否':
        filter_data = DB.select_filter('DataTable', 29)  # 业务
    elif over_limit == '是':
        filter_data = DB.select_filter_or('DataTable', 29, '', '', '', '', '', '', '', '', '', '',
                                          '', '', '', '', '', '', '', '', '', '', '', '是', '是', '',
                                          '', '', '', '', '', '', )
    else:
        filter_data = []
    filter_data = PublicMode.sort_data(filter_data)
    remove_filter_data = PublicMode.remove_index_for_data(filter_data)  # 移除四个不显示字段
    # 分页
    paginator = Paginator(remove_filter_data, pagesize)
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
    PublicMode.delete_folder(BASE_DIR + '/templates/files/export', 1024 * 1024 * 100)
    PublicMode.delete_folder(BASE_DIR + '/templates/files/import', 1024 * 1024 * 100)
    save_path = '/files/export/data_{}.xls'.format(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    file_name = BASE_DIR + '/templates' + save_path
    data_dict['file'] = '/static' + save_path
    write_data = PublicMode.change_auto_id(filter_data)
    PublicMode.append_xls(file_name, write_data)
    return render(request, 'one/select.html', data_dict)


def add(request):
    DB.insert('DataTable',
              [request.POST['add_field1'], request.POST['add_field2'], request.POST['add_field3'],
               request.POST['add_field4'], request.POST['add_field5'], request.POST['add_field6'],
               request.POST['add_field7'], request.POST['add_field8'], request.POST['add_field9'],
               request.POST['add_field10'], request.POST['add_field11'],
               request.POST['add_field12'], request.POST['add_field13'],
               request.POST['add_field14'], request.POST['add_field15'],
               request.POST['add_field16'], request.POST['add_field17'],
               request.POST['add_field18'], request.POST['add_field19'],
               request.POST['add_field20'], request.POST['add_field21'],
               request.POST['add_field22'], request.POST['add_field23'],
               request.POST['add_field24'], request.POST['add_field25'],
               request.POST['add_field26'], request.POST['add_field27'],
               request.POST['add_field28'], request.POST['add_field29'], ])
    return redirect("/select.html/")


def update(request):
    DB.update('DataTable', request.POST['update_id'],
              request.POST['update_field1'], request.POST['update_field2'],
              request.POST['update_field3'], request.POST['update_field4'],
              request.POST['update_field5'], request.POST['update_field6'],
              request.POST['update_field7'], request.POST['update_field8'],
              request.POST['update_field9'], request.POST['update_field10'],
              request.POST['update_field11'], request.POST['update_field12'],
              request.POST['update_field13'], request.POST['update_field14'],
              request.POST['update_field15'], request.POST['update_field16'],
              request.POST['update_field17'], request.POST['update_field18'],
              request.POST['update_field19'], request.POST['update_field20'],
              request.POST['update_field21'], request.POST['update_field22'],
              request.POST['update_field23'], request.POST['update_field24'],
              request.POST['update_field25'], request.POST['update_field26'],
              request.POST['update_field27'], request.POST['update_field28'],
              request.POST['update_field29'], )
    return redirect("/select.html/")


def delete(request):
    delete_ids = request.GET['delete_ids']
    ids = delete_ids.split('_')
    ids.pop(len(ids) - 1)  # 去除最后的空串
    for delete_id in ids:
        DB.delete('DataTable', delete_id)
    return redirect("/select.html/")


def import_data(request):  # 导入
    data_dict = dict()
    remove_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = BASE_DIR + '/templates/files/import/data_{}.xls'.format(
            time.strftime("%Y%m%d%H%M%S", time.localtime()))
        PublicMode.save_file(filename, file)
        try:
            file_data = PublicMode.read_xls(filename)
            deal_data = Business.calculation_line(file_data)
            sorted_data = PublicMode.sort_data(deal_data)
            if PublicMode.can_import(sorted_data) is True:
                pop_data = Business.pop_first(sorted_data)
                for one_data in pop_data:
                    DB.insert('DataTable', one_data)
                remove_data = PublicMode.remove_index_for_data(sorted_data)  # 移除不显示字段
                data_dict['success'] = '导入成功'
            else:
                data_dict['success'] = '导入失败'
        except Exception as e:
            data_dict['success'] = '导入失败'
            print('导入文件失败:{}'.format(e))
    data_dict['data'] = remove_data
    return render(request, 'one/import.html', data_dict)


def debug(request):
    data = [[1, 2], [3, 4]]
    return render(request, 'debug.html')


def select_for_update(request):  # 为了修改查询数据
    data_dict = dict()
    one_data = DB.select_one('DataTable', 29, request.GET['update_id'])
    index = 0
    for data in one_data:
        data_dict['src_update_field{}'.format(index)] = data
        index += 1
    return HttpResponse(json.dumps(data_dict), content_type="application/json")


def import_html(request):
    return render(request, 'one/import.html')


def check_data(request):
    data_dict = dict()
    remove_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = BASE_DIR + '/templates/files/import/data_{}.xls'.format(
            time.strftime("%Y%m%d%H%M%S", time.localtime()))
        PublicMode.save_file(filename, file)
        try:
            file_data = PublicMode.read_xls(filename)
            deal_data = Business.calculation_line(file_data)
            sorted_data = PublicMode.sort_data(deal_data)
            remove_data = PublicMode.remove_index_for_data(sorted_data)
            data_dict['success'] = '查看成功'
        except Exception as e:
            data_dict['success'] = '查看失败'
            print('查看文件数据失败:{}'.format(e))
    data_dict['data'] = remove_data
    return render(request, 'one/import.html', data_dict)
