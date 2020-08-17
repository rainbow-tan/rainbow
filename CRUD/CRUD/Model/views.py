# -*- encoding=utf-8 -*-
import time

from django.shortcuts import render, redirect
from DataManagement import PublicMode
from CRUD.settings import BASE_DIR
from Model import DB
from DataManagement import Business


def login_html(request):
    return render(request, 'login.html')


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username == 'admin' and password == 'admin':
        response = redirect("/select.html/")
        response.set_cookie("is_admin", True)
    elif username == 'root' and password == 'root':
        response = redirect("/select.html/")
        response.set_cookie("is_admin", False)
    else:
        response = redirect("/login.html/")
    return response


def select_html(request):
    data_dict = dict()
    page = 'page'
    cut = ''
    if page in request.GET and request.GET[page] != '':
        cut = int(request.GET[page])
        data_dict['next'] = cut + 30
        data_dict['before'] = cut - 30
    all_data_list = DB.select_all('DataTable', 29)
    if cut != '':
        data_dict['data'] = all_data_list[cut - 30:cut]
    else:
        data_dict['data'] = all_data_list

    save_path = '/files/data_{}.xls'.format(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    file_name = BASE_DIR + '/templates' + save_path
    data_dict['file_path'] = '/static' + save_path
    write_data = PublicMode.change_auto_id(all_data_list)
    PublicMode.write_xls(file_name, write_data)
    return render(request, 'select.html', data_dict)


def add_html(request):
    print(request.COOKIES.get('is_admin'))
    print(request.COOKIES.get('is_admin1'))
    data_dict = dict()
    data_dict['field1'] = DB.select_column('Field1Table', 'field1')
    data_dict['field2'] = DB.select_column('Field2Table', 'field1')
    data_dict['field3'] = DB.select_column('Field3Table', 'field1')
    data_dict['field23'] = DB.select_column('Field23Table', 'field1')
    data_dict['field24'] = DB.select_column('Field24Table', 'field1')
    data_dict['field25'] = DB.select_column('Field25Table', 'field1')
    data_dict['field26'] = DB.select_column('Field26Table', 'field1')
    data_dict['field27'] = DB.select_column('Field27Table', 'field1')
    return render(request, 'add.html', data_dict)


def add(request):
    DB.insert('DataTable', [request.POST['field1'], request.POST['field2'], request.POST['field3'],
                            request.POST['field4'], request.POST['field5'], request.POST['field6'],
                            request.POST['field7'], request.POST['field8'], request.POST['field9'],
                            request.POST['field10'], request.POST['field11'],
                            request.POST['field12'], request.POST['field13'],
                            request.POST['field14'], request.POST['field15'],
                            request.POST['field16'], request.POST['field17'],
                            request.POST['field18'], request.POST['field19'],
                            request.POST['field20'], request.POST['field21'],
                            request.POST['field22'], request.POST['field23'],
                            request.POST['field24'], request.POST['field25'],
                            request.POST['field26'], request.POST['field27'],
                            request.POST['field28'], request.POST['field29'], ])
    return redirect("/select.html/")


def update_html(request):
    data_dict = dict()
    one_data = DB.select_one('DataTable', 29, request.GET['update_id'])
    index = 0
    for data in one_data:
        data_dict['current_field{}'.format(index)] = data
        index += 1
    data_dict['auto_id'] = data_dict['current_field0']
    data_dict['field1'] = DB.select_column('Field1Table', 'field1')
    data_dict['field2'] = DB.select_column('Field2Table', 'field1')
    data_dict['field3'] = DB.select_column('Field3Table', 'field1')
    data_dict['field23'] = DB.select_column('Field23Table', 'field1')
    data_dict['field24'] = DB.select_column('Field24Table', 'field1')
    data_dict['field25'] = DB.select_column('Field25Table', 'field1')
    data_dict['field26'] = DB.select_column('Field26Table', 'field1')
    data_dict['field27'] = DB.select_column('Field27Table', 'field1')
    return render(request, 'update.html', data_dict)


def update(request):
    DB.update('DataTable', request.POST['auto_id'], request.POST['field1'], request.POST['field2'],
              request.POST['field3'], request.POST['field4'], request.POST['field5'],
              request.POST['field6'], request.POST['field7'], request.POST['field8'],
              request.POST['field9'], request.POST['field10'], request.POST['field11'],
              request.POST['field12'], request.POST['field13'], request.POST['field14'],
              request.POST['field15'], request.POST['field16'], request.POST['field17'],
              request.POST['field18'], request.POST['field19'], request.POST['field20'],
              request.POST['field21'], request.POST['field22'], request.POST['field23'],
              request.POST['field24'], request.POST['field25'], request.POST['field26'],
              request.POST['field27'], request.POST['field28'], request.POST['field29'], )

    return redirect("/select.html/")


def delete(request):
    delete_ids = request.GET['delete_ids']
    ids = delete_ids.split('_')
    ids.pop(len(ids) - 1)  # 去除最后的空串
    for delete_id in ids:
        DB.delete('DataTable', delete_id)

    return redirect("/select.html/")


def to_lead_html(request):
    return render(request, 'to_lead.html')


def upload(request):  # 导入
    data_dict = dict()
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = BASE_DIR + '/templates/files/data_{}.xls'.format(
            time.strftime("%Y%m%d%H%M%S", time.localtime()))
        PublicMode.save_file(filename, file)
        file_data = PublicMode.read_xls(filename)
        data_dict['data'] = file_data
        deal_data = Business.calculation_line(file_data)
        pop_data = Business.pop_first(deal_data)
        for one_data in pop_data:
            DB.insert('DataTable', one_data)
    return render(request, 'to_lead.html', data_dict)


def choose_select_html(request):
    data_dict = dict()
    data_dict['field1'] = DB.select_column('Field1Table', 'field1')
    data_dict['field2'] = DB.select_column('Field2Table', 'field1')
    data_dict['field3'] = DB.select_column('Field3Table', 'field1')
    data_dict['field23'] = DB.select_column('Field23Table', 'field1')
    data_dict['field24'] = DB.select_column('Field24Table', 'field1')
    data_dict['field25'] = DB.select_column('Field25Table', 'field1')
    data_dict['field26'] = DB.select_column('Field26Table', 'field1')
    data_dict['field27'] = DB.select_column('Field27Table', 'field1')

    all_data_list = DB.select_all('DataTable', 29)
    save_path = '/files/data_{}.xls'.format(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    file_name = BASE_DIR + '/templates' + save_path
    data_dict['file_path'] = '/static' + save_path
    write_data = PublicMode.change_auto_id(all_data_list)
    PublicMode.write_xls(file_name, write_data)
    return render(request, 'choose_select.html', data_dict)


def choose_select(request):
    data_dict = dict()
    data_dict['field1'] = DB.select_column('Field1Table', 'field1')
    data_dict['field2'] = DB.select_column('Field2Table', 'field1')
    data_dict['field3'] = DB.select_column('Field3Table', 'field1')
    data_dict['field23'] = DB.select_column('Field23Table', 'field1')
    data_dict['field24'] = DB.select_column('Field24Table', 'field1')
    data_dict['field25'] = DB.select_column('Field25Table', 'field1')
    data_dict['field26'] = DB.select_column('Field26Table', 'field1')
    data_dict['field27'] = DB.select_column('Field27Table', 'field1')
    data_dict['current_field1'] = request.POST['field1']
    data_dict['current_field2'] = request.POST['field2']
    data_dict['current_field3'] = request.POST['field3']
    data_dict['current_field16'] = request.POST['field16']
    data_dict['current_field17'] = request.POST['field17']
    data_dict['current_field21'] = request.POST['field21']
    data_dict['current_field22'] = request.POST['field22']
    data_dict['current_field23'] = request.POST['field23']
    data_dict['current_field24'] = request.POST['field24']
    data_dict['current_field25'] = request.POST['field25']
    data_dict['current_field26'] = request.POST['field26']
    data_dict['current_field27'] = request.POST['field27']

    all_data_list = DB.select_filter('DataTable', 29, request.POST['field1'],
                                     request.POST['field2'],
                                     request.POST['field3'], request.POST['field16'],
                                     request.POST['field17'], request.POST['field21'],
                                     request.POST['field22'],
                                     request.POST['field23'],
                                     request.POST['field24'], request.POST['field25'],
                                     request.POST['field26'], request.POST['field27'], )

    data_dict['data'] = all_data_list
    save_path = '/files/data_{}.xls'.format(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    file_name = BASE_DIR + '/templates' + save_path
    data_dict['file_path'] = '/static' + save_path
    write_data = PublicMode.change_auto_id(all_data_list)
    PublicMode.write_xls(file_name, write_data)
    return render(request, 'choose_select.html', data_dict)


def debug(request):
    return render(request, 'select.html')
