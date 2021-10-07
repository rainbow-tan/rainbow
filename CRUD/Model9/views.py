# -*- encoding=utf-8 -*-
import os

from django.shortcuts import redirect
from django.shortcuts import render

from CRUD import Pub
from CRUD import database
from Model.models import Field1Table
from Model.models import Field23Table
from Model.models import Field3Table
from Model2.models import Field37Table
from Model8.models import QuDuanTable
from Model9 import business
from Model9 import db

COLUMN_NAMES = ['auto_id', 'xianbie',
                'chezhan',
                'quduan',
                'zaiping',
                'dianrongshuliang',
                'hangbie',
                'quduanchangdu', ]


def select_html(request):
    data_dict = dict()

    # 查询下拉框
    data_dict['xianbies'] = Pub.select_column(Field1Table, 'field1')
    data_dict['chezhans'] = Pub.select_column(Field3Table, 'field1')
    data_dict['zaipings'] = Pub.select_column(Field37Table, 'field1')
    data_dict['hangbies'] = Pub.select_column(Field23Table, 'field1')

    # 获取前端数据
    xianbie = Pub.request_data(request, 'GET', 'xianbie', '')
    chezhan = Pub.request_data(request, 'GET', 'chezhan', '')
    quduan = Pub.request_data(request, 'GET', 'quduan', '')
    zaiping = Pub.request_data(request, 'GET', 'zaiping', '')
    dianrongshuliang = Pub.request_data(request, 'GET', 'dianrongshuliang', '')
    hangbie = Pub.request_data(request, 'GET', 'hangbie', '')
    quduanchangdu = Pub.request_data(request, 'GET', 'quduanchangdu', '')
    pagesize = int(Pub.request_data(request, 'GET', 'pagesize', Pub.PAGESIZE))
    current_page = int(Pub.request_data(request, 'GET', 'current_page', Pub.CURRENT_PAGE))

    data_dict['xianbie'] = xianbie
    data_dict['chezhan'] = chezhan
    data_dict['quduan'] = quduan
    data_dict['zaiping'] = zaiping
    data_dict['dianrongshuliang'] = dianrongshuliang
    data_dict['hangbie'] = hangbie
    data_dict['quduanchangdu'] = quduanchangdu

    # 查询
    all_data = db.select(xianbie, chezhan, quduan, zaiping, dianrongshuliang, hangbie,
                         quduanchangdu, COLUMN_NAMES)

    database.paging(all_data, pagesize, current_page, data_dict)  # 分页
    database.export(all_data, data_dict, u'区段名称导出模板.xls', '9')  # 导出
    return render(request, 'Model9/select.html', data_dict)


def add_html(request):
    data_dict = dict()
    # 查询下拉框
    data_dict['xianbies'] = Pub.select_column(Field1Table, 'field1')
    data_dict['chezhans'] = Pub.select_column(Field3Table, 'field1')
    data_dict['zaipings'] = Pub.select_column(Field37Table, 'field1')
    data_dict['hangbies'] = Pub.select_column(Field23Table, 'field1')
    return render(request, 'Model9/add.html', data_dict)


def add(request):
    Pub.insert_db(QuDuanTable,
                  xianbie=request.POST['xianbie'],
                  chezhan=request.POST['chezhan'],
                  quduan=request.POST['quduan'],
                  zaiping=request.POST['zaiping'],
                  dianrongshuliang=request.POST['dianrongshuliang'],
                  hangbie=request.POST['hangbie'],
                  quduanchangdu=request.POST['quduanchangdu'],
                  )
    return redirect("/Model9/select.html/")


def update_html(request):
    update_id = request.GET['update_id']
    data_dict = dict()

    # 查询下拉框
    data_dict['xianbies'] = Pub.select_column(Field1Table, 'field1')
    data_dict['chezhans'] = Pub.select_column(Field3Table, 'field1')
    data_dict['zaipings'] = Pub.select_column(Field37Table, 'field1')
    data_dict['hangbies'] = Pub.select_column(Field23Table, 'field1')

    obj = QuDuanTable.objects.get(auto_id=update_id)
    data_dict['auto_id'] = obj.auto_id
    data_dict['xianbie'] = obj.xianbie
    data_dict['chezhan'] = obj.chezhan
    data_dict['quduan'] = obj.quduan
    data_dict['zaiping'] = obj.zaiping
    data_dict['dianrongshuliang'] = obj.dianrongshuliang
    data_dict['hangbie'] = obj.hangbie
    data_dict['quduanchangdu'] = obj.quduanchangdu

    return render(request, 'Model9/update.html', data_dict)


def update(request):
    Pub.update_db(QuDuanTable, request.POST['auto_id'],
                  xianbie=request.POST['xianbie'],
                  chezhan=request.POST['chezhan'],
                  quduan=request.POST['quduan'],
                  zaiping=request.POST['zaiping'],
                  dianrongshuliang=request.POST['dianrongshuliang'],
                  hangbie=request.POST['hangbie'],
                  quduanchangdu=request.POST['quduanchangdu'],
                  )
    # 更新对应的表
    db.update_others(xianbie=request.POST['xianbie'],
                     chezhan=request.POST['chezhan'],
                     quduan=request.POST['quduan'],
                     zaiping=request.POST['zaiping'],
                     dianrongshuliang=request.POST['dianrongshuliang'],
                     hangbie=request.POST['hangbie'],
                     quduanchangdu=request.POST['quduanchangdu'])
    return redirect("/Model9/select.html/")


def delete(request):
    delete_ids = request.GET['delete_ids']
    ids = delete_ids.split('_')
    ids.pop(-1)  # 去除最后的空串
    for delete_id in ids:
        Pub.delete_db(QuDuanTable, delete_id)
    return redirect("/Model9/select.html/")


def check_data(request):
    data_dict = dict()
    file_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = os.path.join(Pub.IMPORT_FOLDER,
                                'Model9_check_data_{}.xls'.format(Pub.get_time()))
        Pub.save_file(filename, file)
        try:
            file_data = Pub.read_xls(filename, 2)
            can_import, message = business.deal_xls_data(file_data)
            data_dict['success'] = '查看成功'
        except Exception as e:
            data_dict['success'] = '查看失败->{}'.format(e)
    data_dict['data'] = file_data
    return render(request, 'Model9/import.html', data_dict)


def import_html(request):
    return render(request, 'Model9/import.html')


def import_data(request):
    data_dict = dict()
    file_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = os.path.join(Pub.IMPORT_FOLDER, 'Model9', 'import_{}.xls'.format(Pub.get_time()))
        Pub.save_file(filename, file)
        try:
            file_data = Pub.read_xls(filename, 2)
            can_import, message = business.deal_xls_data(file_data)
            if can_import:
                for row_data in file_data:
                    Pub.insert_db(QuDuanTable,
                                  xianbie=row_data[1],
                                  chezhan=row_data[2],
                                  quduan=row_data[3],
                                  zaiping=row_data[4],
                                  dianrongshuliang=row_data[5],
                                  hangbie=row_data[6],
                                  quduanchangdu=row_data[7],
                                  )
                data_dict['success'] = '导入成功'
            else:
                data_dict['success'] = '导入失败->{}'.format(message)
        except Exception as e:
            data_dict['success'] = '导入失败->{}'.format(e)
    data_dict['data'] = file_data
    return render(request, 'Model9/import.html', data_dict)
