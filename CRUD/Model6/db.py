import datetime

from django.db.models import Q
from django.db.models.sql import AND

from CRUD import Pub
from Model6.models import Luruye
from Model6.models import ZhuYe


def select(duanbie, xianbie, chejian, chezhan, genbanren, gongqu, zuoyeren, renwuliang, xiangmu,
           fenlei, yuefen,
           gongzuoneirong, zhouqi, neirongshuoming, danwei, wanchengshuliang, starttime, endtime,
           column_names):
    q = Q()
    q.connector = AND
    if duanbie != '':
        q.children.append(('duanbie', duanbie))
    if xianbie != '':
        q.children.append(('xianbie', xianbie))
    if chejian != '':
        q.children.append(('chejian', chejian))
    if chezhan != '':
        q.children.append(('chezhan', chezhan))
    if genbanren != '':
        q.children.append(('genbanren', genbanren))
    if gongqu != '':
        q.children.append(('gongqu', gongqu))
    if zuoyeren != '':
        q.children.append(('zuoyeren', zuoyeren))
    if renwuliang != '':
        q.children.append(('renwuliang', renwuliang))
    if xiangmu != '':
        q.children.append(('xiangmu', xiangmu))
    if fenlei != '':
        q.children.append(('fenlei', fenlei))
    if yuefen != '':
        q.children.append(('yuefen', yuefen))
    if gongzuoneirong != '':
        q.children.append(('gongzuoneirong', gongzuoneirong))
    if zhouqi != '':
        q.children.append(('zhouqi', zhouqi))
    if neirongshuoming != '':
        q.children.append(('neirongshuoming', neirongshuoming))
    if danwei != '':
        q.children.append(('danwei', danwei))
    if wanchengshuliang != '':
        q.children.append(('wanchengshuliang', wanchengshuliang))
    if starttime != '':
        q.children.append(('wanchengriqi__gte', starttime))
    if endtime != '':
        q.children.append(('wanchengriqi__lte', endtime))
    objects = Luruye.objects.filter(q).order_by('xianbie').order_by('chejian').order_by('chezhan')

    all_data = []
    for obj in objects:
        one_data = list()
        for column_name in column_names:
            one_data.append(obj.__dict__[column_name])
        all_data.append(one_data)
    return all_data


def updte_zhuye(chejian, chezhan, xiangmu, fenlei, old_shuliang, new_shulaing):
    # 修改录入页的数量来修改主页
    old_shuliang = int(old_shuliang)
    new_shulaing = int(new_shulaing)
    pianyiliang = new_shulaing - old_shuliang
    obj = ZhuYe.objects.filter(chejian=chejian, chezhan=chezhan, xiangmu=xiangmu,
                               fenlei=fenlei).first()
    if obj:
        leijiwanchen = int(obj.leijiwanchen)
        new_leijiwanchen = leijiwanchen + pianyiliang
        obj.leijiwanchen = new_leijiwanchen
        obj.save()


def set_xiangmus(xiangmu, fenlei):
    # 根据前端出入的项目名称和分类名称决定查询的项目
    if xiangmu and fenlei:
        objs = ZhuYe.objects.filter(xiangmu=xiangmu, fenlei=fenlei)
        xiangmus = []
        for obj in objs:
            xiangmus.append(obj.xiangmu)
        xiangmus = list(set(xiangmus))
    elif xiangmu and not fenlei:
        xiangmus = [xiangmu]
    elif not xiangmu and fenlei:
        objs = ZhuYe.objects.filter(fenlei=fenlei)
        xiangmus = []
        for obj in objs:
            xiangmus.append(obj.xiangmu)
        xiangmus = list(set(xiangmus))
    else:
        xiangmus = list(Pub.select_column(ZhuYe, 'xiangmu'))
    return xiangmus


def select_benyuewancheng(chejian, chezhan, xiangmu, fenlei):
    objs = Luruye.objects.filter(chejian=chejian, chezhan=chezhan, xiangmu=xiangmu, fenlei=fenlei)
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    sum = 0
    for obj in objs:
        pass
        obj_time = datetime.datetime.strptime(obj.wanchengriqi, '%Y-%m-%d')
        obj_year = obj_time.year
        obj_month = obj_time.month
        if obj_year == year and obj_month == month:
            sum += int(obj.wanchengshuliang)
    return sum


def select_history(chejian, chezhan, xiangmu, fenlei, chadangyue, column_names):
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
    objects = Luruye.objects.filter(q).order_by('xianbie').order_by('chejian').order_by('chezhan')
    show_history = []
    for obj in objects:
        if chadangyue != '':
            now = datetime.datetime.now()
            year = now.year
            month = now.month
            obj_time = datetime.datetime.strptime(obj.wanchengriqi, '%Y-%m-%d')
            obj_year = obj_time.year
            obj_month = obj_time.month
            if obj_year == year and obj_month == month:
                show_history.append(obj)
        else:
            show_history.append(obj)

    all_data = []
    for obj in show_history:
        one_data = list()
        for column_name in column_names:
            one_data.append(obj.__dict__[column_name])
        all_data.append(one_data)
    return all_data
