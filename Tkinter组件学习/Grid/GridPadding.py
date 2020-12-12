# -*- encoding=utf-8 -*-

import tkinter
from tkinter import *

if __name__ == '__main__':
    pass
    win = tkinter.Tk()  # 窗口
    win.title('南风丶轻语')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 300
    height = 100
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置
    Button(win, text='按钮1', bg='red').grid(
            row=0,  # 行数
            column=0,  # 列数
            padx=5,  # 横坐标外间距
            pady=5,  # 纵坐标外间距
            ipadx=5,  # 横坐标内间距
            ipady=5,  # 纵坐标内间距
            )
    Button(win, text='按钮2', bg='yellow').grid(
            row=0,  # 行数
            column=1  # 列数
            )
    Button(win, text='按钮3', bg='blue').grid(
            row=0,  # 行数
            column=2  # 列数
            )
    Button(win, text='按钮4', bg='red').grid(
            row=1,  # 行数
            column=2  # 列数
            )
    Button(win, text='按钮5', bg='yellow').grid(
            row=1,  # 行数
            column=3  # 列数
            )
    Button(win, text='按钮6', bg='blue').grid(
            row=1,  # 行数
            column=4  # 列数
            )
    win.mainloop()
