from django.db.models import Q


def select_business(table_name, field1, field2, field3, field23, field24, field37, field48, field49,
                    field50, field52, field71, field72, field55, field57, field59, field61, field54,
                    column_names):
    q = Q()
    q.connector = 'AND'
    if field1 != '':
        q.children.append(('field1', field1))
    if field2 != '':
        q.children.append(('field2', field2))
    if field3 != '':
        q.children.append(('field3', field3))
    if field23 != '':
        q.children.append(('field23', field23))
    if field24 != '':
        q.children.append(('field24', field24))
    if field37 != '':
        q.children.append(('field37', field37))
    if field48 != '':
        q.children.append(('field48__contains', field48))
    if field49 != '':
        q.children.append(('field49__contains', field49))
    if field50 != '':
        q.children.append(('field50', field50))
    if field52 != '':
        q.children.append(('field52__contains', field52))
    if field71 != '':
        q.children.append(('field71', field71))
    if field72 == '无数据':
        q.children.append(('field72', ''))
    elif field72 != '':
        q.children.append(('field72', field72))
    else:
        pass
    if field55 == '无数据':
        q.children.append(('field55', ''))
    elif field55 != '':
        q.children.append(('field55', field55))
    else:
        pass
    if field57 == '无数据':
        q.children.append(('field57', ''))
    elif field57 != '':
        q.children.append(('field57', field57))
    else:
        pass
    if field59 == '无数据':
        q.children.append(('field59', ''))
    elif field59 != '':
        q.children.append(('field59', field59))
    else:
        pass
    if field61 == '无数据':
        q.children.append(('field61', ''))
    elif field61 != '':
        q.children.append(('field61', field61))
    else:
        pass
    if field54 == '无数据':
        q.children.append(('field54', ''))
    elif field54 != '':
        q.children.append(('field54', field54))
    else:
        pass
    filter_data = table_name.objects.filter(q)
    all_data_list = []
    for data in filter_data:
        one_data = list()
        for column_name in column_names:
            one_data.append(data.__dict__[column_name])
        all_data_list.append(one_data)
    return all_data_list
