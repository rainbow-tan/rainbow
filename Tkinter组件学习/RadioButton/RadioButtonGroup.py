# -*- encoding=utf-8 -*-

import tkinter
from tkinter import *


def event():
    print('选中的组件值为:{}'.format(value.get()))


def event2():
    print('选中的组件值为:{}'.format(value2.get()))


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

    f1 = Frame(relief='g')
    f1.pack(side=LEFT)
    value = IntVar()
    value.set(0)  # 不设置默认为0
    radiobutton = Radiobutton(
            master=f1,  # 父容器
            text='标签',  # 文本
            bg='yellow',  # 背景颜色
            fg='red',  # 文本颜色
            activebackground='pink',  # 状态为active时的背景颜色
            activeforeground='blue',  # 状态为active的文字颜色
            relief='flat',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            bd=3,  # 边框的大小
            height=1,  # 高度
            width=10,  # 宽度
            padx=1,  # 内间距，字体与边框的X距离
            pady=1,  # 内间距，字体与边框的Y距离
            state='normal',  # 设置状态 normal、active、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('黑体', 20),  # 字体
            value=1,  # 默认value，选中后会传递给variable
            variable=value,  # 通过IntVar设置1为选中,0为未选中
            command=event,  # 点击时的事件
            )
    radiobutton.pack()
    radiobutton = Radiobutton(
            master=f1,  # 父容器
            text='标签',  # 文本
            bg='pink',  # 背景颜色
            fg='blue',  # 文本颜色
            activebackground='yellow',  # 状态为active时的背景颜色
            activeforeground='red',  # 状态为active的文字颜色
            relief='flat',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            bd=3,  # 边框的大小
            height=1,  # 高度
            width=10,  # 宽度
            padx=1,  # 内间距，字体与边框的X距离
            pady=1,  # 内间距，字体与边框的Y距离
            state='normal',  # 设置状态 normal、active、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('黑体', 20),  # 字体
            value=2,  # 默认value，选中后会传递给variable
            variable=value,  # 通过IntVar设置1为选中,0为未选中
            command=event,  # 点击时的事件
            )
    radiobutton.pack()
    radiobutton = Radiobutton(
            master=f1,  # 父容器
            text='标签',  # 文本
            bg='yellow',  # 背景颜色
            fg='red',  # 文本颜色
            activebackground='pink',  # 状态为active时的背景颜色
            activeforeground='blue',  # 状态为active的文字颜色
            relief='flat',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            bd=3,  # 边框的大小
            height=1,  # 高度
            width=10,  # 宽度
            padx=1,  # 内间距，字体与边框的X距离
            pady=1,  # 内间距，字体与边框的Y距离
            state='normal',  # 设置状态 normal、active、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('黑体', 20),  # 字体
            value=3,  # 默认value，选中后会传递给variable
            variable=value,  # 通过IntVar设置1为选中,0为未选中
            command=event,  # 点击时的事件
            )
    radiobutton.pack()

    Label(f1, textvariable=value, relief='g', width=10).pack(padx=20)  # 用于显示value的值

    f1 = Frame(relief='g')
    f1.pack(side=RIGHT)
    value2 = IntVar()
    value2.set(0)  # 不设置默认为0
    radiobutton = Radiobutton(
            master=f1,  # 父容器
            text='标签',  # 文本
            bg='yellow',  # 背景颜色
            fg='red',  # 文本颜色
            activebackground='pink',  # 状态为active时的背景颜色
            activeforeground='blue',  # 状态为active的文字颜色
            relief='flat',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            bd=3,  # 边框的大小
            height=1,  # 高度
            width=10,  # 宽度
            padx=1,  # 内间距，字体与边框的X距离
            pady=1,  # 内间距，字体与边框的Y距离
            state='normal',  # 设置状态 normal、active、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('黑体', 20),  # 字体
            value=4,  # 默认value，选中后会传递给variable
            variable=value2,  # 通过IntVar设置1为选中,0为未选中
            command=event2,  # 点击时的事件
            )
    radiobutton.pack()
    radiobutton = Radiobutton(
            master=f1,  # 父容器
            text='标签',  # 文本
            bg='pink',  # 背景颜色
            fg='blue',  # 文本颜色
            activebackground='yellow',  # 状态为active时的背景颜色
            activeforeground='red',  # 状态为active的文字颜色
            relief='flat',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            bd=3,  # 边框的大小
            height=1,  # 高度
            width=10,  # 宽度
            padx=1,  # 内间距，字体与边框的X距离
            pady=1,  # 内间距，字体与边框的Y距离
            state='normal',  # 设置状态 normal、active、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('黑体', 20),  # 字体
            value=5,  # 默认value，选中后会传递给variable
            variable=value2,  # 通过IntVar设置1为选中,0为未选中
            command=event2,  # 点击时的事件
            )
    radiobutton.pack()
    radiobutton = Radiobutton(
            master=f1,  # 父容器
            text='标签',  # 文本
            bg='yellow',  # 背景颜色
            fg='red',  # 文本颜色
            activebackground='pink',  # 状态为active时的背景颜色
            activeforeground='blue',  # 状态为active的文字颜色
            relief='flat',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            bd=3,  # 边框的大小
            height=1,  # 高度
            width=10,  # 宽度
            padx=1,  # 内间距，字体与边框的X距离
            pady=1,  # 内间距，字体与边框的Y距离
            state='normal',  # 设置状态 normal、active、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('黑体', 20),  # 字体
            value=6,  # 默认value，选中后会传递给variable
            variable=value2,  # 通过IntVar设置1为选中,0为未选中
            command=event2,  # 点击时的事件
            )
    radiobutton.pack()

    Label(f1, textvariable=value2, relief='g', width=10).pack(padx=20)  # 用于显示value的值

    win.mainloop()
