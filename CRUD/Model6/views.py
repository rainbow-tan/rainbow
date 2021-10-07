# -*- encoding=utf-8 -*-
import datetime
import json
import os

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from CRUD import Pub
from CRUD import database
from CRUD.Pub import CURRENT_PAGE
from CRUD.Pub import PAGESIZE
from Model.models import Field2Table
from Model.models import Field3Table
from Model6 import XLS
from Model6 import business
from Model6 import db
from Model6.business import qiuhe
from Model6.models import Luruye
from Model6.models import ZhuYe
from Model7.models import XianbieChejianChenzhan

COLUMN_NAMES = ['auto_id', 'duanbie', 'xianbie', 'chejian', 'chezhan', 'genbanren', 'gongqu',
                'zuoyeren', 'renwuliang',
                'xiangmu', 'fenlei', 'yuefen', 'gongzuoneirong', 'zhouqi', 'neirongshuoming',
                'danwei',
                'wanchengshuliang', 'wanchengriqi', ]


def select_html(request):
    data_dict = dict()

    # 查询下拉框
    data_dict['xianbies'] = Pub.select_column(XianbieChejianChenzhan, 'xianbie')
    data_dict['chejians'] = Pub.select_column(Field2Table, 'field1')
    data_dict['chezhans'] = Pub.select_column(Field3Table, 'field1')
    data_dict['xiangmus'] = Pub.select_column(ZhuYe, 'xiangmu')
    data_dict['fenleis'] = Pub.select_column(ZhuYe, 'fenlei')

    # 前端数据
    duanbie = request.GET.get('duanbie', '')
    xianbie = request.GET.get('xianbie', '')
    chejian = request.GET.get('chejian', '')
    chezhan = request.GET.get('chezhan', '')
    genbanren = request.GET.get('genbanren', '')
    gongqu = request.GET.get('gongqu', '')
    zuoyeren = request.GET.get('zuoyeren', '')
    renwuliang = request.GET.get('renwuliang', '')
    xiangmu = request.GET.get('xiangmu', '')
    fenlei = request.GET.get('fenlei', '')
    yuefen = request.GET.get('yuefen', '')
    gongzuoneirong = request.GET.get('gongzuoneirong', '')
    zhouqi = request.GET.get('zhouqi', '')
    neirongshuoming = request.GET.get('neirongshuoming', '')
    danwei = request.GET.get('danwei', '')
    wanchengshuliang = request.GET.get('wanchengshuliang', '')
    starttime = request.GET.get('starttime', '')
    endtime = request.GET.get('endtime', '')
    pagesize = int(Pub.request_data(request, 'GET', 'pagesize', PAGESIZE))
    current_page = int(Pub.request_data(request, 'GET', 'current_page', CURRENT_PAGE))

    data_dict['duanbie'] = duanbie
    data_dict['xianbie'] = xianbie
    data_dict['chejian'] = chejian
    data_dict['chezhan'] = chezhan
    data_dict['genbanren'] = genbanren
    data_dict['gongqu'] = gongqu
    data_dict['zuoyeren'] = zuoyeren
    data_dict['renwuliang'] = renwuliang
    data_dict['xiangmu'] = xiangmu
    data_dict['fenlei'] = fenlei
    data_dict['yuefen'] = yuefen
    data_dict['gongzuoneirong'] = gongzuoneirong
    data_dict['zhouqi'] = zhouqi
    data_dict['neirongshuoming'] = neirongshuoming
    data_dict['danwei'] = danwei
    data_dict['wanchengshuliang'] = wanchengshuliang
    data_dict['starttime'] = starttime
    data_dict['endtime'] = endtime

    # 按条件查询
    all_data = db.select(duanbie, xianbie, chejian, chezhan, genbanren, gongqu, zuoyeren,
                         renwuliang, xiangmu, fenlei,
                         yuefen,
                         gongzuoneirong, zhouqi, neirongshuoming, danwei, wanchengshuliang,
                         starttime, endtime,
                         COLUMN_NAMES)

    database.paging(all_data, pagesize, current_page, data_dict)  # 分页
    database.export(all_data, data_dict, u'录入页导出模板.xls', '6')  # 导出
    return render(request, 'Model6/select.html', data_dict)


