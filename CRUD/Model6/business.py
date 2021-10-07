# -*- encoding=utf-8 -*-
def qiuhe(data):
    """
    求和 ['1','2','3','',]
    返回['6','1','2','3','',]
    :param data:
    :return:
    """
    s = 0
    for i in data:
        if i != '':
            s = s + int(i)
    new = [str(s)] + data
    return new


def filter_data_for_xls(filter_data):
    pass
    all_data = []
    index = 1
    for one_obj in filter_data:
        one_data = list()
        one_data.append(index)
        one_data.append(one_obj.duanbie)
        one_data.append(one_obj.xianbie)
        one_data.append(one_obj.chejian)
        one_data.append(one_obj.chezhan)
        one_data.append(one_obj.genbanren)
        one_data.append(one_obj.gongqu)
        one_data.append(one_obj.zuoyeren)
        one_data.append(one_obj.renwuliang)
        one_data.append(one_obj.xiangmu)
        one_data.append(one_obj.fenlei)
        one_data.append(one_obj.yuefen)
        one_data.append(one_obj.gongzuoneirong)
        one_data.append(one_obj.zhouqi)
        one_data.append(one_obj.neirongshuoming)
        one_data.append(one_obj.danwei)
        one_data.append(one_obj.wanchengshuliang)
        one_data.append(one_obj.wanchengriqi)
        all_data.append(one_data)
        index += 1
    return all_data


def get_gongzuo_jidu(month):
    yuefen = ''
    for index, data in enumerate(month):
        if data.strip().lower() == 'on':
            yuefen += str(index + 1) + '-'
    yuefen = yuefen[0:len(yuefen) - 1]
    return yuefen


def split_qianduan_data(yuefen):
    yuefen_list = yuefen.split('-')[: - 1]
    return yuefen_list


def set_fenleis(yuefen, obj, fenlei):
    # 根据前端的月份和分类设置查询的分类
    if fenlei:
        fenleis = [fenlei]
    else:
        fenleis = []
        if yuefen:
            yuefen_list = split_qianduan_data(yuefen)
            for i in yuefen_list:
                if i in obj.yuefen.split('-'):
                    fenleis.append(obj.fenlei)
        else:
            fenleis.append(obj.fenlei)

    return fenleis
