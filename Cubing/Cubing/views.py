from django.shortcuts import redirect
from django.shortcuts import render

from Cubing import Business
from Cubing import Pub


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
    admin_user = ['admin', '胡明']
    delete_users = ['胡明', "刘洋"]
    update_readonly = ['root', '胡明', "刘洋"]
    can_login = False
    for usr in Business.user_dict:
        if username == usr.get(Business.USER) and password == usr.get(Business.PASSWORD):
            can_login = True
            break
    if can_login is True:
        response = redirect('/index.html')
        if username in admin_user:
            response.set_cookie("is_admin", True)
        if username in delete_users:
            response.set_cookie("can_delete", True)
        if username in update_readonly:
            response.set_cookie("only1", True)

        response.set_cookie("is_login", True)
        response.set_cookie("user", username)
        return response
    else:
        return render(request, 'login.html', {'msg': '用户名密码错误'})


def debug(request):
    return render(request, 'debug.html')
