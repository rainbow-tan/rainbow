# -*- encoding=utf-8 -*-

import tkinter
from tkinter import *


def event():
    print('当前的值:{}'.format(value.get()))


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

    value = StringVar()
    checkbutton = Checkbutton(
            master=win,  # 父容器
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
            onvalue='哈哈',  # 选中传递的值，默认是1
            offvalue='嘿嘿',  # 取消选中后传递的值，默认是0
            variable=value,  # 通过onvalue和offvalue传递
            command=event,  # 点击时的事件
            )
    checkbutton.pack()

    Label(win, textvariable=value, relief='g', width=10).pack(padx=20)  # 用于显示value的值

    win.mainloop()
