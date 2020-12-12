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
            columnspan=2,  # 占的列数
            sticky=E + W  # 对齐方式 N/S/E/W，分别代表上/下/右/左
            )
    Button(win, text='按钮3', bg='blue').grid(
            row=0,  # 行数
            column=2  # 列数

            )
    Button(win, text='按钮4', bg='red').grid(
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
    Button(win, text='按钮7', bg='yellow').grid(
            row=0,  # 行数
            column=3,  # 列数
            rowspan=2,  # 占的行数
            ipady=10,  # 内间距Y
            sticky=N + S + E + W  # 对齐方式 N/S/E/W，分别代表上/下/右/左
            )
    win.mainloop()
