# -*- encoding=utf-8 -*-
import json
import os

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from CRUD import Pub
from CRUD import database
from Model.models import Field1Table
from Model.models import Field23Table
from Model.models import Field2Table
from Model.models import Field3Table
from Model2.models import Field37Table
from Model7.models import ChangJia
from Model7.models import JiandingZhouqi
from Model8 import business
from Model8 import db
from Model8.models import DataTable

COLUMN_NAMES = ['auto_id',
                'wentiriqi',
                'xianbie',
                'chejian',
                'chezhan',
                'quduan',
                'buliangdianrong',
                'hangbie',
                'dianrongshuliang',
                'zaiping',
                'chuliriqi',
                'yuanying',
                'chuliqingkuang',
                'shangbaoqingkuang',
                'zhouqi',
                'beizhu',
                'qiandianliu',
                'houdianliu',
                'qiandianya',
                'houdianya',
                'qiandianrong',
                'houdianrong',
                'changjia',
                'shiyongshijian',
                'fankuiren', ]


def select_html(request):
    data_dict = dict()

    # 查询下拉框
    data_dict['xianbies'] = Pub.select_column(Field1Table, 'field1')
    data_dict['chejians'] = Pub.select_column(Field2Table, 'field1')
    data_dict['chezhans'] = Pub.select_column(Field3Table, 'field1')
    data_dict['changjias'] = Pub.select_column(ChangJia, 'changjia')
    data_dict['hangbies'] = Pub.select_column(Field23Table, 'field1')
    data_dict['zaipings'] = Pub.select_column(Field37Table, 'field1')
    data_dict['zhouqis'] = Pub.select_column(JiandingZhouqi, 'zhouqi')

    # 获取前端数据
    auto_id = Pub.request_data(request, 'GET', 'auto_id', '')
    wentiriqi = Pub.request_data(request, 'GET', 'wentiriqi', '')
    xianbie = Pub.request_data(request, 'GET', 'xianbie', '')
    chejian = Pub.request_data(request, 'GET', 'chejian', '')
    chezhan = Pub.request_data(request, 'GET', 'chezhan', '')
    quduan = Pub.request_data(request, 'GET', 'quduan', '')
    buliangdianrong = Pub.request_data(request, 'GET', 'buliangdianrong', '')
    hangbie = Pub.request_data(request, 'GET', 'hangbie', '')
    dianrongshuliang = Pub.request_data(request, 'GET', 'dianrongshuliang', '')
    zaiping = Pub.request_data(request, 'GET', 'zaiping', '')
    chuliriqi = Pub.request_data(request, 'GET', 'chuliriqi', '')
    yuanying = Pub.request_data(request, 'GET', 'yuanying', '')
    chuliqingkuang = Pub.request_data(request, 'GET', 'chuliqingkuang', '')
    shangbaoqingkuang = Pub.request_data(request, 'GET', 'shangbaoqingkuang', '')
    zhouqi = Pub.request_data(request, 'GET', 'zhouqi', '')
    beizhu = Pub.request_data(request, 'GET', 'beizhu', '')
    qiandianliu = Pub.request_data(request, 'GET', 'qiandianliu', '')
    houdianliu = Pub.request_data(request, 'GET', 'houdianliu', '')
    qiandianya = Pub.request_data(request, 'GET', 'qiandianya', '')
    houdianya = Pub.request_data(request, 'GET', 'houdianya', '')
    qiandianrong = Pub.request_data(request, 'GET', 'qiandianrong', '')
    houdianrong = Pub.request_data(request, 'GET', 'houdianrong', '')
    changjia = Pub.request_data(request, 'GET', 'changjia', '')
    shiyongshijian = Pub.request_data(request, 'GET', 'shiyongshijian', '')
    fankuiren = Pub.request_data(request, 'GET', 'fankuiren', '')
    pagesize = int(Pub.request_data(request, 'GET', 'pagesize', Pub.PAGESIZE))
    current_page = int(Pub.request_data(request, 'GET', 'current_page', Pub.CURRENT_PAGE))

    data_dict['auto_id'] = auto_id
    data_dict['wentiriqi'] = wentiriqi
    data_dict['xianbie'] = xianbie
    data_dict['chejian'] = chejian
    data_dict['chezhan'] = chezhan
    data_dict['quduan'] = quduan
    data_dict['buliangdianrong'] = buliangdianrong
    data_dict['hangbie'] = hangbie
    data_dict['dianrongshuliang'] = dianrongshuliang
    data_dict['zaiping'] = zaiping
    data_dict['chuliriqi'] = chuliriqi
    data_dict['yuanying'] = yuanying
    data_dict['chuliqingkuang'] = chuliqingkuang
    data_dict['shangbaoqingkuang'] = shangbaoqingkuang
    data_dict['zhouqi'] = zhouqi
    data_dict['beizhu'] = beizhu
    data_dict['qiandianliu'] = qiandianliu
    data_dict['houdianliu'] = houdianliu
    data_dict['qiandianya'] = qiandianya
    data_dict['houdianya'] = houdianya
    data_dict['qiandianrong'] = qiandianrong
    data_dict['houdianrong'] = houdianrong
    data_dict['changjia'] = changjia
    data_dict['shiyongshijian'] = shiyongshijian
    data_dict['fankuiren'] = fankuiren

    # 查询
    filter_data = db.select(wentiriqi, xianbie, chejian, chezhan, quduan, buliangdianrong,
                            hangbie, dianrongshuliang, zaiping, chuliriqi, yuanying,
                            chuliqingkuang, shangbaoqingkuang, zhouqi, beizhu, qiandianliu,
                            houdianliu, qiandianya, houdianya, qiandianrong, houdianrong,
                            changjia, shiyongshijian, fankuiren, COLUMN_NAMES)

    database.paging(filter_data, pagesize, current_page, data_dict)  # 分页
    database.export(filter_data, data_dict, u'高速综合检测车检测问题台账导出模板.xls', '8')  # 导出

    return render(request, 'Model8/select.html', data_dict)


