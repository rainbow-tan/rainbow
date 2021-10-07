def can_import(data):
    """
    判断导入合理性
    :param data:
    :return:
    """
    msg = ''
    index = {2: '线别', 3: '综合车间', 4: '行别', 11: '是否站联区段', 12: '标称载频', 16: '是否容许信号', 17: '方向电路制式', }
    for one_data in data:
        for need_index in index:
            if one_data[need_index] == '':
                msg = '{} 数据为空'.format(index[need_index])
                return False, msg
        if one_data[13] != '':
            try:
                int(one_data[13])
            except Exception as e:
                msg = '区段长度非数值型'
                return False, msg
        if one_data[14] != '':
            try:
                int(one_data[14])
            except Exception as e:
                msg = '电容数量非数值型'
                return False, msg
    return True, msg


# 排序
def sort_data(data):
    data.sort(key=lambda x: (x[2], x[3]))
    return data
