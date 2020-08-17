# -*- encoding=utf-8 -*-

from Model.models import DataTable
from Model.models import Field1Table
from Model.models import Field2Table
from Model.models import Field3Table
from Model.models import Field23Table
from Model.models import Field24Table
from Model.models import Field25Table
from Model.models import Field26Table
from Model.models import Field27Table
from django.db.models import Q

table = {'DataTable': DataTable,
         "Field1Table": Field1Table,
         "Field2Table": Field2Table,
         "Field3Table": Field3Table,
         "Field23Table": Field23Table,
         "Field24Table": Field24Table,
         "Field25Table": Field25Table,
         "Field26Table": Field26Table,
         "Field27Table": Field27Table,
         }


def select_all(table_name, field_count):
    """
    查表的所有数据
    :param table_name: 表名
    :param field_count: 字段数量,必须为auto_id和field1,field2
    :return: [[],[],[]]
    """
    all_data = table[table_name].objects.all()
    all_data_list = []
    for data in all_data:
        one_data = list()
        one_data.append(data.__dict__['auto_id'])
        for index in range(field_count):
            one_data.append(data.__dict__['field{}'.format(index + 1)])
        all_data_list.append(one_data)
    return all_data_list


def select_filter_and(table_name, field_count, auto_id, *args):
    """
    根据不定个参数查询数据，采用AND方式
    :param table_name: 表名
    :param field_count: 字段数量,必须为auto_id和field1,field2
    :param auto_id: 给定auto_id则为objects.get()返回数据只有一条
    :param args: 不定个参数查询
    :return: [[],[],[]]
    """
    q = Q()
    q.connector = 'AND'
    if auto_id != '':
        q.children.append(('auto_id', auto_id))
    for index, arg in enumerate(args):
        if arg != '':
            q.children.append(('field{}'.format(index + 1), arg))
    all_data = table[table_name].objects.filter(q)

    all_data_list = []
    for data in all_data:
        one_data = list()
        one_data.append(data.__dict__['auto_id'])
        for index in range(field_count):
            one_data.append(data.__dict__['field{}'.format(index + 1)])
        all_data_list.append(one_data)

    return all_data_list


def select_filter_or(table_name, field_count, auto_id, *args):
    q = Q()
    q.connector = 'OR'
    if auto_id != '':
        q.children.append(('auto_id', auto_id))
    for index, arg in enumerate(args):
        if arg != '':
            q.children.append(('field{}'.format(index + 1), arg))
    all_data = table[table_name].objects.filter(q)

    all_data_list = []
    for data in all_data:
        one_data = list()
        one_data.append(data.__dict__['auto_id'])
        for index in range(field_count):
            one_data.append(data.__dict__['field{}'.format(index + 1)])
        all_data_list.append(one_data)

    return all_data_list


# 业务
def select_filter(table_name, field_count, field1, field2, field3, field16, field17, field21,
                  field22, field23, field24, field25, field26, field27):
    q1 = Q()
    q1.connector = 'OR'
    if field21 != '':
        q1.children.append(('field21', field21))
    if field22 != '':
        q1.children.append(('field22', field22))

    q2 = Q()
    q2.connector = 'AND'
    if field1 != '':
        q2.children.append(('field1', field1))
    if field2 != '':
        q2.children.append(('field2', field2))
    if field3 != '':
        q2.children.append(('field3', field3))
    if field16 != '':
        q2.children.append(('field16', field16))
    if field17 != '':
        q2.children.append(('field17', field17))
    if field23 != '':
        q2.children.append(('field23', field23))
    if field24 != '':
        q2.children.append(('field24', field24))
    if field25 != '':
        q2.children.append(('field25', field25))
    if field26 != '':
        q2.children.append(('field26', field26))
    if field27 != '':
        q2.children.append(('field27', field27))

    q = Q()
    q.add(q1, 'AND')
    q.add(q2, 'AND')

    all_data_list = []
    all_data = table[table_name].objects.filter(q)
    for data in all_data:
        one_data = list()
        one_data.append(data.__dict__['auto_id'])
        for index in range(field_count):
            one_data.append(data.__dict__['field{}'.format(index + 1)])
        all_data_list.append(one_data)

    return all_data_list


def select_column(table_name, column_name):
    """
    查询表中某一列
    :param table_name: 表名
    :param column_name: 列名
    :return: [[],[],[]]
    """
    column_data = table[table_name].objects.all().values(column_name)
    all_data = []
    for data in column_data:
        all_data.append(data[column_name])
    return all_data


def select_one(table_name, field_count, auto_id):
    """
    根据auto_id查
    :param table_name: 表名
    :param field_count: 字段数量,必须为auto_id和field1,field2
    :param auto_id:自增id
    :return:
    """
    one_data = table[table_name].objects.get(auto_id=auto_id)
    one_data_list = list()
    one_data_list.append(one_data.__dict__['auto_id'])
    for index in range(field_count):
        one_data_list.append(one_data.__dict__['field{}'.format(index + 1)])

    return one_data_list


def update(table_name, auto_id, *args):
    """
    根据auto_id修改
    :param table_name: 表名
    :param auto_id: 自增id
    :param args: 修改的数据['field1_value','field2_value','field3_value','','','',]
    :return:
    """
    update_object = table[table_name].objects.get(auto_id=auto_id)
    for index, arg in enumerate(args):
        update_object.__dict__['field{}'.format(index + 1)] = arg
    update_object.save()


def delete(table_name, auto_id):
    """
    根据auto_id删除
    :param table_name: 表名
    :param auto_id: 自增id
    :return:
    """
    table[table_name].objects.get(auto_id=auto_id).delete()


def insert(table_name, data_list):
    """
    插入
    :param table_name: 表名
    :param data_list:
    :return: auto_id自增，其他为添加的数据['field1_value','field2_value','field3_value','','','',]
    """
    print(data_list)
    insert_object = table[table_name]()
    for index, data in enumerate(data_list):
        insert_object.__dict__['field{}'.format(index + 1)] = data
    insert_object.save()
