# -*- encoding=utf-8 -*-
import json
import os

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from CRUD import Pub
from CRUD import database
from Model.models import Field1Table
from Model.models import Field2Table
from Model7 import business
from Model7 import db
from Model7.models import ChangJia
from Model7.models import DangqianZhuangtai
from Model7.models import DataTable
from Model7.models import DiDian
from Model7.models import JiandingZhouqi
from Model7.models import JiliangQiju
import Model3.Business as Business
COLUMN_NAMES = ['auto_id', 'xianbie', 'chejian', 'didian', 'zongcheng', 'mingcheng', 'bianhao',
                'guige', 'dengji',
                'fanwei', 'changjia', 'zhuanye', 'fuzeren', 'riqi', 'xiaciriqi', 'zhouqi',
                'dangqianzhuangtai',
                'yibiaozhuangtai', 'beizhu', ]


def select_html(request):
    data_dict = dict()

    # 查询下拉框
    data_dict['xianbies'] = Pub.select_column(Field1Table, 'field1')
    data_dict['chejians'] = Pub.select_column(Field2Table, 'field1')
    data_dict['zongchengs'] = Pub.select_column(JiliangQiju, 'zongcheng')
    data_dict['zhouqis'] = Pub.select_column(JiandingZhouqi, 'zhouqi')
    data_dict['didians'] = Pub.select_column(DiDian, 'didian')
    data_dict['dangqianzhuangtais'] = Pub.select_column(DangqianZhuangtai, 'dangqianzhuangtai')
    data_dict['changjias'] = Pub.select_column(ChangJia, 'changjia')

    # 获取前端数据
    xianbie = Pub.request_data(request, 'GET', 'xianbie', '')
    chejian = Pub.request_data(request, 'GET', 'chejian', '')
    didian = Pub.request_data(request, 'GET', 'didian', '')
    zongcheng = Pub.request_data(request, 'GET', 'zongcheng', '')
    mingcheng = Pub.request_data(request, 'GET', 'mingcheng', '')
    bianhao = Pub.request_data(request, 'GET', 'bianhao', '')
    guige = Pub.request_data(request, 'GET', 'guige', '')
    dengji = Pub.request_data(request, 'GET', 'dengji', '')
    fanwei = Pub.request_data(request, 'GET', 'fanwei', '')
    changjia = Pub.request_data(request, 'GET', 'changjia', '')
    zhuanye = Pub.request_data(request, 'GET', 'zhuanye', '')
    fuzeren = Pub.request_data(request, 'GET', 'fuzeren', '')
    riqi = Pub.request_data(request, 'GET', 'riqi', '')
    xiaciriqi = Pub.request_data(request, 'GET', 'xiaciriqi', '')
    zhouqi = Pub.request_data(request, 'GET', 'zhouqi', '')
    dangqianzhuangtai = Pub.request_data(request, 'GET', 'dangqianzhuangtai', '')
    yibiaozhuangtai = Pub.request_data(request, 'GET', 'yibiaozhuangtai', '')
    beizhu = Pub.request_data(request, 'GET', 'beizhu', '')
    pagesize = int(Pub.request_data(request, 'GET', 'pagesize', Pub.PAGESIZE))
    current_page = int(Pub.request_data(request, 'GET', 'current_page', Pub.CURRENT_PAGE))

    data_dict['xianbie'] = xianbie
    data_dict['chejian'] = chejian
    data_dict['didian'] = didian
    data_dict['zongcheng'] = zongcheng
    data_dict['mingcheng'] = mingcheng
    data_dict['bianhao'] = bianhao
    data_dict['guige'] = guige
    data_dict['dengji'] = dengji
    data_dict['fanwei'] = fanwei
    data_dict['changjia'] = changjia
    data_dict['zhuanye'] = zhuanye
    data_dict['fuzeren'] = fuzeren
    data_dict['riqi'] = riqi
    data_dict['xiaciriqi'] = xiaciriqi
    data_dict['zhouqi'] = zhouqi
    data_dict['dangqianzhuangtai'] = dangqianzhuangtai
    data_dict['yibiaozhuangtai'] = yibiaozhuangtai
    data_dict['beizhu'] = beizhu

    # 查询
    all_data = db.select(xianbie, chejian, didian, zongcheng, mingcheng, bianhao, guige, dengji,
                         fanwei, changjia, zhuanye, fuzeren, riqi, xiaciriqi, zhouqi,
                         dangqianzhuangtai, yibiaozhuangtai, beizhu, COLUMN_NAMES)

    database.paging(all_data, pagesize, current_page, data_dict)  # 分页
    database.export(all_data, data_dict, u'仪器仪表台账列表导出模板.xls', '7')  # 导出
    return render(request, 'Model7/select.html', data_dict)