def add_html(request):
    # 查询下拉框
    data_dict = dict()
    data_dict['xianbies'] = Pub.select_column(XianbieChejianChenzhan, 'xianbie')
    data_dict['xiangmus'] = Pub.select_column(ZhuYe, 'xiangmu')
    return render(request, 'Model6/add.html', data_dict)


def add(request):
    # 前端数据
    duanbie = request.POST['duanbie']
    xianbie = request.POST['xianbie']
    chejian = request.POST['chejian']
    chezhan = request.POST['chezhan']
    genbanren = request.POST['genbanren']
    gongqu = request.POST['gongqu']
    zuoyeren = request.POST['zuoyeren']
    renwuliang = request.POST['renwuliang']
    xiangmu = request.POST['xiangmu']
    fenlei = request.POST['fenlei']
    gongzuoneirong = request.POST['gongzuoneirong']
    zhouqi = request.POST['zhouqi']
    neirongshuoming = request.POST['neirongshuoming']
    danwei = request.POST['danwei']
    wanchengshuliang = request.POST['wanchengshuliang']
    wanchengriqi = request.POST['wanchengriqi']

    month1 = request.POST.get('month1', '')
    month2 = request.POST.get('month2', '')
    month3 = request.POST.get('month3', '')
    month4 = request.POST.get('month4', '')
    month5 = request.POST.get('month5', '')
    month6 = request.POST.get('month6', '')
    month7 = request.POST.get('month7', '')
    month8 = request.POST.get('month8', '')
    month9 = request.POST.get('month9', '')
    month10 = request.POST.get('month10', '')
    month11 = request.POST.get('month11', '')
    month12 = request.POST.get('month12', '')
    yuefen = business.get_gongzuo_jidu(
            [month1, month2, month3, month4, month5, month6, month7, month8, month9, month10,
             month11, month12, ])

    # 添加录入页
    luruye = Luruye()
    luruye.duanbie = duanbie
    luruye.xianbie = xianbie
    luruye.chejian = chejian
    luruye.chezhan = chezhan
    luruye.genbanren = genbanren
    luruye.gongqu = gongqu
    luruye.zuoyeren = zuoyeren
    luruye.renwuliang = renwuliang
    luruye.xiangmu = xiangmu
    luruye.fenlei = fenlei
    luruye.yuefen = yuefen
    luruye.gongzuoneirong = gongzuoneirong
    luruye.zhouqi = zhouqi
    luruye.neirongshuoming = neirongshuoming
    luruye.danwei = danwei
    luruye.wanchengshuliang = wanchengshuliang
    luruye.wanchengriqi = wanchengriqi
    luruye.save()

    # 根据添加的录入页修改主页数据
    today = datetime.date.today()
    current_year = int(today.year)
    current_month = int(today.month)
    zhuye = ZhuYe.objects.filter(chejian=chejian, chezhan=chezhan, xiangmu=xiangmu,
                                 fenlei=fenlei).first()
    if zhuye:
        # 有该车间,车站,工作内容分类则修改数据
        wanchengriqi_split = wanchengriqi.split('-')
        wanchengriqi_year = int(wanchengriqi_split[0])
        wanchengriqi_month = int(wanchengriqi_split[1])

        if wanchengriqi_year == current_year and wanchengriqi_month == current_month:  # 年份月份一样则相加
            zhuye.benyuewanchen = int(zhuye.benyuewanchen) + int(wanchengshuliang)
        zhuye.xiangmu = xiangmu
        zhuye.fenlei = fenlei
        zhuye.yuefen = yuefen
        zhuye.danwei = danwei
        zhuye.renwuliang = renwuliang
        zhuye.leijiwanchen = int(zhuye.leijiwanchen) + int(wanchengshuliang)
        zhuye.xianbie = xianbie
        zhuye.chejian = chejian
        zhuye.chezhan = chezhan
        zhuye.zhouqi = zhouqi
        zhuye.neirongshuoming = neirongshuoming
        zhuye.create_time = wanchengriqi
        zhuye.save()
    else:
        # 无该车间,车站,工作内容分类则添加一条数据
        new_zhuye = ZhuYe()
        new_zhuye.xiangmu = xiangmu
        new_zhuye.fenlei = fenlei
        new_zhuye.yuefen = yuefen
        new_zhuye.danwei = danwei
        new_zhuye.renwuliang = renwuliang
        new_zhuye.benyuewanchen = wanchengshuliang
        new_zhuye.leijiwanchen = wanchengshuliang
        new_zhuye.xianbie = xianbie
        new_zhuye.chejian = chejian
        new_zhuye.chezhan = chezhan
        new_zhuye.zhouqi = zhouqi
        new_zhuye.neirongshuoming = neirongshuoming
        new_zhuye.create_time = wanchengriqi
        new_zhuye.save()

    return redirect('/Model6/zhuye.html/')


