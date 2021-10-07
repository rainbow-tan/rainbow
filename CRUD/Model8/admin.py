# Register your models here.
from django.contrib import admin

from Model8.models import DataTable
from Model8.models import QuDuanTable


@admin.register(DataTable)
class DataTableAdmin(admin.ModelAdmin):
    list_display = (
        'auto_id', 'wentiriqi', 'xianbie', 'chejian', 'chezhan', 'quduan', 'buliangdianrong',
        'hangbie',
        'dianrongshuliang', 'zaiping', 'chuliriqi', 'yuanying', 'chuliqingkuang',
        'shangbaoqingkuang', 'zhouqi', 'beizhu', 'qiandianliu', 'houdianliu', 'qiandianya',
        'houdianya', 'qiandianrong',
        'houdianrong', 'changjia', 'shiyongshijian', 'fankuiren',
        )


@admin.register(QuDuanTable)
class QuDuanTableAdmin(admin.ModelAdmin):
    list_display = ['auto_id', 'xianbie', 'chezhan', 'quduan', 'zaiping', 'dianrongshuliang',
                    'hangbie', 'quduanchangdu', ]
