# -*- encoding=utf-8 -*-

import tkinter
from tkinter import *

from PIL import Image
from PIL import ImageTk


def event():
    print('点击事件')


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

    img_open = Image.open('19.png')
    img_png = ImageTk.PhotoImage(img_open)
    button = Button(
            master=win,  # 父容器
            text='标签',  # 文本
            bg='pink',  # 背景颜色
            fg='red',  # 文本颜色
            activebackground='pink',  # 状态为active时的背景颜色
            activeforeground='blue',  # 状态为active的文字颜色
            relief='groove',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            bd=3,  # 边框的大小
            height=64,  # 高度
            width=64,  # 宽度
            padx=1,  # 内间距，字体与边框的X距离
            pady=1,  # 内间距，字体与边框的Y距离
            state='normal',  # 设置状态 normal、active、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('黑体', 20),  # 字体
            image=img_png,  # 图片
            command=event,  # 点击事件
            )
    button.pack()
    win.mainloop()
