# -*- encoding=utf-8 -*-

from django.shortcuts import render

from CRUD import Pub
from Model.models import Field1Table
from Model.models import Field2Table
from Model.models import Field3Table
from Model5.models import Luruye as Luruye5
from Model5.models import ZhuYe as ZhuYe5
from Model6.models import Luruye as Luruye6
from Model6.models import ZhuYe as ZhuYe6
from ModelA import db


def update_html(request):
    data_dict = dict()
    # 查询下拉框
    data_dict['xianbies'] = Pub.select_column(Field1Table, 'field1')
    data_dict['chejians'] = Pub.select_column(Field2Table, 'field1')
    data_dict['chezhans'] = Pub.select_column(Field3Table, 'field1')
    data_dict['xiangmus'] = Pub.select_column(ZhuYe5, 'xiangmu')
    data_dict['fenleis'] = Pub.select_column(ZhuYe5, 'fenlei')
    data_dict['xianbies6'] = data_dict['xianbies']
    data_dict['chejians6'] = data_dict['chejians']
    data_dict['chezhans6'] = data_dict['chezhans']
    data_dict['xiangmus6'] = Pub.select_column(ZhuYe6, 'xiangmu')
    data_dict['fenleis6'] = Pub.select_column(ZhuYe6, 'fenlei')
    return render(request, 'ModelA/update.html', data_dict)


def setting_html(request):
    return render(request, 'ModelA/setting.html')


def update(request):
    data_dict = dict()
    # 查询下拉框
    data_dict['xianbies'] = Pub.select_column(Field1Table, 'field1')
    data_dict['chejians'] = Pub.select_column(Field2Table, 'field1')
    data_dict['chezhans'] = Pub.select_column(Field3Table, 'field1')
    data_dict['xiangmus'] = Pub.select_column(ZhuYe5, 'xiangmu')
    data_dict['fenleis'] = Pub.select_column(ZhuYe5, 'fenlei')

    chejian = request.POST["chejian"]
    chezhan = request.POST["chezhan"]
    xiangmu = request.POST["xiangmu"]
    fenlei = request.POST["fenlei"]
    renwuliang = request.POST["renwuliang"]
    db.update(ZhuYe5, chejian, chezhan, xiangmu, fenlei, renwuliang)
    db.update(Luruye5, chejian, chezhan, xiangmu, fenlei, renwuliang)
    data_dict['msg'] = '修改完毕'

    return render(request, 'ModelA/update.html', data_dict)


def update6(request):
    data_dict = dict()
    # 查询下拉框
    data_dict['xianbies6'] = Pub.select_column(Field1Table, 'field1')
    data_dict['chejians6'] = Pub.select_column(Field2Table, 'field1')
    data_dict['chezhans6'] = Pub.select_column(Field3Table, 'field1')
    data_dict['xiangmus6'] = Pub.select_column(ZhuYe5, 'xiangmu')
    data_dict['fenleis6'] = Pub.select_column(ZhuYe5, 'fenlei')

    chejian = request.POST["chejian6"]
    chezhan = request.POST["chezhan6"]
    xiangmu = request.POST["xiangmu6"]
    fenlei = request.POST["fenlei6"]
    renwuliang = request.POST["renwuliang6"]
    db.update(ZhuYe6, chejian, chezhan, xiangmu, fenlei, renwuliang)
    db.update(Luruye6, chejian, chezhan, xiangmu, fenlei, renwuliang)

    return render(request, 'ModelA/update.html', data_dict)
