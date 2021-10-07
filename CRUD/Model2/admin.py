# Register your models here.
from django.contrib import admin

from Model2.models import DataTable
from Model2.models import Field36Table
from Model2.models import Field37Table
from Model2.models import Field41Table
from Model2.models import Field42Table


@admin.register(DataTable)
class DataTableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field30', 'field1', 'field2', 'field23', 'field31', 'field32',
                    'field33', 'field3', 'field34', 'field35', 'field36', 'field37', 'field38',
                    'field39', 'field40', 'field41', 'field42', 'field43', 'field44', 'field45')


@admin.register(Field36Table)
class Field36TableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1')


@admin.register(Field37Table)
class Field37TableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1')


@admin.register(Field41Table)
class Field41TableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1')


@admin.register(Field42Table)
class Field42TableAdmin(admin.ModelAdmin):
    list_display = ('auto_id', 'field1')
