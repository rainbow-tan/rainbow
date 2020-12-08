# -*- encoding=utf-8 -*-

import tkinter
from tkinter import *


def end_insert():
    entry.insert('end', 'A')  # 插入到末尾


def point_insert():
    entry.insert('insert', 'B')  # 插入到光标处


def start_insert():
    entry.insert(0, 'C')  # 插入到开头


def four_insert():
    entry.insert(4, 'D')  # 插入到指定下标


def get():
    msg = entry.get()  # 获取输入的信息
    print(msg)


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

    entry = Entry(
            master=win,  # 父容器
            text='标签',  # 文本
            bg='pink',  # 背景颜色
            fg='red',  # 文本颜色
            relief='sunken',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            bd=3,  # 边框的大小
            width=10,  # 宽度
            state='normal',  # 设置状态 normal、readonly、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('黑体', 20),  # 字体
            show='',  # 显示的字符
            )
    entry.pack()
    Button(text='插入到末尾', command=end_insert).pack()
    Button(text='插入到鼠标位置', command=point_insert).pack()
    Button(text='插入到开始', command=start_insert).pack()
    Button(text='插入到下标4处', command=four_insert).pack()
    Button(text='获取输入的信息', command=get).pack()
    win.mainloop()