def update_html(request):
    update_id = request.GET['update_id']
    data_dict = dict()

    obj = Luruye.objects.get(auto_id=update_id)
    data_dict['auto_id'] = obj.auto_id
    data_dict['duanbie'] = obj.duanbie
    data_dict['xianbie'] = obj.xianbie
    data_dict['chejian'] = obj.chejian
    data_dict['chezhan'] = obj.chezhan
    data_dict['genbanren'] = obj.genbanren
    data_dict['gongqu'] = obj.gongqu
    data_dict['zuoyeren'] = obj.zuoyeren
    data_dict['renwuliang'] = obj.renwuliang
    data_dict['xiangmu'] = obj.xiangmu
    data_dict['fenlei'] = obj.fenlei
    data_dict['yuefen'] = obj.yuefen
    data_dict['gongzuoneirong'] = obj.gongzuoneirong
    data_dict['zhouqi'] = obj.zhouqi
    data_dict['neirongshuoming'] = obj.neirongshuoming
    data_dict['danwei'] = obj.danwei
    data_dict['wanchengshuliang'] = obj.wanchengshuliang
    data_dict['wanchengriqi'] = obj.wanchengriqi
    return render(request, 'Model6/update.html', data_dict)


def update(request):
    auto_id = request.POST['auto_id']
    chejian = request.POST['chejian']
    chezhan = request.POST['chezhan']
    xiangmu = request.POST['xiangmu']
    fenlei = request.POST['fenlei']
    wanchengshuliang = request.POST['wanchengshuliang']
    old_shuliang = int(Luruye.objects.get(auto_id=auto_id).wanchengshuliang)
    Pub.update_db(Luruye, auto_id,
                  duanbie=request.POST['duanbie'],
                  xianbie=request.POST['xianbie'],
                  chejian=chejian,
                  chezhan=chezhan,
                  genbanren=request.POST['genbanren'],
                  gongqu=request.POST['gongqu'],
                  zuoyeren=request.POST['zuoyeren'],
                  renwuliang=request.POST['renwuliang'],
                  xiangmu=xiangmu,
                  fenlei=fenlei,
                  yuefen=request.POST['yuefen'],
                  gongzuoneirong=request.POST['gongzuoneirong'],
                  zhouqi=request.POST['zhouqi'],
                  neirongshuoming=request.POST['neirongshuoming'],
                  danwei=request.POST['danwei'],
                  wanchengshuliang=wanchengshuliang,
                  wanchengriqi=request.POST['wanchengriqi'],
                  )
    db.updte_zhuye(chejian, chezhan, xiangmu, fenlei, old_shuliang, wanchengshuliang)
    return redirect("/Model6/select.html/")


