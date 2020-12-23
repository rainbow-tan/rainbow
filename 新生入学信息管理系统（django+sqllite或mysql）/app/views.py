import json
from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from app.models import BasicInfo
from app.models import ExamArea
from app.models import Faculty
from app.models import Language
from app.models import Nationality
from app.models import Sex


def select_html(request):
    data = dict()

    # 前端数据
    select_number = request.GET.get('number', '')
    select_name = request.GET.get('name', '')
    select_sex = request.GET.get('sex', '')
    select_faculty = request.GET.get('faculty', '')
    select_class_name = request.GET.get('class_name', '')
    select_exam_area = request.GET.get('exam_area', '')
    select_into_date = request.GET.get('into_date', '')
    select_language = request.GET.get('language', '')
    select_nationality = request.GET.get('nationality', '')

    # 当前查询条件
    data['select_number'] = select_number
    data['select_name'] = select_name
    data['select_sex'] = select_sex
    data['select_faculty'] = select_faculty
    data['select_class_name'] = select_class_name
    data['select_exam_area'] = select_exam_area
    data['select_into_date'] = select_into_date
    data['select_language'] = select_language
    data['select_nationality'] = select_nationality

    # 下拉框
    data['faculty'] = Faculty.objects.values_list('name', flat=True)
    data['exam_area'] = ExamArea.objects.values_list('name', flat=True)
    data['language'] = Language.objects.values_list('name', flat=True)
    data['nationality'] = Nationality.objects.values_list('name', flat=True)
    data['sex'] = Sex.objects.values_list('name', flat=True)

    # 拼接查询条件
    q = Q()
    q.connector = 'AND'
    if select_number != '':
        q.children.append(('number', select_number))
    if select_name != '':
        q.children.append(('name', select_name))
    if select_sex != '':
        select_sex_obj = Sex.objects.filter(name=select_sex).first()
        q.children.append(('sex', select_sex_obj))
    if select_faculty != '':
        select_faculty_obj = Faculty.objects.filter(name=select_faculty).first()
        q.children.append(('faculty', select_faculty_obj))
    if select_class_name != '':
        q.children.append(('class_name', select_class_name))
    if select_exam_area != '':
        select_exam_area_obj = ExamArea.objects.filter(name=select_exam_area).first()
        q.children.append(('exam_area', select_exam_area_obj))
    if select_into_date != '':
        select_into_date_obj = datetime.strptime(select_into_date, '%Y-%m-%d')
        q.children.append(('into_date', select_into_date_obj))
    if select_language != '':
        select_language_obj = Language.objects.filter(name=select_language).first()
        q.children.append(('language', select_language_obj))
    if select_nationality != '':
        select_nationality_obj = Nationality.objects.filter(name=select_nationality).first()
        q.children.append(('nationality', select_nationality_obj))

    # 查询数据
    objects = BasicInfo.objects.filter(q)
    all_data = list()
    for one_object in objects:
        one_data = dict()
        one_data['number'] = one_object.number
        one_data['name'] = one_object.name
        one_data['sex'] = one_object.sex
        one_data['faculty'] = one_object.faculty
        one_data['class_name'] = one_object.class_name
        one_data['exam_area'] = one_object.exam_area
        one_data['into_date'] = one_object.into_date
        one_data['language'] = one_object.language
        one_data['birthday'] = one_object.birthday
        one_data['nationality'] = one_object.nationality
        one_data['grade'] = one_object.grade
        one_data['email'] = one_object.email
        all_data.append(one_data)
    data['objects'] = all_data

    return render(request, 'select.html', data)


def add_html(request):
    data = dict()
    data['faculty'] = Faculty.objects.values_list('name', flat=True)
    data['exam_area'] = ExamArea.objects.values_list('name', flat=True)
    data['language'] = Language.objects.values_list('name', flat=True)
    data['nationality'] = Nationality.objects.values_list('name', flat=True)
    data['sex'] = Sex.objects.values_list('name', flat=True)
    return render(request, 'add.html', data)


# 是否存在学号
def exist_number(request):
    ret = dict()
    exist = 'exist'
    number = request.GET['number']
    try:
        BasicInfo.objects.get(number=number)
        ret[exist] = True
    except Exception as e:
        ret[exist] = False
    return HttpResponse(json.dumps(ret), content_type="application/json")


