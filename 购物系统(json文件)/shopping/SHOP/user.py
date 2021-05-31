# -*- coding: utf-8 -*-
import json
import os
import tkinter
from tkinter import *
from tkinter import messagebox

sys.path.append('../')
from COMMON.ReadJson import ReadJson
from COMMON.pub import *


def login():
    user = user_entry.get().strip()
    pwd = pwd_entry.get().strip()
    if user == '' or pwd == '':
        messagebox.showinfo('提示信息', '用户名或密码不能为空')
        return None

    obj = ReadJson(SHOP_INFO_FILE)
    users = list(obj.load_data().values())

    current_info = dict()
    for info in users:
        if user == info.get(SHOP_USER, '') and pwd == info.get(SHOP_PWD, ''):

            shop_user = info.get(SHOP_USER, '初始化用户')
            shop_pwd = info.get(SHOP_PWD, '初始化密码')
            shop_name = info.get(SHOP_NAME, '初始化店名')
            shop_address = info.get(SHOP_ADDRESS, '初始化店铺地址')
            shop_owner = info.get(SHOP_OWNER, '初始化店主')
            phone = info.get(PHONE, '初始化联系方式')
            shop_goods = info.get(SHOP_GOODS, {})
            goods_name = info.get(GOODS_NAME, '')
            goods_price = info.get(GOODS_PRICE, '')
            count = info.get(COUNT, '')

            current_info[SHOP_USER] = shop_user
            current_info[SHOP_PWD] = shop_pwd
            current_info[SHOP_NAME] = shop_name
            current_info[SHOP_ADDRESS] = shop_address
            current_info[SHOP_OWNER] = shop_owner
            current_info[PHONE] = phone
            current_info[SHOP_GOODS] = info.get(SHOP_GOODS)

            current_info[SHOP_GOODS] = shop_goods

            with open(CURRENT_SHOP_FILE, 'w', encoding='utf-8') as f:
                json.dump(current_info, f, indent=4, ensure_ascii=FALSE, )
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

    obj = ReadJson(SHOP_INFO_FILE)
    users = list(obj.load_data().values())

    for info in users:
        if user == info.get(SHOP_USER, ''):
            msg = '{}用户已经存在'.format(user)

            messagebox.showinfo('提示信息', msg)
            return None

    add_info = {
        SHOP_USER: user,
        SHOP_PWD: pwd,
        SHOP_NAME: user,
        SHOP_ADDRESS: '{}的地址'.format(user),
        SHOP_OWNER: user,
        PHONE: '{}的联系方式'.format(user),
        SHOP_GOODS: {}
        }
    users.append(add_info)

    new_user = dict()
    for index, one_user in enumerate(users):
        new_user[str(index + 1)] = one_user

    with open(SHOP_INFO_FILE, 'w', encoding='utf-8') as f:
        json.dump(new_user, f, indent=4, ensure_ascii=False)
    msg = '注册成功！！！'
    messagebox.showinfo('提示信息', msg)
    pass


if __name__ == '__main__':

    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    welcome_label = Label(window, text='店铺管理', font=('', FONT_SIZE_24))
    user_label = tkinter.Label(frame, text='用户名', font=('', FONT_SIZE_16), )
    pwd_label = tkinter.Label(frame, text='密码', font=('', FONT_SIZE_16), )
    login_btn = tkinter.Button(frame, text='登录', font=('', FONT_SIZE_16), command=login)
    register_btn = tkinter.Button(frame, text='注册', font=('', FONT_SIZE_16), command=register)
    user_entry = tkinter.Entry(frame)
    pwd_entry = tkinter.Entry(frame, show='*')
    pwd_entry.bind('<Return>', lambda x: login())
    user_entry.focus_set()

    welcome_label.pack(side=tkinter.TOP, padx=10, pady=40)
    frame.pack()

    user_label.grid(row=0, column=0, padx=10, pady=35)
    pwd_label.grid(row=1, column=0, padx=10, pady=35)
    user_entry.grid(row=0, column=1, padx=10, pady=35)
    pwd_entry.grid(row=1, column=1, padx=10, pady=35)
    login_btn.grid(row=2, column=0, padx=10, pady=35)
    register_btn.grid(row=2, column=1, padx=10, pady=35, sticky='e')

    window.title(SHOP_APP_TITLE)

    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    width = 500
    height = 500
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.resizable(0, 0)
    window.mainloop()
