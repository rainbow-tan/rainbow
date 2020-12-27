# -*- encoding=utf-8 -*-
import json
import os
import random

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from Cubing import Pub
from Cubing.BarCode import BarCode
from Cubing.Business import scarp_data
from Cubing.Business import select_no_baofei
from Cubing.Business import yichu_erweima
from Model import DB
from Model.models import PartTable

COLUMN_NAMES = ['sn', 'qrcode', 'pn', 'part_name', 'car_type', 'producer', 'receive_date', 'batch',
                'send_people', 'contact',
                'use', 'receive_people', 'deal_mode', 'deal_remark',
                'deal_date', ]


def import_html(request):
    return render(request, 'one/import.html')


def select_html(request):
    data_dict = dict()

    # 查询下拉框
    pn = Pub.select_column(PartTable, 'pn')
    part_name = Pub.select_column(PartTable, 'part_name')
    car_type = Pub.select_column(PartTable, 'car_type')
    producer = Pub.select_column(PartTable, 'producer')
    receive_people = Pub.select_column(PartTable, 'receive_people')
    use = Pub.select_column(PartTable, 'use')

    data_dict['pn'] = pn
    data_dict['part_name'] = part_name
    data_dict['car_type'] = car_type
    data_dict['producer'] = producer
    data_dict['receive_people'] = receive_people
    data_dict['use'] = use

    # 前端数据
    select_pn = Pub.request_data(request, 'GET', 'select_pn', '')
    select_part_name = Pub.request_data(request, 'GET', 'select_part_name', '')
    select_car_type = Pub.request_data(request, 'GET', 'select_car_type', '')
    select_use = Pub.request_data(request, 'GET', 'select_use', '')
    select_receive_date = Pub.request_data(request, 'GET', 'select_receive_date', '')
    select_deal_date = Pub.request_data(request, 'GET', 'select_deal_date', '')
    select_receive_people = Pub.request_data(request, 'GET', 'select_receive_people', '')

    data_dict['select_pn'] = select_pn
    data_dict['select_part_name'] = select_part_name
    data_dict['select_car_type'] = select_car_type
    data_dict['select_use'] = select_use
    data_dict['select_receive_date'] = select_receive_date
    data_dict['select_receive_people'] = select_receive_people

    # 分页
    pagesize = int(Pub.request_data(request, 'GET', 'pagesize', Pub.PAGESIZE))
    data_dict['pagesize'] = pagesize
    current_page = int(Pub.request_data(request, 'GET', 'current_page', Pub.CURRENT_PAGE))
    data_dict['current_page'] = current_page

    select_tiaojian = {
        'pn': select_pn, 'part_name': select_part_name, 'car_type': select_car_type,
        'use': select_use, 'receive_date': select_receive_date, 'deal_date': select_deal_date,
        'receive_people': select_receive_people,
        }
    no_baofei_xianshi = ['sn', 'qrcode', 'pn', 'part_name', 'car_type', 'producer', 'receive_date',
                         'batch', 'send_people', 'contact', 'use', 'receive_people', ]
    filter_data = select_no_baofei(PartTable, 'AND', select_tiaojian, no_baofei_xianshi)

    # 分页
    paginator = Paginator(filter_data, pagesize)
    last_page = paginator.num_pages
    data_dict['last_page'] = last_page
    if current_page > last_page:  # 当前页大于总分页默认最后一页
        current_page = last_page
    try:
        show_data = paginator.page(current_page)
    except Exception as e:
        show_data = paginator.page(1)

    # 前一页
    if current_page - 1 > 0:
        previous_page = current_page - 1
    else:
        previous_page = 1
    data_dict['previous_page'] = previous_page

    # 后一页
    if current_page + 1 < last_page:
        next_page = current_page + 1
    else:
        next_page = last_page
    data_dict['next_page'] = next_page
    data_dict['data'] = show_data.object_list
    data_dict['count'] = len(filter_data)  # 数据总条数

    # 查询导出xls
    folder = '/one/data_{}.xls'.format(Pub.get_time())
    save_path = Pub.EXPORT_FOLDER + folder
    data_dict['file'] = Pub.STATIC_EXPORT_FOLDER + folder
    write_data = filter_data
    write_data = yichu_erweima(write_data)
    source_file = os.path.join(Pub.EXPORT_TEMPLATE_FOLDER, u'select_export.xls')
    Pub.append_xls(source_file, save_path, write_data)

    return render(request, 'one/select.html', data_dict)


