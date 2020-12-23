from django.contrib import admin

from app.models import BasicInfo
from app.models import ExamArea
from app.models import Faculty
from app.models import Language
from app.models import Nationality
from app.models import Sex


# 默认显示几个添加表单
# class BasicInfoInline(admin.StackedInline):
#     model = BasicInfo
#     extra = 3  # 添加学院的同时显示3个基础信息添加


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('number', 'name',)
    # inlines = [BasicInfoInline]


@admin.register(ExamArea)
class ExamAreaAdmin(admin.ModelAdmin):
    list_display = ('number', 'name',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('number', 'name',)


@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ('number', 'name',)


@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    list_display = ('number', 'name',)


@admin.register(BasicInfo)
class BasicInfoAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'name',
        'sex',
        'faculty',
        'class_name',
        'exam_area',
        'into_date',
        'language',
        'birthday',
        'nationality',
        'grade',
        'email',)
    list_filter = ['sex', ]  # 过滤
    search_fields = ['name', 'number', 'birthday', 'grade']