def delete(request):
    delete_ids = request.GET['delete_ids']
    ids = delete_ids.split('_')
    ids.pop(len(ids) - 1)  # 去除最后的空串
    for delete_id in ids:
        delete_obj = Luruye.objects.get(auto_id=int(delete_id))
        chejian = delete_obj.chejian
        chezhan = delete_obj.chezhan
        xiangmu = delete_obj.xiangmu
        fenlei = delete_obj.fenlei
        wanchengshuliang = delete_obj.wanchengshuliang
        wanchengriqi = delete_obj.wanchengriqi
        zhuye_obj = ZhuYe.objects.filter(chejian=chejian, chezhan=chezhan, xiangmu=xiangmu,
                                         fenlei=fenlei).first()

        zhuye_obj.leijiwanchen = int(zhuye_obj.leijiwanchen) - int(wanchengshuliang)
        today = datetime.date.today()
        current_year = int(today.year)
        current_month = int(today.month)
        wanchengriqi_split = wanchengriqi.split('-')
        wanchengriqi_year = int(wanchengriqi_split[0])
        wanchengriqi_month = int(wanchengriqi_split[1])
        if current_year == wanchengriqi_year and current_month == wanchengriqi_month:
            zhuye_obj.benyuewanchen = int(zhuye_obj.benyuewanchen) - int(wanchengshuliang)
        zhuye_obj.save()
        delete_obj.delete()
    # 根据删除修改主页
    return redirect('/Model6/select.html/')


def search_chejian(request):
    xianbie = request.GET['xianbie']
    chejian = database.select_chejian(xianbie)
    data = {'chejian': chejian}
    return HttpResponse(json.dumps(data), content_type="application/json")


def search_chezhan(request):
    xianbie = request.GET['xianbie']
    chejian = request.GET['chejian']
    chezhan = database.select_chezhan(xianbie, chejian)
    data = {'chezhan': chezhan}
    return HttpResponse(json.dumps(data), content_type="application/json")


def search_fenlei(request):
    xiangmu = request.GET['xiangmu']
    search_data = Luruye.objects.filter(xiangmu=xiangmu)
    fenlei = []
    for one in search_data:
        fenlei.append(one.fenlei)
    fenlei = list(set(fenlei))
    data = {'fenlei': fenlei}
    return HttpResponse(json.dumps(data), content_type="application/json")


def search_renwuliang_danwei(request):
    chejian = request.GET['chejian']
    chezhan = request.GET['chezhan']
    xiangmu = request.GET['xiangmu']
    fenlei = request.GET['fenlei']
    data_dict = dict()
    obj1 = ZhuYe.objects.filter(xiangmu=xiangmu, fenlei=fenlei).first()
    obj2 = ZhuYe.objects.filter(chejian=chejian, chezhan=chezhan, xiangmu=xiangmu,
                                fenlei=fenlei).first()
    danwei_string = 'danwei'
    zhouqi_string = 'zhouqi'
    neirongshuoming_string = 'neirongshuoming'
    yuefen_string = 'yuefen'
    renwuliang_string = 'renwuliang'
    if obj1:
        data_dict[danwei_string] = obj1.danwei
        data_dict[zhouqi_string] = obj1.zhouqi
        data_dict[neirongshuoming_string] = obj1.neirongshuoming
        data_dict[yuefen_string] = obj1.yuefen.split('-')
    else:
        data_dict[danwei_string] = ''
        data_dict[zhouqi_string] = ''
        data_dict[neirongshuoming_string] = ''
        data_dict[yuefen_string] = []
    if obj2:
        data_dict[renwuliang_string] = obj2.renwuliang
    else:
        data_dict[renwuliang_string] = ''
    return HttpResponse(json.dumps(data_dict), content_type="application/json")


def zhuye_html(request):
    data_dict = dict()
    # 查询下拉框
    data_dict['chejians'] = Pub.select_column(XianbieChejianChenzhan, 'chejian')
    data_dict['xiangmus'] = Pub.select_column(ZhuYe, 'xiangmu')
    data_dict['fenleis'] = Pub.select_column(ZhuYe, 'fenlei')
    return render(request, 'Model6/zhuye.html', data_dict)


