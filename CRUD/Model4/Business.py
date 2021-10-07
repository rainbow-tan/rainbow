# 排序前三项
def sort_data(data):
    data.sort(key=lambda x: (x[1], x[2], x[3]))
    return data


def can_import(data):
    index = [1, 2, 3, 5]  # 不能为空串
    msg = ''
    for one_data in data:
        for need_index in index:
            if one_data[need_index] == '':
                msg = '下标{}数据为空'.format(need_index)
                return False, msg
    return True, msg
