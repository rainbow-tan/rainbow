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
    Button(win, text='按钮1', bg='red').pack(side=LEFT)
    Button(win, text='按钮2', bg='yellow').pack(side=LEFT)
    Button(win, text='按钮3', bg='blue').pack(side=LEFT)
    Button(win, text='按钮4', bg='green').pack(side=LEFT)

    Button(win, text='按钮5', bg='red').pack(side=RIGHT)
    Button(win, text='按钮6', bg='yellow').pack(side=RIGHT)
    Button(win, text='按钮7', bg='blue').pack(side=RIGHT)
    Button(win, text='按钮8', bg='green').pack(side=RIGHT)

    win.mainloop()
