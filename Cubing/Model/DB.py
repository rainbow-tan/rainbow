# -*- encoding=utf-8 -*-

from django.db.models import Q

from Model.models import PartTable


def select_for_auto_input(pn, column_names):
    q = Q()
    q.connector = Q.AND
    if pn != '':
        q.children.append(('pn', pn))
    filter_data = PartTable.objects.filter(q).last()
    data = list()
    for arg in column_names:
        if filter_data is not None:
            data.append(filter_data.__dict__[arg])
        else:
            data.append('')
    return data