def add_html(request):
    data_dict = dict()
    # 查询下拉框
    data_dict['xianbies'] = Pub.select_column(Field1Table, 'field1')
    data_dict['chejians'] = Pub.select_column(Field2Table, 'field1')
    data_dict['chezhans'] = Pub.select_column(Field3Table, 'field1')
    data_dict['changjias'] = Pub.select_column(ChangJia, 'changjia')
    data_dict['hangbies'] = Pub.select_column(Field23Table, 'field1')
    data_dict['zaipings'] = Pub.select_column(Field37Table, 'field1')
    data_dict['zhouqis'] = Pub.select_column(JiandingZhouqi, 'zhouqi')
    return render(request, 'Model8/add.html', data_dict)


def add(request):
    Pub.insert_db(DataTable,
                  wentiriqi=request.POST['wentiriqi'],
                  xianbie=request.POST['xianbie'],
                  chejian=request.POST['chejian'],
                  chezhan=request.POST['chezhan'],
                  quduan=request.POST['quduan'],
                  buliangdianrong=request.POST['buliangdianrong'],
                  hangbie=request.POST['hangbie'],
                  dianrongshuliang=request.POST['dianrongshuliang'],
                  zaiping=request.POST['zaiping'],
                  chuliriqi=request.POST['chuliriqi'],
                  yuanying=request.POST['yuanying'],
                  chuliqingkuang=request.POST['chuliqingkuang'],
                  shangbaoqingkuang=request.POST['shangbaoqingkuang'],
                  zhouqi=request.POST['zhouqi'],
                  beizhu=request.POST['beizhu'],
                  qiandianliu=request.POST['qiandianliu'],
                  houdianliu=request.POST['houdianliu'],
                  qiandianya=request.POST['qiandianya'],
                  houdianya=request.POST['houdianya'],
                  qiandianrong=request.POST['qiandianrong'],
                  houdianrong=request.POST['houdianrong'],
                  changjia=request.POST['changjia'],
                  shiyongshijian=request.POST['shiyongshijian'],
                  fankuiren=request.POST['fankuiren'],
                  )
    return redirect("/Model8/select.html/")


def update_html(request):
    update_id = request.GET['update_id']
    data_dict = dict()
    # 查询下拉框
    data_dict['xianbies'] = Pub.select_column(Field1Table, 'field1')
    data_dict['chejians'] = Pub.select_column(Field2Table, 'field1')
    data_dict['chezhans'] = Pub.select_column(Field3Table, 'field1')
    data_dict['changjias'] = Pub.select_column(ChangJia, 'changjia')
    data_dict['hangbies'] = Pub.select_column(Field23Table, 'field1')
    data_dict['zaipings'] = Pub.select_column(Field37Table, 'field1')
    data_dict['zhouqis'] = Pub.select_column(JiandingZhouqi, 'zhouqi')

    obj = DataTable.objects.get(auto_id=update_id)
    data_dict['auto_id'] = obj.auto_id
    data_dict['wentiriqi'] = obj.wentiriqi
    data_dict['xianbie'] = obj.xianbie
    data_dict['chejian'] = obj.chejian
    data_dict['chezhan'] = obj.chezhan
    data_dict['quduan'] = obj.quduan
    data_dict['buliangdianrong'] = obj.buliangdianrong
    data_dict['hangbie'] = obj.hangbie
    data_dict['dianrongshuliang'] = obj.dianrongshuliang
    data_dict['zaiping'] = obj.zaiping
    data_dict['chuliriqi'] = obj.chuliriqi
    data_dict['yuanying'] = obj.yuanying
    data_dict['chuliqingkuang'] = obj.chuliqingkuang
    data_dict['shangbaoqingkuang'] = obj.shangbaoqingkuang
    data_dict['zhouqi'] = obj.zhouqi
    data_dict['beizhu'] = obj.beizhu
    data_dict['qiandianliu'] = obj.qiandianliu
    data_dict['houdianliu'] = obj.houdianliu
    data_dict['qiandianya'] = obj.qiandianya
    data_dict['houdianya'] = obj.houdianya
    data_dict['qiandianrong'] = obj.qiandianrong
    data_dict['houdianrong'] = obj.houdianrong
    data_dict['changjia'] = obj.changjia
    data_dict['shiyongshijian'] = obj.shiyongshijian
    data_dict['fankuiren'] = obj.fankuiren
    return render(request, 'Model8/update.html', data_dict)


