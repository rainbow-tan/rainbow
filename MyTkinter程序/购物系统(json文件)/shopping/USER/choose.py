# -*- coding: utf-8 -*-
import os
import tkinter
from tkinter import *

sys.path.append('../')
from COMMON.pub import *


def btn1_event():
    ##print('查看个人信息')
    window.destroy()
    os.system('python myself.py')
    pass


def btn2_event():
    ##print('查看店铺信息')
    window.destroy()
    os.system('python see_shop.py')
    pass


def btn3_event():
    ##print('个人订单管理')
    window.destroy()
    os.system('python my_orders.py')
    pass


def btn4_event():
    ##print('返回登录')
    window.destroy()
    os.system('python user.py')
    pass


if __name__ == '__main__':

    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    welcome_label = Label(window, text='信息管理', font=('', FONT_SIZE_24))
    login_btn1 = tkinter.Button(frame, text='个人信息', font=('', FONT_SIZE_16), command=btn1_event)
    login_btn2 = tkinter.Button(frame, text='查看店铺', font=('', FONT_SIZE_16), command=btn2_event)
    login_btn3 = tkinter.Button(frame, text='订单管理', font=('', FONT_SIZE_16), command=btn3_event)
    login_btn4 = tkinter.Button(frame, text='返回登录', font=('', FONT_SIZE_16), command=btn4_event)
    welcome_label.pack(side=tkinter.TOP, padx=10, pady=40)
    frame.pack()
    padx = 50
    pady = 30
    login_btn1.grid(row=1, column=0, padx=padx, pady=pady)
    login_btn2.grid(row=1, column=1, padx=padx, pady=pady)
    login_btn3.grid(row=2, column=0, padx=padx, pady=pady)
    login_btn4.grid(row=2, column=1, padx=padx, pady=pady)
    window.title(CUSTOMER_APP_TITLE)
    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    width = 700
    height = 450
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
