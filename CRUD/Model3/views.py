# -*- encoding=utf-8 -*-
import json
import os
import time

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from CRUD import Pub
from CRUD import Tool
from CRUD import database
from CRUD.settings import BASE_DIR
from Model.models import Field1Table
from Model.models import Field23Table
from Model.models import Field24Table
from Model.models import Field2Table
from Model.models import Field3Table
from Model2.models import Field37Table
from Model3 import Business
from Model3 import DB
from Model3.models import DataTable
from Model3.models import Field71Table

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

    database.paging(remove_sort_data, pagesize, current_page, data_dict)  # 分页
    database.export(sort_data, data_dict, u'ZPW导出模板.xls', '3')  # 导出

    return render(request, 'Model3/select.html', data_dict)


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
    return redirect("/Model3/select.html/")


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
    return redirect("/Model3/select.html/")


def delete(request):
    delete_ids = request.GET['delete_ids']
    ids = delete_ids.split('_')
    ids.pop(len(ids) - 1)  # 去除最后的空串
    for delete_id in ids:
        Pub.delete_db(DataTable, delete_id)
    return redirect("/Model3/select.html/")


def import_html(request):
    return render(request, 'Model3/import.html')


def import_data(request):  # 导入
    data_dict = dict()
    sorted_data = []
    file_string = 'file'
    if file_string in request.FILES:
        file = request.FILES[file_string]
        # filename = BASE_DIR + '/templates/files/import/data_three_{}.xls'.format(
        #     time.strftime("%Y%m%d%H%M%S", time.localtime()))
        now = Tool.now()
        # filename = os.path.join(BASE_DIR, 'templates/files/import/data_three_{}.xls'.format(now))
        filename = os.path.join(Pub.IMPORT_FOLDER, 'Model3', 'import_{}.xls'.format(now))
        Pub.save_file(filename, file)
        try:
            file_data = Business.read_xls(filename, 5)
            calculate_data = Business.all_row(file_data)
            ret, msg = Business.can_import(calculate_data)
            if ret is True:
                sorted_data = Business.sort_data(calculate_data)
                pop_data = Pub.pop_first(sorted_data)
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
                                  field84=one_data[36],  # 补偿连接线
                                  field63=one_data[37],
                                  field64=one_data[38],
                                  field65=one_data[39],
                                  field66=one_data[40],
                                  field67=one_data[41],
                                  field68=one_data[42],
                                  field69=one_data[43],
                                  )
                data_dict['success'] = '导入成功'
            else:
                data_dict['success'] = '导入结果:导入失败\n原因:{}'.format(msg)
        except Exception as e:
            data_dict['success'] = '导入失败->{}'.format(e)
    data_dict['data'] = sorted_data
    return render(request, 'Model3/import.html', data_dict)


def check_data(request):
    data_dict = dict()
    calculate_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = BASE_DIR + '/templates/files/import/data_two_{}.xls'.format(
            time.strftime("%Y%m%d%H%M%S", time.localtime()))
        Pub.save_file(filename, file)
        try:
            file_data = Business.read_xls(filename, 5)
            sorted_data = Business.sort_data(file_data)
            calculate_data = Business.all_row(sorted_data)
            data_dict['success'] = '查看成功'
        except Exception as e:
            data_dict['success'] = '查看失败'
    data_dict['data'] = calculate_data
    return render(request, 'Model3/import.html', data_dict)


def select_changdu_by_guidao(request):
    data_dict = dict()
    guidaoleixing = request.GET['guidaoleixing']
    data_dict['value'] = DB.select_changdu_by_guidao(guidaoleixing)
    return HttpResponse(json.dumps(data_dict), content_type="application/json")


def gcdpldfx(request):
    """
    功出电平等级求封线
    :param request:
    :return:
    """
    value = request.GET['value']
    ret = Business.gongchu_lilundengji_fengxian.get(value, '')
    data = dict(ret=ret)
    return HttpResponse(json.dumps(data), content_type="application/json")


