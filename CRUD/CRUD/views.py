from django.shortcuts import render, redirect

from CRUD import Pub
from Model.models import Field1Table
from Model.models import Field23Table
from Model.models import Field24Table
from Model.models import Field25Table
from Model.models import Field26Table
from Model.models import Field27Table
from Model.models import Field2Table
from Model.models import Field3Table
from Model2.models import Field37Table
from Model2.models import Field41Table
from Model2.models import Field42Table
from Model3.models import Field71Table


def index_html(request):
    Pub.delete_folder(Pub.IMPORT_FOLDER, Pub.SAVE_FOLDER_SIZE)
    Pub.delete_folder(Pub.EXPORT_FOLDER, Pub.SAVE_FOLDER_SIZE)
    return render(request, 'index.html')


def login_html(request):
    return render(request, 'login.html')


def debug_html(request):
    return render(request, 'debug.html')


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    if username == 'admin' and password == 'admin':
        response = redirect("/index.html/")
        response.set_cookie("is_login", True)
        response.set_cookie("is_admin", True)
    elif username == 'root' and password == 'root':
        response = redirect("/index.html/")
        response.set_cookie("is_login", True)
        response.set_cookie("is_admin", False)
    else:
        response = redirect("/login.html/")
        response.set_cookie("is_login", False)
    return response


def debug(request):
    return render(request, 'debug.html')


def init_db():
    xianbie = ['沈大高铁', '新通客专', '喀赤客专', '沈丹客专', '盘营客专', '京哈高铁', '朝凌客专', ]
    for i in xianbie:
        Field1Table(field1='{}'.format(i.strip())).save()
    zonghechejian = ['牛河梁', '朝阳', '阜新', '沈阳南', '鞍山西', '营口东', '彰武', '宁城', '凤城东', '瓦房店西', ]
    for i in zonghechejian:
        Field2Table(field1='{}'.format(i.strip())).save()
    qujianmingchen = ['京哈中继13',
                      '京哈中继14',
                      '京哈中继15',
                      '京哈中继16',
                      '京哈牛河梁',
                      '京哈中继17',
                      '孙家沟线路所',
                      '喀左',
                      '京哈中继18',
                      '京哈中继19',
                      '奈林皋',
                      '京哈中继20',
                      '京哈中继21',
                      '朝阳',
                      '京哈中继22',
                      '京哈中继23',
                      '北票',
                      '京哈中继24',
                      '京哈中继25',
                      '京哈中继26',
                      '乌兰木图',
                      '京哈中继27',
                      '京哈中继28',
                      '阜新',
                      '京哈中继29',
                      '京哈中继30',
                      '京哈中继31',
                      '黑山北',
                      '京哈中继32',
                      '京哈中继33',
                      '姚家窝铺线路所',
                      '新民北',
                      '沈阳西',
                      '京哈中继34',
                      '京哈中继35',
                      '田家窝铺线路所',
                      '新通中继1',
                      '新通中继2',
                      '彰武',
                      '新通中继3',
                      '章古台',
                      '新通中继4',
                      '甘旗卡',
                      '新通中继5',
                      '新通中继6',
                      '新通中继7',
                      '木里图',
                      '通辽高速场',
                      '沈大中继1',
                      '沈大中继2',
                      '普湾',
                      '沈大中继3',
                      '沈大中继4',
                      '瓦房店西',
                      '沈大中继5',
                      '沈大中继6',
                      '沈大中继7',
                      '沈大中继8',
                      '鲅鱼圈',
                      '沈大中继9#',
                      '盖州西',
                      '沈大中继10',
                      '营口东',
                      '沈大中继11',
                      '下夹河线路所',
                      '海城西',
                      '沈大中继12',
                      '沈大中继13',
                      '鞍山西',
                      '沈大中继14',
                      '盘营中继1',
                      '盘锦高速场',
                      '盘营中继2',
                      '盘营中继3',
                      '盘营中继4',
                      '中小线路所',
                      '辽阳高速场',
                      '沈大中继15',
                      '沈大中继16',
                      '沈大中继17',
                      '沈阳南',
                      '沙河堡线路所',
                      '沈丹中继1',
                      '本溪新城',
                      '沈丹中继2',
                      '沈丹中继3',
                      '南芬北',
                      '本溪客车场',
                      '沈丹中继4',
                      '通远堡西',
                      '沈丹中继5',
                      '凤城东',
                      '沈丹中继6',
                      '五龙背东',
                      '沈南动车所',
                      '沈北动车所',
                      '通辽动车所',
                      '郑仗子线路所',
                      '建平',
                      '喀赤中继1',
                      '喀赤中继2',
                      '喀赤宁城',
                      '喀赤中继3',
                      '喀赤中继4',
                      '平庄',
                      '喀赤中继5',
                      '喀赤中继6',
                      '赤峰高速场', ]
    for i in qujianmingchen:
        Field3Table(field1=i.strip()).save()
    hangbie = ['上行', '下行']
    for i in hangbie:
        Field23Table(field1=i).save()
    zhanneiqujian = ['站内', '区间']
    for i in zhanneiqujian:
        Field24Table(field1=i).save()
    cankaobiaozhun = ['高铁标准', '普铁标准']
    for i in cankaobiaozhun:
        Field25Table(field1=i).save()
    fangzhuangqiang = ['有防撞墙',
                       '无防撞强',
                       '无数据',
                       '低于轨面',
                       '低于25mm',
                       ]
    for i in fangzhuangqiang:
        Field26Table(field1=i.strip()).save()
    shebenleixing = ['进站信号机',
                     '出站信号机',
                     '调车信号机',
                     'ZDJ9型道岔',
                     'ZD6型道岔',
                     '扼流变压器',
                     '电热融雪箱',
                     '电缆盒',
                     '绝缘破损防护TB',
                     '调谐匹配单元',
                     '空心线圈',
                     '信号标志牌',
                     '器材XB箱',
                     '其它',
                     'LEU箱',
                     '无数据',
                     ]
    for i in shebenleixing:
        Field27Table(field1=i.strip()).save()
    biaochenzaiping = ['1700-1',
                       '2000-1',
                       '2300-1',
                       '2600-1',
                       '1700-2',
                       '2000-2',
                       '2300-2',
                       '2600-2']
    for i in biaochenzaiping:
        Field37Table(field1=i.strip()).save()
    rongxuxinhao = ['是', '否']
    for i in rongxuxinhao:
        Field41Table(field1=i.strip()).save()
    fanxiandianlu = ['二线', '四线']
    for i in fanxiandianlu:
        Field42Table(field1=i.strip()).save()
    guidaoleixing = ['无砟桥梁', '无砟路基', '特殊区段(7.5KM)', '有砟路基', '无砟桥梁(站内)', '无砟路基(站内)', '站内道岔区段',
                     '特殊区段(10KM)', '股道区段',
                     '有砟T梁桥', '有砟箱梁桥']
    for i in guidaoleixing:
        Field71Table(field1=i.strip()).save()
