# -*- coding: utf-8 -*-
import os
import tkinter
from tkinter import *
from tkinter import messagebox

sys.path.append('../')
from COMMON import MyFile

from COMMON.ReadJson import ReadJson
from COMMON.pub import *


def login():
    user = user_entry.get().strip()
    pwd = pwd_entry.get().strip()
    if user == '' or pwd == '':
        messagebox.showinfo('提示信息', '用户名或密码不能为空')
        return None
    ##print('登录用户名:{}'.format(user))
    ##print('登录密码:{}'.format(pwd))
    obj = ReadJson(USER_INFO_FILE)
    users = list(obj.load_data().values())
    ##print("用户信息:{}".format(users))
    current_user = dict()
    for info in users:
        if user == info.get(CUSTOMER_USER, '') and pwd == info.get(PWD, ''):
            ##print('{}用户可以登录'.format(user))
            name = info.get(NAME)
            sex = info.get(SEX)
            pwd = info.get(PWD)
            user_contact = info.get(USER_CONTACT)
            user_address = info.get(USER_ADDRESS)
            current_user[NAME] = name
            current_user[SEX] = sex
            current_user[CUSTOMER_USER] = user
            current_user[PWD] = pwd
            current_user[USER_CONTACT] = user_contact
            current_user[USER_ADDRESS] = user_address
            ##print('当前用户:{}'.format(current_user))
            MyFile.write_file(CURRENT_USER_FILE, current_user)
            # with open(CURRENT_USER_FILE, 'w', encoding='utf-8') as f:
            #     json.dump(current_user, f, ensure_ascii=FALSE, )
            window.destroy()
            os.system('python choose.py')
            return None
    messagebox.showinfo('提示信息', '用户名或密码错误')
    return None


def register():
    user = user_entry.get().strip()
    pwd = pwd_entry.get().strip()
    if user == '' or pwd == '':
        messagebox.showinfo('提示信息', '用户名或密码不能为空')
        return None
    ##print('注册用户名:{}'.format(user))
    ##print('注册密码:{}'.format(pwd))
    obj = ReadJson(USER_INFO_FILE)
    users = list(obj.load_data().values())
    ##print("用户信息:{}".format(users))
    for info in users:
        if user == info.get(CUSTOMER_USER, ''):
            msg = '({})用户已经存在'.format(user)
            ##print(msg)
            messagebox.showinfo('提示信息', msg)
            return None

    add_info = {
        CUSTOMER_USER: user, PWD: pwd,
        NAME: '{}的姓名'.format(user),
        SEX: '未知',
        USER_CONTACT: '{}的联系方式'.format(user),
        USER_ADDRESS: '{}的地址'.format(user)
        }
    users.append(add_info)

    new_user = dict()
    for index, one_user in enumerate(users):
        new_user[str(index + 1)] = one_user
    ##print('添加后的用户组:{}'.format(new_user))
    MyFile.write_file(USER_INFO_FILE, new_user)
    # with open(USER_INFO_FILE, 'w', encoding='utf-8') as f:
    #     json.dump(new_user, f, ensure_ascii=False)
    msg = '注册成功！！！'
    messagebox.showinfo('提示信息', msg)
    pass


if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    welcome_label = Label(window, text='欢迎使用', font=('', FONT_SIZE_24))
    user_label = tkinter.Label(frame, text='用户名', font=('', FONT_SIZE_16), )
    pwd_label = tkinter.Label(frame, text='密码', font=('', FONT_SIZE_16), )
    login_btn = tkinter.Button(frame, text='登录', command=login, font=('', FONT_SIZE_16), )
    register_btn = tkinter.Button(frame, text='注册', command=register, font=('', FONT_SIZE_16), )
    user_entry = tkinter.Entry(frame)
    user_entry.focus_set()
    pwd_entry = tkinter.Entry(frame, show='*')
    padx = 10
    pady = 35
    welcome_label.pack(side=tkinter.TOP, padx=padx, pady=40)
    frame.pack()

    user_label.grid(row=0, column=0, padx=padx, pady=pady)
    pwd_label.grid(row=1, column=0, padx=padx, pady=pady)
    user_entry.grid(row=0, column=1, padx=padx, pady=pady)
    pwd_entry.grid(row=1, column=1, padx=padx, pady=pady)
    login_btn.grid(row=2, column=0, padx=padx, pady=pady)
    register_btn.grid(row=2, column=1, padx=padx, pady=pady, sticky='e')

    window.title(CUSTOMER_APP_TITLE)

    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    width = 500
    height = 500
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.resizable(0, 0)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
