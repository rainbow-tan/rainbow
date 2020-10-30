# -*- encoding=utf-8 -*-

from django.db.models import Q


def select_business(table_name, field1, field2, field3, field4, field16, field17, field18, field24,
                    field25,
                    field26, field27, field28, limit, column_names):
    q1 = Q()
    q1.connector = 'AND'
    if field2 == '所有':  # 为所有时变成空串，查询出的数据就是所有车间
        field2 = ''
    if field1 != '':
        q1.children.append(('field1', field1))
    if field2 != '':
        q1.children.append(('field2', field2))
    if field3 != '':
        q1.children.append(('field3', field3))
    if field4 != '':
        q1.children.append(('field4__contains', field4))
    if field16 != '':
        q1.children.append(('field16', field16))
    if field17 != '':
        q1.children.append(('field17', field17))
    if field18 == '无数据':
        q1.children.append(('field18', ''))
    elif field18 != '':
        q1.children.append(('field18__contains', field18))  # like %field18%
    else:
        pass

    if field24 != '':
        q1.children.append(('field24', field24))
    if field25 != '':
        q1.children.append(('field25', field25))
    if field26 != '':
        q1.children.append(('field26', field26))
    if field27 != '':
        q1.children.append(('field27', field27))
    if field28 != '':
        q1.children.append(('field28__contains', field28))

    q2 = Q()
    q2.connector = 'OR'
    q2.children.append(('field21', '是'))
    q2.children.append(('field22', '是'))

    q = Q()

    if limit == '是':
        q.add(q1, 'AND')
        q.add(q2, 'AND')
    elif limit == '否':
        q.add(q1, 'AND')
        q.add(~q2, 'AND')
    else:
        q.add(q1, 'AND')
    filter_data = table_name.objects.filter(q)
    all_data_list = []
    for data in filter_data:
        one_data = list()
        for column_name in column_names:
            one_data.append(data.__dict__[column_name])
        all_data_list.append(one_data)
    return all_data_list