def add_html(request):
    data_dict = dict()
    # 查询下拉框
    data_dict['xianbies'] = Pub.select_column(Field1Table, 'field1')
    data_dict['chejians'] = Pub.select_column(Field2Table, 'field1')
    data_dict['zongchengs'] = Pub.select_column(JiliangQiju, 'zongcheng')
    data_dict['zhouqis'] = Pub.select_column(JiandingZhouqi, 'zhouqi')
    data_dict['didians'] = Pub.select_column(DiDian, 'didian')
    data_dict['dangqianzhuangtais'] = Pub.select_column(DangqianZhuangtai, 'dangqianzhuangtai')
    data_dict['changjias'] = Pub.select_column(ChangJia, 'changjia')
    return render(request, 'Model7/add.html', data_dict)


def add(request):
    Pub.insert_db(DataTable,
                  xianbie=request.POST['xianbie'],
                  chejian=request.POST['chejian'],
                  didian=request.POST['didian'],
                  zongcheng=request.POST['zongcheng'],
                  mingcheng=request.POST['mingcheng'],
                  bianhao=request.POST['bianhao'],
                  guige=request.POST['guige'],
                  dengji=request.POST['dengji'],
                  fanwei=request.POST['fanwei'],
                  changjia=request.POST['changjia'],
                  zhuanye=request.POST['zhuanye'],
                  fuzeren=request.POST['fuzeren'],
                  riqi=request.POST['riqi'],
                  xiaciriqi=request.POST['xiaciriqi'],
                  zhouqi=request.POST['zhouqi'],
                  dangqianzhuangtai=request.POST['dangqianzhuangtai'],
                  yibiaozhuangtai=request.POST['yibiaozhuangtai'],
                  beizhu=request.POST['beizhu'],
                  )
    return redirect("/Model7/select.html/")


def update_html(request):
    update_id = request.GET['update_id']
    data_dict = dict()

    # 查询下拉框
    data_dict['xianbies'] = Pub.select_column(Field1Table, 'field1')
    data_dict['chejians'] = Pub.select_column(Field2Table, 'field1')
    data_dict['zongchengs'] = Pub.select_column(JiliangQiju, 'zongcheng')
    data_dict['zhouqis'] = Pub.select_column(JiandingZhouqi, 'zhouqi')
    data_dict['didians'] = Pub.select_column(DiDian, 'didian')
    data_dict['dangqianzhuangtais'] = Pub.select_column(DangqianZhuangtai, 'dangqianzhuangtai')
    data_dict['changjias'] = Pub.select_column(ChangJia, 'changjia')

    obj = DataTable.objects.get(auto_id=update_id)
    data_dict['auto_id'] = obj.auto_id
    data_dict['xianbie'] = obj.xianbie
    data_dict['chejian'] = obj.chejian
    data_dict['didian'] = obj.didian
    data_dict['zongcheng'] = obj.zongcheng
    data_dict['mingcheng'] = obj.mingcheng
    data_dict['bianhao'] = obj.bianhao
    data_dict['guige'] = obj.guige
    data_dict['dengji'] = obj.dengji
    data_dict['fanwei'] = obj.fanwei
    data_dict['changjia'] = obj.changjia
    data_dict['zhuanye'] = obj.zhuanye
    data_dict['fuzeren'] = obj.fuzeren
    data_dict['riqi'] = obj.riqi
    data_dict['xiaciriqi'] = obj.xiaciriqi
    data_dict['zhouqi'] = obj.zhouqi
    data_dict['dangqianzhuangtai'] = obj.dangqianzhuangtai
    data_dict['yibiaozhuangtai'] = obj.yibiaozhuangtai
    data_dict['beizhu'] = obj.beizhu
    return render(request, 'Model7/update.html', data_dict)


