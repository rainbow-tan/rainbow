from django.db.models import Q


def select_business(table_name, field1, field2, field3, field24, field37, field48, field50, field54,
                    column_names):
    q = Q()
    q.connector = 'AND'
    if field1 != '':
        q.children.append(('field1', field1))
    if field2 != '':
        q.children.append(('field2', field2))
    if field3 != '':
        q.children.append(('field3', field3))
    if field24 != '':
        q.children.append(('field24', field24))
    if field37 != '':
        q.children.append(('field37', field37))
    if field48 != '':
        q.children.append(('field48__contains', field48))
    if field50 != '':
        q.children.append(('field50', field50))
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
