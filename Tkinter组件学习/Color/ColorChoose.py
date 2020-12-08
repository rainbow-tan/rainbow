# -*- encoding=utf-8 -*-

import tkinter
import tkinter.colorchooser as cc
from tkinter import *


def choose_color():
    choose = cc.askcolor()
    print(choose)
    color_value = choose[1]
    button.config(bg=color_value)


if __name__ == '__main__':
    win = tkinter.Tk()  # 窗口
    win.title('南风丶轻语')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 500
    height = 300
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

    button = Button(win, text="Select Color", command=choose_color)
    button.pack()

    win.mainloop()