def zhuye(request):
    data_dict = dict()
    qianduan_chejians = request.GET['chejians']
    qianduan_xiangmu = request.GET.get('xiangmu', '')
    qianduan_fenlei = request.GET.get('fenlei', '')
    yuefen = request.GET.get('yuefen', '')
    chezhans = []
    qianduan_chejians = business.split_qianduan_data(qianduan_chejians)

    all_chejian_chezhans = []

    for chejian in qianduan_chejians:
        chejian_chezhans = dict()
        chejian_chezhans['chejian'] = chejian
        chezhans_for_one_chejian = []
        objs = Luruye.objects.filter(chejian=chejian)
        if objs:
            for common_obj in objs:
                chezhans_for_one_chejian.append(common_obj.chezhan)
        else:
            chezhans_for_one_chejian.append('')
        chezhans_for_one_chejian = list(set(chezhans_for_one_chejian))
        chejian_chezhans['chezhan'] = chezhans_for_one_chejian
        all_chejian_chezhans.append(chejian_chezhans)

    data_dict['head'] = all_chejian_chezhans

    for one in all_chejian_chezhans:
        chezhans += one['chezhan']

    xiangmus = db.set_xiangmus(qianduan_xiangmu, qianduan_fenlei)
    data_dict['xiangmu'] = xiangmus

    database_data = []
    data_dict['body'] = database_data
    index = 1
    for xiangmu in xiangmus:
        fenleis = []
        obj_by_xiangmus = ZhuYe.objects.filter(xiangmu=xiangmu)
        for obj_by_xiangmu in obj_by_xiangmus:
            fenleis += business.set_fenleis(yuefen, obj_by_xiangmu, qianduan_fenlei)
        fenleis = list(set(fenleis))
        for fenlei in fenleis:
            common_obj = ZhuYe.objects.filter(xiangmu=xiangmu, fenlei=fenlei, ).first()

            one_row = dict()
            one_row['auto_id'] = index
            one_row['xiangmu'] = common_obj.xiangmu
            one_row['fenlei'] = common_obj.fenlei
            one_row['danwei'] = common_obj.danwei
            one_row['zhouqi'] = common_obj.zhouqi
            one_row['neirongshuoming'] = common_obj.neirongshuoming
            one_row['yuefen'] = common_obj.yuefen

            renweiliang = []
            one_row['renwuliang'] = renweiliang
            benyuewancheng = []
            one_row['benyuewancheng'] = benyuewancheng
            leijiwancheng = []
            one_row['leijiwancheng'] = leijiwancheng
            benyue_history = []
            one_row['benyue_history'] = benyue_history
            leiji_history = []
            one_row['leiji_history'] = leiji_history
            zong_benyue_history = '/Model6/history.html/?xiangmu={}&fenlei={}&chadangyue=True'.format(
                    xiangmu, fenlei)
            zong_leiji_history = '/Model6/history.html/?xiangmu={}&fenlei={}'.format(xiangmu,
                                                                                     fenlei)
            for item in all_chejian_chezhans:
                chejian_name = item['chejian']
                chezhan_names = item['chezhan']
                for chezhan in chezhan_names:
                    zhuye_obj = ZhuYe.objects.filter(xiangmu=common_obj.xiangmu, fenlei=fenlei,
                                                     chezhan=chezhan).first()
                    if zhuye_obj:
                        renweiliang.append(zhuye_obj.renwuliang)
                        benyuewancheng.append(
                                db.select_benyuewancheng(chejian_name, chezhan, xiangmu, fenlei))
                        url_benyuye = '/Model6/history.html/?chejian={}&chezhan={}&xiangmu={}&fenlei={}&chadangyue=True'.format(
                                chejian_name,
                                chezhan,
                                common_obj.xiangmu,
                                fenlei)
                        benyue_history.append(url_benyuye)

                        leijiwancheng.append(zhuye_obj.leijiwanchen)
                        url_leiji = '/Model6/history.html/?chejian={}&chezhan={}&xiangmu={}&fenlei={}'.format(
                                chejian_name,
                                chezhan,
                                common_obj.xiangmu,
                                fenlei)
                        leiji_history.append(url_leiji)
                    else:
                        renweiliang.append('')
                        benyuewancheng.append('')
                        benyue_history.append('#')
                        leijiwancheng.append('')
                        leiji_history.append('#')
            renweiliang = qiuhe(renweiliang)
            one_row['renwuliang'] = renweiliang
            benyuewancheng = qiuhe(benyuewancheng)
            one_row['benyuewancheng'] = benyuewancheng
            leijiwancheng = qiuhe(leijiwancheng)
            one_row['leijiwancheng'] = leijiwancheng
            benyue_history = [zong_benyue_history] + benyue_history
            one_row['benyue_history'] = benyue_history

            leiji_history = [zong_leiji_history] + leiji_history
            one_row['leiji_history'] = leiji_history

            database_data.append(one_row)
            index += 1
        data_dict['body'] = database_data
    folder = 'Model6/export_{}.xls'.format(Pub.get_time())
    save_path = os.path.join(Pub.EXPORT_FOLDER, folder)
    data_dict['file'] = Pub.STATIC_EXPORT_FOLDER + '/' + folder
    XLS.merge_write(save_path, '年度测试工作任务表', data_dict)
    return HttpResponse(json.dumps(data_dict), content_type="application/json")