def add(request):
    current_user = request.POST['add_curretn_user']
    for i in range(int(request.POST['add_save_count'])):
        while True:
            r = random.randint(1, 99999)
            r_str = 'QA' + str(r).rjust(5, '0')
            uses = Pub.select_column(PartTable, 'use')
            if r_str not in uses:
                break
        Pub.insert_db(PartTable,
                      pn=request.POST['add_pn'],
                      part_name=request.POST['add_part_name'],
                      car_type=request.POST['add_car_type'],
                      producer=request.POST['add_producer'],
                      receive_date=request.POST['add_receive_date'],
                      batch=request.POST['add_batch'],
                      send_people=request.POST['add_send_people'],
                      contact=request.POST['add_contact'],
                      save_count=1,
                      deal_count=0,
                      receive_people=request.POST['add_receive_people'],
                      qrcode=r_str,
                      use=request.POST['add_use']
                      )
    return redirect("/one/select.html/?select_receive_people={}".format(current_user))


def update(request):
    current_user = request.POST['update_curretn_user']
    Pub.update_db(PartTable, request.POST['update_sn'],
                  pn=request.POST['update_pn'],
                  part_name=request.POST['update_part_name'],
                  car_type=request.POST['update_car_type'],
                  producer=request.POST['update_producer'],
                  receive_date=request.POST['update_receive_date'],
                  batch=request.POST['update_batch'],
                  send_people=request.POST['update_send_people'],
                  contact=request.POST['update_contact'],
                  save_count=request.POST['update_save_count'],
                  deal_count=request.POST['update_deal_count'],
                  receive_people=request.POST['update_receive_people'],
                  deal_mode=request.POST['update_deal_mode'],
                  deal_remark=request.POST['update_deal_remark'],
                  deal_date=request.POST['update_deal_date'],
                  use=request.POST['update_use'])
    return redirect("/one/select.html/?select_receive_people={}".format(current_user))


def delete(request):
    delete_ids = request.GET['delete_ids']
    ids = delete_ids.split('_')
    ids.pop(len(ids) - 1)  # 去除最后的空串
    for delete_id in ids:
        Pub.delete_db(PartTable, delete_id)
    return redirect("/one/select.html/")


def select_for_update(request):  # 为了修改查询数据
    data_dict = dict()
    update_id = request.GET['update_id']
    names = ['sn', 'qrcode', 'pn', 'part_name', 'car_type', 'producer', 'receive_date', 'batch',
             'send_people', 'contact',
             'use', 'receive_people', 'deal_mode', 'deal_remark',
             'deal_date', 'deal_count']
    data = Pub.select_db_one(PartTable, update_id, names)
    for index, column_name in enumerate(names):
        data_dict['src_update_{}'.format(column_name)] = data[index]
    return HttpResponse(json.dumps(data_dict), content_type="application/json")


def scrap(request):
    current_user = request.POST['baofei_curretn_user']
    scrap_sns = request.POST.get('scrap_sn', '')
    ids = scrap_sns.split('_')
    if '' not in ids:
        Pub.update_db1(PartTable, ids[0].strip(),
                       deal_count='1',
                       deal_mode=request.POST['scrap_deal_mode'],
                       deal_remark=request.POST['scrap_deal_remark'],
                       deal_date=request.POST['scrap_deal_date'],
                       )
    else:
        ids.pop(len(ids) - 1)
        for baofei_id in ids:
            Pub.update_db(PartTable, baofei_id,
                          deal_count='1',
                          deal_mode=request.POST['scrap_deal_mode'],
                          deal_remark=request.POST['scrap_deal_remark'],
                          deal_date=request.POST['scrap_deal_date'],
                          )

    return redirect("/one/select.html/?select_receive_people={}".format(current_user))


def barcode(request):
    code = request.POST.get('code', '----')
    code_just = code.rjust(4, '0')
    code_data = code_just
    bar = BarCode()
    folder = '/one/barcode_{}.png'.format(Pub.get_time())
    save_path = Pub.EXPORT_FOLDER + folder
    file = Pub.STATIC_EXPORT_FOLDER + folder
    bar.generate(code_data, save_path)
    return HttpResponse(json.dumps(file), content_type="application/json")


def max_barcode(request):
    file = ''
    return HttpResponse(json.dumps(file), content_type="application/json")


# 自动填充
def select_for_auto_input(request):
    data_dict = dict()
    add_pn = Pub.request_data(request, 'POST', 'add_pn', '')
    data = DB.select_for_auto_input(add_pn, COLUMN_NAMES)
    for index, column_name in enumerate(COLUMN_NAMES):
        data_dict['src_add_{}'.format(column_name)] = data[index]
    return HttpResponse(json.dumps(data_dict), content_type="application/json")


