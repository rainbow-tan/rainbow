# Register your models here.
from django.contrib import admin

from Model4.models import DataTable


@admin.register(DataTable)
class DataTableAdmin(admin.ModelAdmin):
    list_display = ['auto_id', 'field1', 'field2', 'field3', 'field48', 'field37', 'field50',
                    'field54',
                    'field85', 'field86', 'field87', 'field88', 'field89', 'field90', 'field91',
                    'field92', 'field93', 'field94', 'field95', 'field96', 'field97', 'field98',
                    'field99', 'field100', 'field101', 'field102', 'field103', 'field104',
                    'field105',
                    'field106', 'field107', 'field108', 'field109', 'field110', ]
