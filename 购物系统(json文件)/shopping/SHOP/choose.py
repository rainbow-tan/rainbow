# -*- coding: utf-8 -*-
import sys

sys.path.append('../')
import os
import tkinter
from tkinter import *

from COMMON.pub import FONT_SIZE_16
from COMMON.pub import FONT_SIZE_24
from COMMON.pub import SHOP_APP_TITLE


def btn1_event():
    window.destroy()
    os.system('python myself.py')
    pass


def btn2_event():
    window.destroy()
    os.system('python goods.py')
    pass


def btn3_event():
    window.destroy()
    os.system('python my_orders.py')
    pass


def btn4_event():
    window.destroy()
    os.system('python user.py')
    pass


if __name__ == '__main__':

    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    welcome_label = Label(window, text='信息管理', font=('', FONT_SIZE_24))
    login_btn1 = tkinter.Button(frame, text='店铺信息', font=('', FONT_SIZE_16), command=btn1_event)
    login_btn2 = tkinter.Button(frame, text='商品管理', font=('', FONT_SIZE_16), command=btn2_event)
    login_btn3 = tkinter.Button(frame, text='订单管理', font=('', FONT_SIZE_16), command=btn3_event)
    login_btn4 = tkinter.Button(frame, text='返回登录', font=('', FONT_SIZE_16), command=btn4_event)
    welcome_label.pack(side=tkinter.TOP, padx=10, pady=40)
    frame.pack()
    login_btn1.grid(row=1, column=0, padx=50, pady=30)
    login_btn2.grid(row=1, column=1, padx=50, pady=30)
    login_btn3.grid(row=2, column=0, padx=50, pady=30)
    login_btn4.grid(row=2, column=1, padx=50, pady=30)
    window.title(SHOP_APP_TITLE)
    window.resizable(0, 0)
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    width = 700
    height = 450
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
