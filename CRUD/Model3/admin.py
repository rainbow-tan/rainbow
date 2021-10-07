# Register your models here.
from django.contrib import admin

from Model3.models import DataTable
from Model3.models import Field71Table


@admin.register(DataTable)
class DataTableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1', 'field2', 'field3',
                    'field24',
                    'field23', 'field46', 'field47', 'field48',
                    'field49',
                    'field37', 'field50', 'field51', 'field52',
                    'field53',
                    'field54', 'field55', 'field56', 'field57',
                    'field58',
                    'field59', 'field60', 'field61', 'field62',
                    'field71',
                    'field72', 'field73', 'field74', 'field75',
                    'field76',
                    'field77', 'field78', 'field79', 'field80',
                    'field81',
                    'field82', 'field83', 'field84', 'field63',
                    'field64', 'field65', 'field66', 'field67',
                    'field68',
                    'field69',)


@admin.register(Field71Table)
class Field71TableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1', 'changdu')