def update(request):
    Pub.update_db(DataTable, request.POST['auto_id'],
                  xianbie=request.POST['xianbie'],
                  chejian=request.POST['chejian'],
                  didian=request.POST['didian'],
                  zongcheng=request.POST['zongcheng'],
                  mingcheng=request.POST['mingcheng'],
                  bianhao=request.POST['bianhao'],
                  guige=request.POST['guige'],
                  dengji=request.POST['dengji'],
                  fanwei=request.POST['fanwei'],
                  changjia=request.POST['changjia'],
                  zhuanye=request.POST['zhuanye'],
                  fuzeren=request.POST['fuzeren'],
                  riqi=request.POST['riqi'],
                  xiaciriqi=request.POST['xiaciriqi'],
                  zhouqi=request.POST['zhouqi'],
                  dangqianzhuangtai=request.POST['dangqianzhuangtai'],
                  yibiaozhuangtai=request.POST['yibiaozhuangtai'],
                  beizhu=request.POST['beizhu'],
                  )
    return redirect("/Model7/select.html/")


def delete(request):
    delete_ids = request.GET['delete_ids']
    ids = delete_ids.split('_')
    ids.pop(-1)  # 去除最后的空串
    for delete_id in ids:
        Pub.delete_db(DataTable, delete_id)
    return redirect("/Model7/select.html/")


def set_dangqianzhuangtai(request):
    auto_id = request.GET['auto_id']
    state = request.GET['state']
    obj = DataTable.objects.get(auto_id=auto_id)
    obj.dangqianzhuangtai = state
    obj.save()
    return HttpResponse(json.dumps({}), content_type="application/json")


def check_data(request):
    data_dict = dict()
    file_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = os.path.join(Pub.IMPORT_FOLDER, 'Model7SeeData{}.xls'.format(Pub.get_time()))
        Pub.save_file(filename, file)
        try:
            file_data = business.read_xls(filename, 3)
            can_import, message = business.deal_xls_data(file_data)
            data_dict['success'] = '查看成功'
        except Exception as e:
            data_dict['success'] = '查看失败->{}'.format(e)
    data_dict['data'] = file_data
    return render(request, 'Model7/import.html', data_dict)


def import_html(request):
    return render(request, 'Model7/import.html')


def import_data(request):
    data_dict = dict()
    file_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = os.path.join(Pub.IMPORT_FOLDER, 'Model7', 'import_{}.xls'.format(Pub.get_time()))
        Pub.save_file(filename, file)
        try:
            file_data = business.read_xls(filename, 3)
            can_import, message = business.deal_xls_data(file_data)
            if can_import:
                for row_data in file_data:
                    Pub.insert_db(DataTable,
                                  xianbie=row_data[1],
                                  chejian=row_data[2],
                                  didian=row_data[3],
                                  zongcheng=row_data[4],
                                  mingcheng=row_data[5],
                                  bianhao=row_data[6],
                                  guige=row_data[7],
                                  dengji=row_data[8],
                                  fanwei=row_data[9],
                                  changjia=row_data[10],
                                  zhuanye=row_data[11],
                                  fuzeren=row_data[12],
                                  riqi=row_data[13],
                                  xiaciriqi=row_data[14],
                                  zhouqi=row_data[15],
                                  dangqianzhuangtai=row_data[16],
                                  yibiaozhuangtai=row_data[17],
                                  beizhu=row_data[18],
                                  )
                data_dict['success'] = '导入成功'
            else:
                data_dict['success'] = '导入失败->{}'.format(message)
        except Exception as e:
            data_dict['success'] = '导入失败->{}'.format(e)
    data_dict['data'] = file_data
    return render(request, 'Model7/import.html', data_dict)


