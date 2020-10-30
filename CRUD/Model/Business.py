# -*- coding: utf-8 -*-


# 移除不显示字段
def remove_index_for_data(data_list, remove_index=[11, 12, 13, 14, 15, 16]):
    """
    移除不显示字段
    :param data_list:
    :param remove_index:
    :return:
    """
    new_data = []
    for one_data in data_list:
        new_one_data = []
        for index, data in enumerate(one_data):
            if index not in remove_index:
                new_one_data.append(data)
        new_data.append(new_one_data)
    return new_data


# 排序前三项
def sort_data(data):
    data.sort(key=lambda x: (x[1], x[2], x[3]))
    return data


# 判断*标数据
def can_import(data):
    index = {1: '线别', 2: '综合车间', 3: '车站及区间名称', 4: '设备名称',
             24: '站内或区间', 25: '参考标准', 26: '有无防撞墙', 27: '建筑设备类型', }
    msg = ''
    for one_data in data:
        for need_index in index:
            if one_data[need_index] == '':
                msg = '{} 数据为空'.format(index[need_index])
                return False, msg
    return True, msg


# 计算本线或邻线
def calculation(number1, number2):
    """
    计算本线或邻线
    :param number1: 空串或者数字
    :param number2: 高铁标准/普铁标准
    :return:
    """
    number3 = ''
    standard1 = '高铁标准'
    standard2 = '普铁标准'
    if number1 != '' and number2 == standard1:
        try:
            number1 = int(number1)
        except Exception as e:
            raise RuntimeError('本(临)线高度转换数值失败:{}'.format(number1))

        if 7250 < number1 <= 100000:
            number3 = ''
        elif 7000 < number1 <= 7250:
            number3 = '800'
        elif 6750 < number1 <= 7000:
            number3 = '950'
        elif 6500 < number1 <= 6750:
            number3 = '1100'
        elif 6250 < number1 <= 6500:
            number3 = '1250'
        elif 6000 < number1 <= 6250:
            number3 = '1400'
        elif 5750 < number1 <= 6000:
            number3 = '1550'
        elif 5500 < number1 <= 5750:
            number3 = '1700'
        elif 5250 < number1 <= 5500:
            number3 = '1824'
        elif 5000 < number1 <= 5250:
            number3 = '1947'
        elif 4750 < number1 <= 5000:
            number3 = '2070'
        elif 4500 < number1 <= 4750:
            number3 = '2194'
        elif 4250 < number1 <= 4500:
            number3 = '2317'
        elif 1000 <= number1 <= 4250:
            number3 = '2440'
        elif 750 <= number1 < 1000:
            number3 = '2289'
        elif 500 <= number1 < 750:
            number3 = '2137'
        elif 250 <= number1 < 500:
            number3 = '1986'
        elif 25 <= number1 < 250:
            number3 = '1834'
        elif 0 <= number1 < 25:
            number3 = ''
        else:
            number3 = ''
    elif number1 != '' and number2 == standard2:
        try:
            number1 = int(number1)
        except Exception as e:
            raise RuntimeError('本(临)线高度转换数值失败:{}'.format(number1))
        if 6550 < number1 <= 10000:
            number3 = ''
        elif 6200 < number1 <= 6550:
            number3 = '1220'
        elif 5500 < number1 <= 6200:
            number3 = '1700'
        elif 5250 < number1 <= 5500:
            number3 = '1700'
        elif 5000 < number1 <= 5250:
            number3 = '1700'
        elif 4750 < number1 <= 5000:
            number3 = '1850'
        elif 4500 < number1 <= 4750:
            number3 = '2000'
        elif 4250 < number1 <= 4500:
            number3 = '2074'
        elif 4000 < number1 <= 4250:
            number3 = '2147'
        elif 3750 < number1 <= 4000:
            number3 = '2220'
        elif 3500 < number1 <= 3750:
            number3 = '2294'
        elif 3250 < number1 <= 3500:
            number3 = '2367'
        elif 1100 <= number1 <= 3250:
            number3 = '2440'
        elif 350 <= number1 < 1100:
            number3 = '1875'
        elif 200 <= number1 < 350:
            number3 = '1725'
        elif 25 <= number1 < 200:
            number3 = '1500'
        elif 0 <= number1 < 25:
            number3 = ''
        else:
            number3 = ''
    else:
        pass
    return number3


# 求距本线或邻线以及是否超限
def distance_over_limit(number1, number2):
    special_str = ['大于3M', '大于3m', '大于3米', '大于三M', '大于三m', '大于三米', '>3M', '>3m', '>3米', '>三M',
                   '>三m', '>三米', '大于6M', '大于6m', '大于6米', '大于六M', '大于六m', '大于六米', '>6M', '>6m',
                   '>6米', '>六M', '>六m', '>六米', ]
    if number1 == '':
        distance = ''
        over_limit = ''
    elif number1 in special_str:
        distance = '正数'
        over_limit = '否'
    elif number1 != '' and number2 != '':
        try:
            number1_int = int(number1)
        except Exception as e:
            raise RuntimeError('距本(临)线转换数值失败:{}'.format(number1))
        try:
            number2_int = int(number2)
        except Exception as e:
            raise RuntimeError('本(临)线标准值转换数值失败:{}'.format(number2))
        distance = number1_int - number2_int
        if distance >= 0:
            over_limit = '否'
        else:
            over_limit = '是'
    else:
        distance = ''
        over_limit = ''
    return distance, over_limit


# 计算距离和是否超限
def calculation_line(data_list):
    """
    计算距离和是否超限
    :param data_list: [[],[]]
    :return:
    """
    need_len = 30
    for data in data_list:
        if len(data) == need_len:
            # 本线
            data[17] = calculation(data[6], data[25])
            # 邻线
            data[18] = calculation(data[9], data[25])

            # 距本线以及是否超限
            data[20], data[22] = distance_over_limit(data[7], data[17])

            # 距邻线以及是否超限
            data[21], data[23] = distance_over_limit(data[8], data[18])

            # 默认防撞墙
            if data[26] == '':
                data[26] = '无数据'
            # 重置一次本线超限
            elif data[26] == '有防撞墙' or data[26] == '低于轨面' or data[26] == '低于25mm':
                data[17] = ''
                data[18] = ''
                data[20] = ''
                data[21] = ''
                if data[6] != '':
                    data[22] = '否'
                else:
                    data[22] = '否'
                if data[9] != '':
                    data[23] = '否'
                else:
                    data[23] = '否'

            # 默认设备类型
            if data[27] == '':
                data[27] = '无数据'
        else:
            raise RuntimeError('数据长度不足{}:{}'.format(need_len, data))
    return data_list