def gcdpfxld(request):
    """
    功出电平封线求等级
    :param request:
    :return:
    """
    value = request.GET['value']
    value = value.replace('，', ',')
    ret = Business.get_key_by_value(Business.gongchu_lilundengji_fengxian, value)
    data = dict(value=value, ret=ret)
    return HttpResponse(json.dumps(data), content_type="application/json")


def jsdpldfx(request):
    """
    接收电平等级求封线
    :param request:
    :return:
    """
    value = request.GET['value']
    ret = Business.jieshou_lilundengji_fengxian.get(value, '')
    ret = Business.jieshou_lilundengji_fengxian.get(value, '')
    data = dict(ret=ret)
    return HttpResponse(json.dumps(data), content_type="application/json")


def jsdpfxld(request):
    """
    接收电平封线求等级
    :param request:
    :return:
    """
    value = request.GET['value']
    value = value.replace('，', ',')
    ret = Business.get_key_by_value(Business.jieshou_lilundengji_fengxian, value)
    data = dict(value=value, ret=ret)
    return HttpResponse(json.dumps(data), content_type="application/json")


def network_length_7(request):
    """
    当电缆规定总长度为7.5时
    发送模拟电缆电缆长度=>发送模拟电缆模拟固定长度
    接收模拟电缆电缆长度=>接收模拟电缆模拟固定长度
    """
    dianlanchangdu = request.GET['dianlanchangdu']
    data = {}
    ret = Business.network_length_7(dianlanchangdu)
    data['gudingchangdu'] = ret
    return HttpResponse(json.dumps(data), content_type="application/json")
def reality_length_7(request):
    """
    当电缆规定总长度为7.5时
    发送模拟电缆电缆长度=>发送模拟电缆实际电缆长度档位
    接收模拟电缆电缆长度=>接收模拟电缆实际电缆长度档位
    """
    data = {}
    dianlanchangdu = request.GET['dianlanchangdu']
    dangwei = Business.reality_length_7(dianlanchangdu)
    data['dangwei'] = dangwei
    return HttpResponse(json.dumps(data), content_type="application/json")
def compensation_7(request):
    """
    当电缆规定总长度为7.5时
    发送模拟电缆电缆长度=>发送模拟电缆补偿连接线
    接收模拟电缆电缆长度=>接收模拟电缆补偿连接线
    """
    data = {}
    dianlanchangdu = request.GET['dianlanchangdu']
    dangwei = Business.compensation_7(dianlanchangdu)
    data['buchang'] = dangwei
    return HttpResponse(json.dumps(data), content_type="application/json")


def network_length_10(request):
    """
    当电缆规定总长度为10时
    发送模拟电缆电缆长度=>发送模拟电缆模拟固定长度
    接收模拟电缆电缆长度=>接收模拟电缆模拟固定长度
    """
    dianlanchangdu = request.GET['dianlanchangdu']
    data = {}
    ret = Business.network_length_10(dianlanchangdu)
    data['gudingchangdu'] = ret
    return HttpResponse(json.dumps(data), content_type="application/json")
def reality_length_10(request):
    """
    当电缆规定总长度为10时
    发送模拟电缆电缆长度=>发送模拟电缆实际电缆长度档位
    接收模拟电缆电缆长度=>接收模拟电缆实际电缆长度档位
    """
    data = {}
    dianlanchangdu = request.GET['dianlanchangdu']
    dangwei = Business.reality_length_10(dianlanchangdu)
    data['dangwei'] = dangwei
    return HttpResponse(json.dumps(data), content_type="application/json")
def compensation_10(request):
    """
    当电缆规定总长度为10时
    发送模拟电缆电缆长度=>发送模拟电缆补偿连接线
    接收模拟电缆电缆长度=>接收模拟电缆补偿连接线
    """
    data = {}
    dianlanchangdu = request.GET['dianlanchangdu']
    dangwei = Business.compensation_10(dianlanchangdu)
    data['buchang'] = dangwei
    return HttpResponse(json.dumps(data), content_type="application/json")