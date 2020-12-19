# -*- coding: utf-8 -*-
import os
import tkinter
from tkinter import *

from COMMON.ReadJson import ReadJson
from COMMON.pub import CURRENT_USER
from COMMON.pub import FONT_SIZE_16
from COMMON.pub import FONT_SIZE_24
from COMMON.pub import NAME
from COMMON.pub import PWD
from COMMON.pub import SEX
from COMMON.pub import USER
from COMMON.pub import USER_ADDRESS
from COMMON.pub import USER_CONTACT


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
    welcome_label = Label(window, text='个人信息', font=('', FONT_SIZE_24))
    name = tkinter.Label(frame, text='姓名', font=('', FONT_SIZE_16), )
    sex = tkinter.Label(frame, text='性别', font=('', FONT_SIZE_16), )
    contact = tkinter.Label(frame, text='联系方式', font=('', FONT_SIZE_16), )
    address = tkinter.Label(frame, text='地址', font=('', FONT_SIZE_16), )
    account = tkinter.Label(frame, text='账号', font=('', FONT_SIZE_16), )
    pwd = tkinter.Label(frame, text='密码', font=('', FONT_SIZE_16), )
    obj = ReadJson(CURRENT_USER)
    data = obj.load_data()

    user2 = data.get(USER)
    print(user2)
    name2 = data.get(NAME, '未设置姓名')
    sex2 = data.get(SEX, '未设置性别')
    pwd2 = data.get(PWD, '未设置密码')
    contact2 = data.get(USER_CONTACT, '未设置联系方式')
    address2 = data.get(USER_ADDRESS, '未设置地址')
    name1 = tkinter.Label(frame, text=name2, font=('', FONT_SIZE_16), )
    sex1 = tkinter.Label(frame, text=sex2, font=('', FONT_SIZE_16), )
    account1 = tkinter.Label(frame, text=user2, font=('', FONT_SIZE_16), )
    pwd1 = tkinter.Label(frame, text=pwd2, font=('', FONT_SIZE_16), )
    contact1 = tkinter.Label(frame, text=contact2, font=('', FONT_SIZE_16), )
    address1 = tkinter.Label(frame, text=address2, font=('', FONT_SIZE_16), )
    return_btn = tkinter.Button(frame, text='返回', font=('', FONT_SIZE_16), command=btn1)
    update_btn = tkinter.Button(frame, text='修改', font=('', FONT_SIZE_16), command=btn2)

    welcome_label.pack(side=tkinter.TOP, padx=10, pady=40)
    frame.pack()
    padx = 20
    pady = 20
    name.grid(row=0, column=0, padx=padx, pady=pady)
    sex.grid(row=1, column=0, padx=padx, pady=pady)
    account.grid(row=2, column=0, padx=padx, pady=pady)
    pwd.grid(row=3, column=0, padx=padx, pady=pady)
    contact.grid(row=4, column=0, padx=padx, pady=pady)
    address.grid(row=5, column=0, padx=padx, pady=pady)
    update_btn.grid(row=6, column=0, padx=20, pady=pady)
    name1.grid(row=0, column=1, padx=padx, pady=pady)
    sex1.grid(row=1, column=1, padx=padx, pady=pady)
    account1.grid(row=2, column=1, padx=padx, pady=pady)
    pwd1.grid(row=3, column=1, padx=padx, pady=pady)
    contact1.grid(row=4, column=1, padx=padx, pady=pady)
    address1.grid(row=5, column=1, padx=padx, pady=pady)
    return_btn.grid(row=6, column=1, padx=20, pady=pady)

    window.title('购物系统')

    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    width = 500
    height = 650
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
