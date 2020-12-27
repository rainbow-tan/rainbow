from django.db.models import Q

USER = 'user'
PASSWORD = 'password'
# 用户密码
user_dict = [{USER: 'admin', PASSWORD: '17012'}, {USER: '龙进', PASSWORD: '27493'},
             {USER: '冯显伟', PASSWORD: '15794'}, {USER: '周帆弋', PASSWORD: '15018'},
             {USER: '赵建彪', PASSWORD: '15414'}, {USER: '杨博凯', PASSWORD: '18332'},
             {USER: '彭李兴', PASSWORD: '18307'}, {USER: '杨敏', PASSWORD: '16242'},
             {USER: '郭众', PASSWORD: '18342'}, {USER: '吴小亮', PASSWORD: '13257'},
             {USER: '佟喜东', PASSWORD: '18343'}, {USER: '罗友', PASSWORD: '14924'},
             {USER: '胡博', PASSWORD: '18338'}, {USER: '刘洋', PASSWORD: '18328'},
             {USER: '潘怀良', PASSWORD: '15031'}, {USER: '陈旭', PASSWORD: '16970'},
             {USER: '叶亮', PASSWORD: '17531'}, {USER: '李思勇', PASSWORD: '123'},
             {USER: '许昭旭', PASSWORD: '123'}, {USER: '孙德臣', PASSWORD: '123'},
             {USER: 'root', PASSWORD: 'root'}, {USER: '胡明', PASSWORD: '17012'}]
# 特殊零件号
special_part_number = ['17G 819 728A', '17G 858 019A', '17G 819 728A', '17G 867 501 C', '17G 868 007']


# 导出报废清单数据
def scarp_data(data):
    new = []
    for i, ii in enumerate(data):
        new_data = [str(i + 1)]
        for j, k in enumerate(ii):
            if j == 4:
                new_data.append('1')
            new_data.append(k)
        new.append(new_data)
    return new


# 移除二维码，用于写入表格
def yichu_erweima(data):
    new = []
    for i in data:
        one = []
        for j, k in enumerate(i):
            if j != 0:
                one.append(k)
        new.append(one)
    return new


# 查询没有报废的数据
def select_no_baofei(table_name, connector, select_conditions, column_names):
    q = Q()
    q.connector = connector
    for select_key, select_value in select_conditions.items():
        if select_value != '':
            q.children.append((select_key, select_value))
    q.children.append(('deal_mode', ''))
    select_data = table_name.objects.filter(q).order_by('-receive_date')
    all_data = []
    for data in select_data:
        one_data = list()
        for column_name in column_names:
            one_data.append(data.__dict__[column_name])
        all_data.append(one_data)
    return all_data
