from django.db.models import Q
from django.db.models.sql import AND

from Model2.models import DataTable as DataTable2
from Model3.models import DataTable as DataTable3
from Model4.models import DataTable as DataTable4
from Model8.models import DataTable as DataTable8
from Model8.models import QuDuanTable


def select(xianbie, chezhan, quduan, zaiping, dianrongshuliang, hangbie, quduanchangdu,
           column_names):
    q = Q()
    q.connector = AND
    if xianbie != '':
        q.children.append(('xianbie', xianbie))
    if chezhan != '':
        q.children.append(('chezhan', chezhan))
    if quduan != '':
        q.children.append(('quduan', quduan))
    if zaiping != '':
        q.children.append(('zaiping', zaiping))
    if dianrongshuliang != '':
        q.children.append(('dianrongshuliang', dianrongshuliang))
    if hangbie != '':
        q.children.append(('hangbie', hangbie))
    if quduanchangdu != '':
        q.children.append(('quduanchangdu', quduanchangdu))

    objects = QuDuanTable.objects.filter(q).order_by('xianbie')

    all_data = []
    for obj in objects:
        one_data = list()
        for column_name in column_names:
            one_data.append(obj.__dict__[column_name])
        all_data.append(one_data)
    return all_data


def update_others(xianbie, chezhan, quduan, zaiping, dianrongshuliang, hangbie, quduanchangdu):
    objs = DataTable2.objects.filter(field1=xianbie, field3=chezhan, field35=quduan)
    try:
        for obj in objs:
            obj.field37 = zaiping
            obj.field38 = quduanchangdu
            obj.field39 = dianrongshuliang
            obj.field23 = hangbie
            obj.save()
    except Exception as e:
        print('修改闭塞失败:{}'.format(e))
    objs = DataTable3.objects.filter(field1=xianbie, field3=chezhan, field63=quduan)
    try:
        for obj in objs:
            obj.field37 = zaiping
            obj.field50 = quduanchangdu
            obj.field54 = dianrongshuliang
            obj.field23 = hangbie
            obj.save()
    except Exception as e:
        print('修改ZPW-2000失败:{}'.format(e))
    objs = DataTable4.objects.filter(field1=xianbie, field3=chezhan, field48=quduan)
    try:
        for obj in objs:
            obj.field37 = zaiping
            obj.field50 = quduanchangdu
            obj.field54 = dianrongshuliang
            obj.save()
    except Exception as e:
        print('修改移频轨道测试数据档案失败:{}'.format(e))
    objs = DataTable8.objects.filter(xianbie=xianbie, chezhan=chezhan, quduan=quduan)

    try:
        for obj in objs:
            obj.zaiping = zaiping
            obj.dianrongshuliang = dianrongshuliang
            obj.hangbie = hangbie
            obj.save()
    except Exception as e:
        print('修改高速综合检测车检测问题台账失败:{}'.format(e))
