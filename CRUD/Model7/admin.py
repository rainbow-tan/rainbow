# Register your models here.
from django.contrib import admin

from Model7.models import ChangJia
from Model7.models import DangqianZhuangtai
from Model7.models import DataTable
from Model7.models import DiDian
from Model7.models import JiandingZhouqi
from Model7.models import JiliangQiju
from Model7.models import XianbieChejianChenzhan


@admin.register(DataTable)
class DataTableAdmin(admin.ModelAdmin):
    list_display = (
        'auto_id', 'xianbie', 'chejian', 'didian', 'zongcheng', 'mingcheng', 'bianhao', 'guige',
        'dengji', 'fanwei', 'changjia', 'zhuanye', 'fuzeren', 'riqi', 'xiaciriqi', 'zhouqi',
        'dangqianzhuangtai', 'yibiaozhuangtai', 'beizhu',
        )


@admin.register(XianbieChejianChenzhan)
class XianbieChejianChenzhanAdmin(admin.ModelAdmin):
    list_display = (
        'auto_id',
        'xianbie',
        'chejian',
        'chezhan'
        )


@admin.register(JiliangQiju)
class JiliangQijuAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'zongcheng')


@admin.register(JiandingZhouqi)
class JiandingZhouqiAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'zhouqi')


@admin.register(DiDian)
class DiDianAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'didian')


@admin.register(DangqianZhuangtai)
class DangqianZhuangtaiAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'dangqianzhuangtai')


@admin.register(ChangJia)
class ChangJiaAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'changjia')
