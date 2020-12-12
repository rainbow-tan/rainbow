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
            sticky=E  # 对齐方式 N/S/E/W，分别代表上/下/右/左
            )
    Button(win, text='按钮2', bg='yellow').grid(
            row=0,  # 行数
            column=1  # 列数
            )
    Button(win, text='按钮3', bg='blue').grid(
            row=0,  # 行数
            column=2  # 列数
            )
    Button(win, text='按钮4', bg='red', width=10).grid(
            row=1,  # 行数
            column=0  # 列数
            )
    Button(win, text='按钮5', bg='yellow').grid(
            row=1,  # 行数
            column=1  # 列数
            )
    Button(win, text='按钮6', bg='blue').grid(
            row=1,  # 行数
            column=2  # 列数
            )
    win.mainloop()
