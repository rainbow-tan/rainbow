# -*- encoding=utf-8 -*-
from django.db.models import Q
from django.db.models.sql import AND

from Model4.models import DataTable as DataTable4
from Model8.models import DataTable
from Model8.models import QuDuanTable


def select(wentiriqi, xianbie, chejian, chezhan, quduan, buliangdianrong, hangbie, dianrongshuliang,
           zaiping, chuliriqi, yuanying, chuliqingkuang, shangbaoqingkuang, zhouqi, beizhu,
           qiandianliu, houdianliu, qiandianya, houdianya, qiandianrong, houdianrong, changjia,
           shiyongshijian, fankuiren, column_names):
    q = Q()
    q.connector = AND
    if wentiriqi != '':
        q.children.append(('wentiriqi', wentiriqi))
    if xianbie != '':
        q.children.append(('xianbie', xianbie))
    if chejian != '':
        q.children.append(('chejian', chejian))
    if chezhan != '':
        q.children.append(('chezhan', chezhan))
    if quduan != '':
        q.children.append(('quduan__icontains', quduan))
    if buliangdianrong != '':
        q.children.append(('buliangdianrong', buliangdianrong))
    if hangbie != '':
        q.children.append(('hangbie', hangbie))
    if dianrongshuliang != '':
        q.children.append(('dianrongshuliang', dianrongshuliang))
    if zaiping != '':
        q.children.append(('zaiping', zaiping))
    if chuliriqi != '':
        q.children.append(('chuliriqi', chuliriqi))
    if yuanying != '':
        q.children.append(('yuanying__icontains', yuanying))
    if chuliqingkuang != '':
        q.children.append(('chuliqingkuang', chuliqingkuang))
    if shangbaoqingkuang != '':
        q.children.append(('shangbaoqingkuang', shangbaoqingkuang))
    if zhouqi != '':
        q.children.append(('zhouqi', zhouqi))
    if beizhu != '':
        q.children.append(('beizhu', beizhu))
    if qiandianliu != '':
        q.children.append(('qiandianliu', qiandianliu))
    if houdianliu != '':
        q.children.append(('houdianliu', houdianliu))
    if qiandianya != '':
        q.children.append(('qiandianya', qiandianya))
    if houdianya != '':
        q.children.append(('houdianya', houdianya))
    if qiandianrong != '':
        q.children.append(('qiandianrong', qiandianrong))
    if houdianrong != '':
        q.children.append(('houdianrong', houdianrong))
    if changjia != '':
        q.children.append(('changjia', changjia))
    if shiyongshijian != '':
        q.children.append(('shiyongshijian', shiyongshijian))
    if fankuiren != '':
        q.children.append(('fankuiren', fankuiren))

    objects = DataTable.objects.filter(q).order_by('-wentiriqi')

    all_data = []
    for obj in objects:
        one_data = list()
        for column_name in column_names:
            one_data.append(obj.__dict__[column_name])
        all_data.append(one_data)
    return all_data


def search_fileds_by_quduan(quduan):
    data = dict()
    obj = DataTable4.objects.filter(field48=quduan).first()
    if obj:
        data['xianbie'] = obj.field1
        data['chejian'] = obj.field2
        data['chezhan'] = obj.field3
        data['field48'] = obj.field48
        data['zaiping'] = obj.field37
        data['field50'] = obj.field50
        data['dianrongshuliang'] = obj.field54
        data['field85'] = obj.field85
        data['field86'] = obj.field86
        data['field87'] = obj.field87
        data['field88'] = obj.field88
        data['field89'] = obj.field89
        data['field90'] = obj.field90
        data['field91'] = obj.field91
        data['field92'] = obj.field92
        data['field93'] = obj.field93
        data['field94'] = obj.field94
        data['field95'] = obj.field95
        data['field96'] = obj.field96
        data['field97'] = obj.field97
        data['field98'] = obj.field98
        data['field99'] = obj.field99
        data['field100'] = obj.field100
        data['field101'] = obj.field101
        data['field102'] = obj.field102
        data['field103'] = obj.field103
        data['field104'] = obj.field104
        data['field105'] = obj.field105
        data['field106'] = obj.field106
        data['field107'] = obj.field107
        data['field108'] = obj.field108
        data['field109'] = obj.field109
        data['field110'] = obj.field110

    else:
        data['xianbie'] = ''
        data['chejian'] = ''
        data['chezhan'] = ''
        data['field48'] = ''
        data['zaiping'] = ''
        data['field50'] = ''
        data['dianrongshuliang'] = ''
        data['field85'] = ''
        data['field86'] = ''
        data['field87'] = ''
        data['field88'] = ''
        data['field89'] = ''
        data['field90'] = ''
        data['field91'] = ''
        data['field92'] = ''
        data['field93'] = ''
        data['field94'] = ''
        data['field95'] = ''
        data['field96'] = ''
        data['field97'] = ''
        data['field98'] = ''
        data['field99'] = ''
        data['field100'] = ''
        data['field101'] = ''
        data['field102'] = ''
        data['field103'] = ''
        data['field104'] = ''
        data['field105'] = ''
        data['field106'] = ''
        data['field107'] = ''
        data['field108'] = ''
        data['field109'] = ''
        data['field110'] = ''
    return data


def get_quduan_info(xianbie, chezhan, quduan):
    data = dict()
    obj = QuDuanTable.objects.filter(xianbie=xianbie, chezhan=chezhan, quduan=quduan).first()
    if obj:
        data['zaiping'] = obj.zaiping
        data['dianrongshuliang'] = obj.dianrongshuliang
        data['hangbie'] = obj.hangbie
        data['quduanchangdu'] = obj.quduanchangdu
    else:
        data['zaiping'] = ''
        data['dianrongshuliang'] = ''
        data['hangbie'] = ''
        data['quduanchangdu'] = ''
    return data
