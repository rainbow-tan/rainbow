# -*- encoding=utf-8 -*-


def calculation(field6, field25):
    """
    计算本线,邻线
    :param field6: 空串或者能数字
    :param field25: 高铁标准/普铁标准
    :return:
    """
    field16 = ''
    if field6 != '' and field25 != '':
        if field25 == '高铁标准':
            if 7250 < field6 <= 100000:
                field16 = ''
            if 7000 < field6 <= 7250:
                field16 = '800'
            if 6750 < field6 <= 7000:
                field16 = '950'
            if 6500 < field6 <= 6750:
                field16 = '1100'
            if 6250 < field6 <= 6500:
                field16 = '1250'
            if 6000 < field6 <= 6250:
                field16 = '1400'
            if 5750 < field6 <= 6000:
                field16 = '1550'
            if 5500 < field6 <= 5750:
                field16 = '1700'
            if 5250 < field6 <= 5500:
                field16 = '1824'
            if 5000 < field6 <= 5250:
                field16 = '1947'
            if 4750 < field6 <= 5000:
                field16 = '2070'
            if 4500 < field6 <= 4750:
                field16 = '2194'
            if 4250 < field6 <= 4500:
                field16 = '2317'
            if 1000 <= field6 <= 4250:
                field16 = '2440'
            if 750 <= field6 < 1000:
                field16 = '2289'
            if 500 <= field6 < 750:
                field16 = '2137'
            if 250 <= field6 < 500:
                field16 = '1986'
            if 25 <= field6 < 250:
                field16 = '1834'
            if 0 <= field6 < 25:
                field16 = ''
        if field25 == '普铁标准':
            if 6550 < field6 <= 10000:
                field16 = ''
            if 6200 < field6 <= 6550:
                field16 = '1220'
            if 5500 < field6 <= 6200:
                field16 = '1700'
            if 5250 < field6 <= 5500:
                field16 = '1700'
            if 5000 < field6 <= 5250:
                field16 = '1700'
            if 4750 < field6 <= 5000:
                field16 = '1850'
            if 4500 < field6 <= 4750:
                field16 = '2000'
            if 4250 < field6 <= 4500:
                field16 = '2074'
            if 4000 < field6 <= 4250:
                field16 = '2147'
            if 3750 < field6 <= 4000:
                field16 = '2220'
            if 3500 < field6 <= 3750:
                field16 = '2294'
            if 3250 < field6 <= 3500:
                field16 = '2367'
            if 1100 <= field6 <= 3250:
                field16 = '2440'
            if 350 <= field6 < 1100:
                field16 = '1875'
            if 200 <= field6 < 350:
                field16 = '1725'
            if 25 <= field6 < 200:
                field16 = '1500'
            if 0 <= field6 < 25:
                field16 = ''
    return field16


def calculation_line(data_list):
    """
    计算距离和是否超限
    :param data_list: [[],[]]
    :return:
    """
    for data in data_list:
        if len(data) > 22:
            data[16] = calculation(data[6], data[25])
            data[17] = calculation(data[9], data[25])
            if (data[7] == '大于3米' or data[7] == '大于3M' or data[7] == '>3米' or
                    data[7] == '>3M' or data[7] == '大于三米' or data[
                        7] == '大于三M' or data[7] == '>三M' or data[7] == '大于三M'):
                data[19] = '正数'
                data[21] = '否'
            else:
                if data[7] != '' and data[16] != '':
                    data[19] = int(data[7]) - int(data[16])
                    if data[19] > 0:
                        data[21] = '否'
                    else:
                        data[21] = '是'

            if (data[8] == '大于3米' or data[8] == '大于3M' or data[8] == '>3米' or
                    data[8] == '>3M' or
                    data[8] == '大于三米' or data[8] == '大于三M' or data[
                        7] == '>三M' or data[8] == '大于三M'):
                data[20] = '正数'
                data[22] = '否'
            else:
                if data[8] != '' and data[16] != '':
                    data[20] = int(data[8]) - int(data[16])
                    if data[20] > 0:
                        data[22] = '否'
                    else:
                        data[22] = '是'

        else:
            print('数据错误')
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
