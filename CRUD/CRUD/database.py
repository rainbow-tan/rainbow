# -*- encoding=utf-8 -*-
import os

from django.core.paginator import EmptyPage
from django.core.paginator import InvalidPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator

from CRUD import Pub
from Model7.models import XianbieChejianChenzhan


def select_chejian(xianbie):
    """根据线别查车间"""
    objs = XianbieChejianChenzhan.objects.filter(xianbie=xianbie)
    chejians = []
    for one in objs:
        chejians.append(one.chejian)
    chejians = list(set(chejians))  # 去重
    return chejians


def select_chezhan(xianbie, chejian):
    """根据线别和车间查车站"""
    objs = XianbieChejianChenzhan.objects.filter(xianbie=xianbie, chejian=chejian)
    chezhans = []
    for one in objs:
        chezhans.append(one.chezhan)
    chezhans = list(set(chezhans))  # 去重
    return chezhans


def paging(db_data, pagesize, current_page, data_dict):
    """分页"""
    paginator = Paginator(db_data, pagesize)
    max_number = paginator.num_pages
    if current_page > max_number:  # 当前页大于总分页,默认最后一页
        current_page = max_number
    try:
        show_data = paginator.page(current_page)
    except PageNotAnInteger:
        show_data = paginator.page(1)
    except EmptyPage:
        show_data = paginator.page(max_number)
    except InvalidPage:
        show_data = paginator.page(1)
    except Exception as e:
        show_data = paginator.page(1)
        print('分页失败:{}'.format(e))

    # 前一页
    if current_page - 1 > 0:
        previous_page = current_page - 1
    else:
        previous_page = 1

    # 后一页
    if current_page + 1 < max_number:
        next_page = current_page + 1
    else:
        next_page = max_number

    # 传递给前端的数据
    data_dict['data'] = show_data
    data_dict['count'] = len(db_data)
    data_dict['pagesize'] = str(pagesize)
    data_dict['current_page'] = str(current_page)
    data_dict['previous_page'] = previous_page
    data_dict['next_page'] = next_page
    data_dict['last_page'] = max_number


def export(data, data_dict, template, index):
    """
    导出
    :param data: 导出的数据
    :param data_dict:
    :param template: 导出模板
    :param index: 第几个model
    :return:
    """
    filename = 'Model{}/export_{}.xls'.format(index, Pub.get_time())
    save_path = os.path.join(Pub.EXPORT_FOLDER, filename)
    data_dict['file'] = Pub.STATIC_EXPORT_FOLDER + '/' + filename
    write_data = Pub.change_auto_id(data)
    source_file = os.path.join(Pub.EXPORT_TEMPLATE_FOLDER, template)
    Pub.append_xls(source_file, save_path, write_data)
