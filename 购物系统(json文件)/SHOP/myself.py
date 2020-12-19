# -*- coding: utf-8 -*-
import os
import tkinter
from tkinter import *

from COMMON.ReadJson import ReadJson
from COMMON.pub import CURRENT_SHOP
from COMMON.pub import FONT_SIZE_16
from COMMON.pub import PHONE
from COMMON.pub import SHOP_ADDRESS
from COMMON.pub import SHOP_NAME
from COMMON.pub import SHOP_OWNER
from COMMON.pub import SHOP_PWD
from COMMON.pub import SHOP_USER


def btn1():
    print('返回信息管理')
    window.destroy()
    os.system('python choose.py')
    pass


def btn2():
    print('修改')
    window.destroy()
    os.system('python myself_update.py')
    pass


if __name__ == '__main__':

    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    welcome_label = Label(window, text='店铺信息', font=('', 24))
    shop_name_label = tkinter.Label(frame, text='店铺名称:', fg='blue', font=('', FONT_SIZE_16), )
    shop_address_label = tkinter.Label(frame, text='店铺地址:', fg='blue', font=('', FONT_SIZE_16))
    shop_owner_label = tkinter.Label(frame, text='店主姓名:', fg='blue', font=('', FONT_SIZE_16))
    phone_label = tkinter.Label(frame, text='联系方式:', fg='blue', font=('', FONT_SIZE_16))
    shop_user_label = tkinter.Label(frame, text='账号:', fg='blue', font=('', FONT_SIZE_16))
    shop_pwd_label = tkinter.Label(frame, text='密码:', fg='blue', font=('', FONT_SIZE_16))

    obj = ReadJson(CURRENT_SHOP)
    data = obj.load_data()
    shop_user = data.get(SHOP_USER, '初始化用户')
    shop_pwd = data.get(SHOP_PWD, '初始化密码')
    shop_name = data.get(SHOP_NAME, '初始化店铺名称')
    shop_address = data.get(SHOP_ADDRESS, '初始化店铺地址')
    shop_owner = data.get(SHOP_OWNER, '初始化店主')
    phone = data.get(PHONE, '初始化联系方式')

    shop_name_label2 = tkinter.Label(frame, font=('', FONT_SIZE_16), text=shop_name)
    shop_address_label2 = tkinter.Label(frame, font=('', FONT_SIZE_16), text=shop_address)
    shop_owner_label2 = tkinter.Label(frame, font=('', FONT_SIZE_16), text=shop_owner)
    phone_label2 = tkinter.Label(frame, font=('', FONT_SIZE_16), text=phone)
    shop_user_label2 = tkinter.Label(frame, font=('', FONT_SIZE_16), text=shop_user)
    shop_pwd_label2 = tkinter.Label(frame, font=('', FONT_SIZE_16), text=shop_pwd)

    return_btn = tkinter.Button(frame, font=('', FONT_SIZE_16), text='返回', command=btn1)
    update_btn = tkinter.Button(frame, font=('', FONT_SIZE_16), text='修改', command=btn2)
    padx = 2
    pady = 20
    welcome_label.pack(side=tkinter.TOP, padx=padx, pady=60)
    frame.pack()

    shop_name_label.grid(row=0, column=0, padx=padx, pady=pady)
    shop_address_label.grid(row=0, column=2, padx=padx, pady=pady)
    shop_owner_label.grid(row=1, column=0, padx=padx, pady=pady)
    phone_label.grid(row=1, column=2, padx=padx, pady=pady)
    shop_user_label.grid(row=2, column=0, padx=padx, pady=pady)
    shop_pwd_label.grid(row=2, column=2, padx=padx, pady=pady)

    shop_name_label2.grid(row=0, column=1, padx=padx, pady=pady)
    shop_address_label2.grid(row=0, column=3, padx=padx, pady=pady)
    shop_owner_label2.grid(row=1, column=1, padx=padx, pady=pady)
    phone_label2.grid(row=1, column=3, padx=padx, pady=pady)
    shop_user_label2.grid(row=2, column=1, padx=padx, pady=pady)
    shop_pwd_label2.grid(row=2, column=3, padx=padx, pady=pady)

    update_btn.grid(row=3, column=1, padx=padx, pady=40)
    return_btn.grid(row=3, column=3, padx=padx, pady=40)

    window.title('购物系统')

    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    width = 800
    height = 560
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