def add(request):
    # 前端数据
    number = request.POST['number']
    name = request.POST['name']
    sex = request.POST['sex']
    faculty = request.POST['faculty']
    class_name = request.POST['class_name']
    exam_area = request.POST['exam_area']
    into_date = request.POST['into_date']
    language = request.POST['language']
    birthday = request.POST['birthday']
    nationality = request.POST['nationality']
    grade = request.POST['grade']
    email = request.POST['email']

    # 新增对象
    add_obj = BasicInfo()
    add_obj.number = number
    add_obj.name = name
    add_obj.sex = Sex.objects.filter(name=sex).first()
    add_obj.faculty = Faculty.objects.filter(name=faculty).first()
    add_obj.class_name = class_name
    add_obj.exam_area = ExamArea.objects.filter(name=exam_area).first()
    try:
        into_date = datetime.strptime(into_date, '%Y-%m-%d')
        add_obj.into_date = into_date
    except Exception as e:
        print('格式化入学时间失败:{}'.format(e))
    add_obj.language = Language.objects.filter(name=language).first()
    try:
        print('birthday:{}'.format(birthday))
        birthday = datetime.strptime(birthday, '%Y-%m-%d')
        add_obj.birthday = birthday
    except Exception as e:
        print('格式化出生年月失败:{}'.format(e))
    add_obj.nationality = Nationality.objects.filter(name=nationality).first()
    add_obj.grade = grade
    add_obj.email = email
    add_obj.save()

    return redirect('/select.html')


def update_html(request):
    data = dict()
    number = request.GET['number']
    obj = BasicInfo.objects.get(number=number)

    # 通过id查询数据
    data['current_number'] = obj.number
    data['current_name'] = obj.name
    data['current_sex'] = obj.sex
    data['current_faculty'] = obj.faculty
    data['current_class_name'] = obj.class_name
    data['current_exam_area'] = obj.exam_area
    data['current_into_date'] = str(obj.into_date)
    data['current_language'] = obj.language
    data['current_birthday'] = str(obj.birthday)
    data['current_nationality'] = obj.nationality
    data['current_grade'] = obj.grade
    data['current_email'] = obj.email

    # 下拉框
    data['faculty'] = Faculty.objects.values_list('name', flat=True)
    data['exam_area'] = ExamArea.objects.values_list('name', flat=True)
    data['language'] = Language.objects.values_list('name', flat=True)
    data['nationality'] = Nationality.objects.values_list('name', flat=True)
    data['sex'] = Sex.objects.values_list('name', flat=True)
    return render(request, 'update.html', data)


def update(request):
    # 前端数据
    number = request.POST['number']
    name = request.POST['name']
    sex = request.POST['sex']
    faculty = request.POST['faculty']
    class_name = request.POST['class_name']
    exam_area = request.POST['exam_area']
    into_date = request.POST['into_date']
    language = request.POST['language']
    birthday = request.POST['birthday']
    nationality = request.POST['nationality']
    grade = request.POST['grade']
    email = request.POST['email']

    update_obj = BasicInfo.objects.get(number=number)
    update_obj.name = name
    update_obj.sex = Sex.objects.filter(name=sex).first()
    update_obj.faculty = Faculty.objects.filter(name=faculty).first()
    update_obj.class_name = class_name
    update_obj.exam_area = ExamArea.objects.filter(name=exam_area).first()
    try:
        into_date = datetime.strptime(into_date, '%Y-%m-%d')
        update_obj.into_date = into_date
    except Exception as e:
        print('格式化入学时间失败:{}'.format(e))
    update_obj.language = Language.objects.filter(name=language).first()
    try:
        print('birthday:{}'.format(birthday))
        birthday = datetime.strptime(birthday, '%Y-%m-%d')
        update_obj.birthday = birthday
    except Exception as e:
        print('格式化出生年月失败:{}'.format(e))
    update_obj.nationality = Nationality.objects.filter(name=nationality).first()
    update_obj.grade = grade
    update_obj.email = email
    update_obj.save()

    return redirect('/select.html')


def delete(request):
    ids = request.GET['ids']
    ids = ids.split(',')
    ids.pop(len(ids) - 1)
    for remove_id in ids:
        BasicInfo.objects.get(number=remove_id).delete()
    return redirect('/select.html')
