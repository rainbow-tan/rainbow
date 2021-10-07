from django.contrib import admin

from Model5.models import Luruye
from Model5.models import XiangMu
from Model5.models import ZhuYe


@admin.register(Luruye)
class LuruyeAdmin(admin.ModelAdmin):
    list_display = (
        'auto_id',
        'duanbie',
        'xianbie',
        'chejian',
        'chezhan',
        'genbanren',
        'gongqu',
        'zuoyeren',
        'renwuliang',
        'xiangmu',
        'fenlei',
        'yuefen',
        'gongzuoneirong',
        'zhouqi',
        'neirongshuoming',
        'danwei',
        'wanchengshuliang',
        'wanchengriqi',

        )
    # list_filter = ['chejian', ]  # 过滤
    search_fields = ['chejian', ]


@admin.register(ZhuYe)
class ZhuYeAdmin(admin.ModelAdmin):
    list_display = (
        'auto_id',
        'xiangmu',
        'fenlei',
        'yuefen',
        'zhouqi',
        'neirongshuoming',
        'danwei',
        'renwuliang',
        'benyuewanchen',
        'leijiwanchen',
        'xianbie',
        'chejian',
        'chezhan',
        'create_time',
        )
    # list_filter = ['chejian', ]  # 过滤
    # search_fields = ['chejian', ]


@admin.register(XiangMu)
class XiangMuAdmin(admin.ModelAdmin):
    list_display = (
        'auto_id',
        'xiangmu',
        'fenlei',
        'yuefen',
        'zhouqi',
        'neirongshuoming',
        'danwei',
        )