def history_html(request):
    data_dict = dict()
    chejian = request.GET.get('chejian', '')
    chezhan = request.GET.get('chezhan', '')
    xiangmu = request.GET.get('xiangmu', '')
    fenlei = request.GET.get('fenlei', '')
    chadangyue = request.GET.get('chadangyue', '')
    data_dict['chejian'] = chejian
    data_dict['chezhan'] = chezhan
    data_dict['xiangmu'] = xiangmu
    data_dict['fenlei'] = fenlei
    # 按条件查询
    q = Q()
    q.connector = 'AND'
    if chejian != '':
        q.children.append(('chejian', chejian))
    if chezhan != '':
        q.children.append(('chezhan', chezhan))
    if fenlei != '':
        q.children.append(('fenlei', fenlei))
    if xiangmu != '':
        q.children.append(('xiangmu', xiangmu))
    filter_data = Luruye.objects.filter(q).order_by('xianbie').order_by('chejian').order_by(
            'chezhan')
    today = datetime.date.today()
    current_year = int(today.year)
    current_month = int(today.month)
    data_dict['data'] = db.select_history(chejian, chezhan, xiangmu, fenlei, chadangyue,
                                          COLUMN_NAMES)

    return render(request, 'Model6/history.html', data_dict)


def history_add_html(request):
    data_dict = dict()
    chejian = request.GET['chejian']
    chezhan = request.GET['chezhan']
    xiangmu = request.GET['xiangmu']
    fenlei = request.GET['fenlei']

    data_dict['xianbies'] = Pub.select_column(XianbieChejianChenzhan, 'xianbie')

    if chezhan != '':
        zhuye = ZhuYe.objects.filter(chejian=chejian, chezhan=chezhan, xiangmu=xiangmu,
                                     fenlei=fenlei).first()
        data_dict['xianbie'] = zhuye.xianbie
        data_dict['chejian'] = zhuye.chejian
        data_dict['chezhan'] = zhuye.chezhan
        data_dict['xiangmu'] = zhuye.xiangmu
        data_dict['fenlei'] = zhuye.fenlei
        data_dict['renwuliang'] = zhuye.renwuliang
        data_dict['zhouqi'] = zhuye.zhouqi
        data_dict['neirongshuoming'] = zhuye.neirongshuoming
        data_dict['danwei'] = zhuye.danwei
    else:
        zhuye = ZhuYe.objects.filter(xiangmu=xiangmu, fenlei=fenlei).first()
        data_dict['xiangmu'] = zhuye.xiangmu
        data_dict['fenlei'] = zhuye.fenlei
        data_dict['renwuliang'] = zhuye.renwuliang
        data_dict['zhouqi'] = zhuye.zhouqi
        data_dict['neirongshuoming'] = zhuye.neirongshuoming
        data_dict['danwei'] = zhuye.danwei

    return render(request, 'Model6/history_add.html', data_dict)


def import_html(request):
    return render(request, 'Model6/import.html')


def see_data(request):
    data_dict = dict()
    file_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = os.path.join(Pub.IMPORT_FOLDER,
                                'data_Model6_check_{}.xls'.format(Pub.get_time()))

        Pub.save_file(filename, file)
        try:
            file_data = Pub.read_xls(filename, 2)
            data_dict['success'] = '查看成功'
        except Exception as e:
            data_dict['success'] = '查看失败->{}'.format(e)
    data_dict['data'] = file_data
    return render(request, 'Model6/import.html', data_dict)