def update(request):
    Pub.update_db(DataTable, request.POST['auto_id'],
                  wentiriqi=request.POST['wentiriqi'],
                  xianbie=request.POST['xianbie'],
                  chejian=request.POST['chejian'],
                  chezhan=request.POST['chezhan'],
                  quduan=request.POST['quduan'],
                  buliangdianrong=request.POST['buliangdianrong'],
                  hangbie=request.POST['hangbie'],
                  dianrongshuliang=request.POST['dianrongshuliang'],
                  zaiping=request.POST['zaiping'],
                  chuliriqi=request.POST['chuliriqi'],
                  yuanying=request.POST['yuanying'],
                  chuliqingkuang=request.POST['chuliqingkuang'],
                  shangbaoqingkuang=request.POST['shangbaoqingkuang'],
                  zhouqi=request.POST['zhouqi'],
                  beizhu=request.POST['beizhu'],
                  qiandianliu=request.POST['qiandianliu'],
                  houdianliu=request.POST['houdianliu'],
                  qiandianya=request.POST['qiandianya'],
                  houdianya=request.POST['houdianya'],
                  qiandianrong=request.POST['qiandianrong'],
                  houdianrong=request.POST['houdianrong'],
                  changjia=request.POST['changjia'],
                  shiyongshijian=request.POST['shiyongshijian'],
                  fankuiren=request.POST['fankuiren'], )
    return redirect("/Model8/select.html/")


def delete(request):
    delete_ids = request.GET['delete_ids']
    ids = delete_ids.split('_')
    ids.pop(-1)  # 去除最后的空串
    for delete_id in ids:
        Pub.delete_db(DataTable, delete_id)
    return redirect("/Model8/select.html/")


# def search_chejian_by_xianbie(request):
#     xianbie = request.GET['xianbie']
#     chejians = database.select_chejian(xianbie)
#     data = {'chejians': chejians}
#     return HttpResponse(json.dumps(data), content_type="application/json")
#
#
# def search_chezhan_by_chejian(request):
#     chejian = request.GET['chejian']
#     chezhans = database.select_chezhan(chejian)
#     data = {'chezhans': chezhans}
#     return HttpResponse(json.dumps(data), content_type="application/json")


def search_fileds_by_quduan(request):
    xianbie = request.GET['xianbie']
    chezhan = request.GET['chezhan']
    quduan = request.GET['quduan']
    data = db.get_quduan_info(xianbie, chezhan, quduan)
    return HttpResponse(json.dumps(data), content_type="application/json")


def import_html(request):
    return render(request, 'Model8/import.html')


def check_data(request):
    data_dict = dict()
    file_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = os.path.join(Pub.IMPORT_FOLDER, 'Model8SeeData{}.xls'.format(Pub.get_time()))
        Pub.save_file(filename, file)
        try:
            file_data = business.read_xls(filename, 2)
            business.deal_xls(file_data)
            data_dict['success'] = '查看成功'
        except Exception as e:
            data_dict['success'] = '查看失败->{}'.format(e)
    data_dict['data'] = file_data
    return render(request, 'Model8/import.html', data_dict)


def import_data(request):
    data_dict = dict()
    file_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = os.path.join(Pub.IMPORT_FOLDER, 'Model8', 'import_{}.xls'.format(Pub.get_time()))
        Pub.save_file(filename, file)
        try:
            file_data = business.read_xls(filename, 2)
            business.deal_xls(file_data)
            for row_data in file_data:
                Pub.insert_db(DataTable,
                              wentiriqi=row_data[1],
                              xianbie=row_data[2],
                              chejian=row_data[3],
                              chezhan=row_data[4],
                              quduan=row_data[5],
                              buliangdianrong=row_data[6],
                              hangbie=row_data[7],
                              dianrongshuliang=row_data[8],
                              zaiping=row_data[9],
                              chuliriqi=row_data[10],
                              yuanying=row_data[11],
                              chuliqingkuang=row_data[12],
                              shangbaoqingkuang=row_data[13],
                              zhouqi=row_data[14],
                              beizhu=row_data[15],
                              qiandianliu=row_data[16],
                              houdianliu=row_data[17],
                              qiandianya=row_data[18],
                              houdianya=row_data[19],
                              qiandianrong=row_data[20],
                              houdianrong=row_data[21],
                              changjia=row_data[22],
                              shiyongshijian=row_data[23],
                              fankuiren=row_data[24],
                              )
            data_dict['success'] = '导入成功'
        except Exception as e:
            data_dict['success'] = '导入失败->{}'.format(e)
    data_dict['data'] = file_data
    return render(request, 'Model8/import.html', data_dict)
