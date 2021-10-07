# Register your models here.
from django.contrib import admin

from Model.models import DataTable
from Model.models import Field1Table
from Model.models import Field23Table
from Model.models import Field24Table
from Model.models import Field25Table
from Model.models import Field26Table
from Model.models import Field27Table
from Model.models import Field2Table
from Model.models import Field3Table


@admin.register(DataTable)
class DataTableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1', 'field2', 'field3', 'field4', 'field5',
                    'field6', 'field7', 'field8', 'field9', 'field70', 'field10', 'field11',
                    'field12', 'field13', 'field14', 'field15', 'field16', 'field17',
                    'field18', 'field19', 'field20', 'field21', 'field22',
                    'field24', 'field25', 'field26', 'field27', 'field28', 'field29',)


@admin.register(Field1Table)
class Field1TableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1')


@admin.register(Field2Table)
class Field2TableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1')


@admin.register(Field3Table)
class Field3TableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1')


@admin.register(Field23Table)
class Field23TableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1')


@admin.register(Field24Table)
class Field24TableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1')


@admin.register(Field25Table)
class Field25TableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1')


@admin.register(Field26Table)
class Field26TableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1')


@admin.register(Field27Table)
class Field27TableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1')