def baofei_html(request):
    data_dict = dict()

    # 查询下拉框
    pn = Pub.select_column(PartTable, 'pn')
    part_name = Pub.select_column(PartTable, 'part_name')
    car_type = Pub.select_column(PartTable, 'car_type')
    producer = Pub.select_column(PartTable, 'producer')
    receive_people = Pub.select_column(PartTable, 'receive_people')
    deal_mode = Pub.select_column(PartTable, 'deal_mode')
    use = Pub.select_column(PartTable, 'use')

    data_dict['pn'] = pn
    data_dict['part_name'] = part_name
    data_dict['car_type'] = car_type
    data_dict['producer'] = producer
    data_dict['receive_people'] = receive_people
    data_dict['deal_mode'] = deal_mode
    data_dict['use'] = use

    # 前端数据
    select_pn = Pub.request_data(request, 'GET', 'select_pn', '')
    select_part_name = Pub.request_data(request, 'GET', 'select_part_name', '')
    select_car_type = Pub.request_data(request, 'GET', 'select_car_type', '')
    select_use = Pub.request_data(request, 'GET', 'select_use', '')
    select_receive_date = Pub.request_data(request, 'GET', 'select_receive_date', '')
    select_deal_date = Pub.request_data(request, 'GET', 'select_deal_date', '')
    select_receive_people = Pub.request_data(request, 'GET', 'select_receive_people', '')
    select_deal_mode = Pub.request_data(request, 'GET', 'select_deal_mode', '')

    data_dict['select_pn'] = select_pn
    data_dict['select_part_name'] = select_part_name
    data_dict['select_car_type'] = select_car_type
    data_dict['select_use'] = select_use
    data_dict['select_receive_date'] = select_receive_date
    data_dict['select_deal_date'] = select_deal_date
    data_dict['select_receive_people'] = select_receive_people
    data_dict['select_deal_mode'] = select_deal_mode

    # 分页
    pagesize = int(Pub.request_data(request, 'GET', 'pagesize', Pub.PAGESIZE))
    data_dict['pagesize'] = pagesize
    current_page = int(Pub.request_data(request, 'GET', 'current_page', Pub.CURRENT_PAGE))
    data_dict['current_page'] = current_page

    # 按条件查询
    q1 = Q()
    q1.connector = 'AND'
    if select_pn != '':
        q1.children.append(('pn', select_pn))
    if select_part_name != '':
        q1.children.append(('part_name', select_part_name))
    if select_car_type != '':
        q1.children.append(('car_type', select_car_type))
    if select_use != '':
        q1.children.append(('use', select_use))
    if select_receive_date != '':
        q1.children.append(('receive_date', select_receive_date))
    if select_deal_date != '':
        q1.children.append(('deal_date', select_deal_date))
    if select_receive_people != '':
        q1.children.append(('receive_people', select_receive_people))

    q2 = Q()
    q2.connector = 'OR'
    if select_deal_mode == '':
        q2.children.append(('deal_mode', '取走'))
        q2.children.append(('deal_mode', '报废'))
    else:
        q2.children.append(('deal_mode', select_deal_mode))

    q = Q()
    q.add(q1, 'AND')
    q.add(q2, 'AND')

    filter_data = []
    db_data = PartTable.objects.filter(q)
    names = ['sn', 'qrcode', 'pn', 'part_name', 'car_type', 'producer', 'receive_date', 'batch',
             'send_people', 'contact',
             'use', 'receive_people', 'deal_mode', 'deal_remark',
             'deal_date', ]
    for data in db_data:
        one_data = list()
        for column_name in names:
            one_data.append(data.__dict__[column_name])
        filter_data.append(one_data)

    # 分页
    paginator = Paginator(filter_data, pagesize)
    last_page = paginator.num_pages
    data_dict['last_page'] = last_page
    if current_page > last_page:  # 当前页大于总分页默认最后一页
        current_page = last_page
    try:
        show_data = paginator.page(current_page)
    except Exception as e:
        show_data = paginator.page(1)

    # 前一页
    if current_page - 1 > 0:
        previous_page = current_page - 1
    else:
        previous_page = 1
    data_dict['previous_page'] = previous_page

    # 后一页
    if current_page + 1 < last_page:
        next_page = current_page + 1
    else:
        next_page = last_page
    data_dict['next_page'] = next_page

    data_dict['data'] = show_data.object_list
    count = len(filter_data)  # 数据总条数
    data_dict['count'] = count

    # 报废清单
    baofei_data = []
    baofei_names = ['qrcode', 'pn', 'part_name', 'use', 'deal_date', 'receive_people']
    for data in db_data:
        one_data = list()
        for column_name in baofei_names:
            one_data.append(data.__dict__[column_name])
        baofei_data.append(one_data)
    folder = '/one/data_list{}.xls'.format(Pub.get_time())
    save_path = Pub.EXPORT_FOLDER + folder
    scrap_file = Pub.STATIC_EXPORT_FOLDER + folder
    data_dict['scrap_file'] = scrap_file
    write_data = baofei_data
    print(len(write_data))
    new = scarp_data(write_data)
    print(len(new))
    source_file = os.path.join(Pub.EXPORT_TEMPLATE_FOLDER, u'baofei_export.xls')
    Pub.append_xls(source_file, save_path, new)

    return render(request, 'one/baofei.html', data_dict)