def import_data(request):
    data_dict = dict()
    file_data = []
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = os.path.join(Pub.IMPORT_FOLDER, 'Model6', 'import_{}.xls'.format(Pub.get_time()))
        Pub.save_file(filename, file)
        try:
            file_data = Pub.read_xls(filename, 2)
            for row_data in file_data:
                # 前端数据
                duanbie = row_data[1]
                xianbie = row_data[2]
                chejian = row_data[3]
                chezhan = row_data[4]
                genbanren = row_data[5]
                gongqu = row_data[6]
                zuoyeren = row_data[7]
                renwuliang = row_data[8]
                xiangmu = row_data[9]
                fenlei = row_data[10]
                yuefen = row_data[11]
                gongzuoneirong = row_data[11 + 1]
                zhouqi = row_data[12 + 1]
                neirongshuoming = row_data[13 + 1]
                danwei = row_data[14 + 1]
                wanchengshuliang = row_data[15 + 1]
                wanchengriqi = row_data[16 + 1]

                # 添加录入页
                luruye = Luruye()
                luruye.duanbie = duanbie
                luruye.xianbie = xianbie
                luruye.chejian = chejian
                luruye.chezhan = chezhan
                luruye.genbanren = genbanren
                luruye.gongqu = gongqu
                luruye.zuoyeren = zuoyeren
                luruye.renwuliang = renwuliang
                luruye.xiangmu = xiangmu
                luruye.fenlei = fenlei
                luruye.yuefen = yuefen
                luruye.gongzuoneirong = gongzuoneirong
                luruye.zhouqi = zhouqi
                luruye.neirongshuoming = neirongshuoming
                luruye.danwei = danwei
                luruye.wanchengshuliang = wanchengshuliang
                luruye.wanchengriqi = wanchengriqi
                luruye.save()

                # 根据添加的录入页修改主页数据
                today = datetime.date.today()
                current_year = int(today.year)
                current_month = int(today.month)
                zhuye = ZhuYe.objects.filter(chejian=chejian, chezhan=chezhan, xiangmu=xiangmu,
                                             fenlei=fenlei).first()
                if zhuye:
                    # 有该车间,车站,工作内容分类则修改数据

                    wanchengriqi_split = wanchengriqi.split('-')
                    wanchengriqi_year = int(wanchengriqi_split[0])
                    wanchengriqi_month = int(wanchengriqi_split[1])

                    if wanchengriqi_year == current_year and wanchengriqi_month == current_month:  # 年份月份一样则相加
                        zhuye.benyuewanchen = int(zhuye.benyuewanchen) + int(wanchengshuliang)
                    zhuye.xiangmu = xiangmu
                    zhuye.fenlei = fenlei
                    zhuye.danwei = danwei
                    zhuye.renwuliang = renwuliang
                    zhuye.leijiwanchen = int(zhuye.leijiwanchen) + int(wanchengshuliang)
                    zhuye.chejian = chejian
                    zhuye.chezhan = chezhan
                    zhuye.zhouqi = zhouqi
                    zhuye.neirongshuoming = neirongshuoming
                    zhuye.create_time = wanchengriqi
                    zhuye.save()
                else:
                    # 无该车间,车站,工作内容分类则添加一条数据

                    new_zhuye = ZhuYe()
                    new_zhuye.xiangmu = xiangmu
                    new_zhuye.fenlei = fenlei
                    new_zhuye.danwei = danwei
                    new_zhuye.renwuliang = renwuliang
                    new_zhuye.benyuewanchen = wanchengshuliang
                    new_zhuye.leijiwanchen = wanchengshuliang
                    new_zhuye.chejian = chejian
                    new_zhuye.chezhan = chezhan
                    new_zhuye.zhouqi = zhouqi
                    new_zhuye.neirongshuoming = neirongshuoming
                    new_zhuye.create_time = wanchengriqi
                    new_zhuye.save()
            data_dict['success'] = '导入成功'
        except Exception as e:
            data_dict['success'] = '导入失败->{}'.format(e)
    data_dict['data'] = file_data
    return render(request, 'Model6/import.html', data_dict)
