# -*- coding: utf-8 -*-
import json
import os
import tkinter
from tkinter import *
from tkinter import messagebox

sys.path.append('../')
from COMMON.ReadJson import ReadJson
from COMMON.pub import CURRENT_SHOP_FILE
from COMMON.pub import FONT_SIZE_16
from COMMON.pub import FONT_SIZE_24
from COMMON.pub import PHONE
from COMMON.pub import SHOP_ADDRESS
from COMMON.pub import SHOP_INFO_FILE
from COMMON.pub import SHOP_NAME
from COMMON.pub import SHOP_OWNER
from COMMON.pub import SHOP_PWD
from COMMON.pub import SHOP_USER
from COMMON.pub import SHOP_APP_TITLE
from COMMON.pub import SHOP_GOODS


def return_btn_event():
    # print('返回个人信息')
    window.destroy()
    os.system('python myself.py')
    pass


def update_btn_event():
    # print('修改个人信息')
    my_json = ReadJson(CURRENT_SHOP_FILE)
    current_user = my_json.load_data()
    old_account = current_user.get(SHOP_USER, '')
    old_shop_name = current_user.get(SHOP_NAME, '')
    old_shop_goods = current_user.get(SHOP_GOODS, {})
    # print('老商品:{}'.format(old_shop_goods))
    # print('老店名:{}'.format(old_shop_name))
    new_shop_user = shop_user_label2.get()
    new_shop_pwd = shop_pwd_label2.get()
    new_shop_name = shop_name_label2.get()
    new_shop_address = shop_address_label2.get()
    new_shop_owner = shop_owner_label2.get()
    new_phone = phone_label2.get()

    my_json2 = ReadJson(SHOP_INFO_FILE)
    users = list(my_json2.load_data().values())
    # print("用户信息:{}".format(users))
    old_users = []
    for i in users:
        old_users.append(i.get(SHOP_USER, ''))
    # print('原有的用户:{}'.format(old_users))
    old_users.pop(old_users.index(old_account))
    for i in users:
        if i.get(SHOP_USER, '') == old_account:
            users.pop(users.index(i))
    # print('剔除当前用户后:{}'.format(old_users))
    # print('剔除当前用户后2:{}'.format(users))

    if new_shop_user in old_users:
        messagebox.showinfo('提示', '该账号已存在')
        return

    source_shop_names = []
    for i in users:
        if i.get(SHOP_NAME, '') != old_shop_name:
            source_shop_names.append(i.get(SHOP_NAME, ''))
        else:
            pass
            # print('剔除旧店名:{}'.format(i.get(SHOP_NAME, '')))
    # print('原有的店名')
    # print(source_shop_names)

    if new_shop_name in source_shop_names:
        msg = '店名（{}）已经存在'.format(new_shop_name)
        messagebox.showinfo('提示信息', msg)
        return None

    new_info = dict()
    new_info[SHOP_NAME] = new_shop_name
    new_info[SHOP_ADDRESS] = new_shop_address
    new_info[SHOP_OWNER] = new_shop_owner
    new_info[PHONE] = new_phone
    new_info[SHOP_USER] = new_shop_user
    new_info[SHOP_PWD] = new_shop_pwd
    new_info[SHOP_GOODS] = old_shop_goods
    # print("修改后的信息:{}".format(new_info))
    with open(CURRENT_SHOP_FILE, 'w', encoding='utf-8') as f:
        json.dump(new_info, f, indent=4, ensure_ascii=False)
    new_user = dict()
    users.append(new_info)
    for index, one_user in enumerate(users):
        new_user[str(index + 1)] = one_user
    # print('添加后的用户组:{}'.format(new_user))

    with open(SHOP_INFO_FILE, 'w', encoding='utf-8') as f:
        json.dump(new_user, f, indent=4, ensure_ascii=False)
    # msg = '修改店铺信息成功！！！'
    # messagebox.showinfo('提示信息', msg)
    return_btn_event()
    pass


