from django.db.models import Q
from django.db.models.sql import AND

from Model7.models import DataTable


def select(xianbie, chejian, didian, zongcheng, mingcheng, bianhao, guige, dengji, fanwei, changjia,
           zhuanye, fuzeren, riqi, xiaciriqi, zhouqi, dangqianzhuangtai, yibiaozhuangtai, beizhu,
           column_names):
    q = Q()
    q.connector = AND
    if xianbie != '':
        q.children.append(('xianbie', xianbie))
    if chejian != '':
        q.children.append(('chejian', chejian))
    if didian != '':
        q.children.append(('didian', didian))
    if zongcheng != '':
        q.children.append(('zongcheng', zongcheng))
    if mingcheng != '':
        q.children.append(('mingcheng', mingcheng))
    if bianhao != '':
        q.children.append(('bianhao__icontains', bianhao))
    if guige != '':
        q.children.append(('guige__icontains', guige))
    if dengji != '':
        q.children.append(('dengji', dengji))
    if fanwei != '':
        q.children.append(('fanwei', fanwei))
    if changjia != '':
        q.children.append(('changjia', changjia))
    if zhuanye != '':
        q.children.append(('zhuanye', zhuanye))
    if fuzeren != '':
        q.children.append(('fuzeren', fuzeren))
    if riqi != '':
        q.children.append(('riqi', riqi))
    if xiaciriqi != '':
        q.children.append(('xiaciriqi', xiaciriqi))
    if zhouqi != '':
        q.children.append(('zhouqi', zhouqi))
    if dangqianzhuangtai == '无数据':
        q.children.append(('dangqianzhuangtai', ''))
    elif dangqianzhuangtai != '':
        q.children.append(('dangqianzhuangtai', dangqianzhuangtai))
    else:
        pass
    if yibiaozhuangtai != '':
        q.children.append(('yibiaozhuangtai', yibiaozhuangtai))
    if beizhu != '':
        q.children.append(('beizhu', beizhu))

    objects = DataTable.objects.filter(q).order_by('xianbie').order_by('chejian')

    all_data = []
    for obj in objects:
        one_data = list()
        for column_name in column_names:
            one_data.append(obj.__dict__[column_name])
        all_data.append(one_data)
    return all_data
