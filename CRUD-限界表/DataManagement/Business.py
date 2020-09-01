# -*- encoding=utf-8 -*-


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
        number1 = int(number1)
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
        number1 = int(number1)
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


def distance_over_limit(number1, number2):
    """
    求距本线或邻线以及是否超限
    :param number1:
    :param number2:
    :return:
    """
    special_str = ['大于3M', '大于3m', '大于3米', '大于三M', '大于三m', '大于三米', '>3M', '>3m', '>3米', '>三M',
                   '>三m', '>三米', '大于6M', '大于6m', '大于6米', '大于六M', '大于六m', '大于六米', '>6M', '>6m',
                   '>6米', '>六M', '>六m', '>六米', ]
    number3 = ''
    over_limit = ''
    if number1 in special_str:
        number3 = '正数'
        over_limit = '否'
    else:
        if number1 != '' and number2 != '':
            number3 = int(number1) - int(number2)
            if number3 > 0:
                over_limit = '否'
            else:
                over_limit = '是'
    return number3, over_limit


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
            data[16] = calculation(data[6], data[25])
            # 邻线
            data[17] = calculation(data[9], data[25])

            # 距本线以及是否超限
            data[19], data[21] = distance_over_limit(data[7], data[16])

            # 距邻线以及是否超限
            data[20], data[22] = distance_over_limit(data[8], data[17])

            # 默认防撞墙
            if data[26] == '':
                data[26] = '无防撞墙'

            # 默认设备类型
            if data[27] == '':
                data[27] = '其它'

            # float转为int
            try:
                data[6] = int(data[6])
                data[7] = int(data[7])
                data[8] = int(data[8])
                data[9] = int(data[9])
            except Exception as e:
                pass
        else:
            print('数据长度不足{}:{}'.format(need_len, data))
    return data_list


def pop_first(data_list):
    """
    移除第一个元素(顺号)
    :param data_list: [['47','b1',','c'],['12','b2',','c'],['1','b3',','c']]
    :return: [['b1',','c'],['b2',','c'],['b3',','c']]
    """
    new_data_list = []
    for data in data_list:
        one_data = []
        for i, j in enumerate(data):
            if i != 0:
                one_data.append(j)
        new_data_list.append(one_data)
    return new_data_list