if __name__ == '__main__':

    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    myself_label = Label(window, text='个人信息', font=('', FONT_SIZE_24))
    shop_name_label = tkinter.Label(frame, text='店铺名称:', fg='blue', font=('', FONT_SIZE_16), )
    shop_address_label = tkinter.Label(frame, text='店铺地址:', fg='blue', font=('', FONT_SIZE_16))
    shop_owner_label = tkinter.Label(frame, text='店主姓名:', fg='blue', font=('', FONT_SIZE_16))
    phone_label = tkinter.Label(frame, text='联系方式:', fg='blue', font=('', FONT_SIZE_16))
    shop_user_label = tkinter.Label(frame, text='账号:', fg='blue', font=('', FONT_SIZE_16))
    shop_pwd_label = tkinter.Label(frame, text='密码:', fg='blue', font=('', FONT_SIZE_16))

    obj = ReadJson(CURRENT_SHOP_FILE)
    data = obj.load_data()
    shop_user = data.get(SHOP_USER, '初始化用户')
    shop_pwd = data.get(SHOP_PWD, '初始化密码')
    shop_name = data.get(SHOP_NAME, '初始化店铺名称')
    shop_address = data.get(SHOP_ADDRESS, '初始化店铺地址')
    shop_owner = data.get(SHOP_OWNER, '初始化店主')
    phone = data.get(PHONE, '初始化联系方式')

    shop_user1 = tkinter.StringVar()
    shop_user1.set(shop_user)

    shop_pwd1 = tkinter.StringVar()
    shop_pwd1.set(shop_pwd)
    shop_name1 = tkinter.StringVar()
    shop_name1.set(shop_name)
    shop_address1 = tkinter.StringVar()
    shop_address1.set(shop_address)
    shop_owner1 = tkinter.StringVar()
    shop_owner1.set(shop_owner)
    phone1 = tkinter.StringVar()
    phone1.set(phone)

    shop_name_label2 = tkinter.Entry(frame, font=('', FONT_SIZE_16), text=shop_name1)

    shop_address_label2 = tkinter.Entry(frame, font=('', FONT_SIZE_16), text=shop_address1)
    shop_owner_label2 = tkinter.Entry(frame, font=('', FONT_SIZE_16), text=shop_owner1)
    phone_label2 = tkinter.Entry(frame, font=('', FONT_SIZE_16), text=phone1)
    shop_user_label2 = tkinter.Entry(frame, font=('', FONT_SIZE_16), text=shop_user1)
    shop_pwd_label2 = tkinter.Entry(frame, font=('', FONT_SIZE_16), text=shop_pwd1)

    return_btn = tkinter.Button(frame, text='返回', font=('', FONT_SIZE_16), command=return_btn_event)
    update_btn = tkinter.Button(frame, text='修改', font=('', FONT_SIZE_16), command=update_btn_event)

    myself_label.pack(side=tkinter.TOP, padx=10, pady=40)
    frame.pack()
    padx = 30
    pady = 20
    shop_user_label.grid(row=0, column=0, padx=padx, pady=pady)

    shop_pwd_label.grid(row=1, column=0, padx=padx, pady=pady)
    shop_name_label.grid(row=2, column=0, padx=padx, pady=pady)
    shop_address_label.grid(row=3, column=0, padx=padx, pady=pady)
    shop_owner_label.grid(row=4, column=0, padx=padx, pady=pady)
    phone_label.grid(row=5, column=0, padx=padx, pady=pady)

    shop_user_label2.grid(row=0, column=1, padx=padx, pady=pady)
    shop_pwd_label2.grid(row=1, column=1, padx=padx, pady=pady)
    shop_name_label2.grid(row=2, column=1, padx=padx, pady=pady)
    shop_user_label2.config(state='readonly')
    shop_address_label2.grid(row=3, column=1, padx=padx, pady=pady)
    shop_owner_label2.grid(row=4, column=1, padx=padx, pady=pady)
    phone_label2.grid(row=5, column=1, padx=padx, pady=pady)
    update_btn.grid(row=6, column=0, padx=padx, pady=30)
    return_btn.grid(row=6, column=1, padx=padx, pady=30)

    window.title(SHOP_APP_TITLE)

    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    width = 700
    height = 700
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
