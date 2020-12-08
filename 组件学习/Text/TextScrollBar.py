# -*- encoding=utf-8 -*-

import tkinter
from tkinter import *

if __name__ == '__main__':
    win = tkinter.Tk()  # 窗口
    win.title('南风丶轻语')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 800
    height = 600
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

    frame = Frame(win)
    frame.pack()

    s_y = Scrollbar(frame, )
    s_y.pack(side=RIGHT, fill=Y)
    s_x = Scrollbar(frame, orient=HORIZONTAL)
    s_x.pack(side=BOTTOM, fill=X)
    text = Text(
            master=frame,  # 父容器
            bg='pink',  # 背景颜色
            fg='red',  # 文本颜色
            relief='sunken',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            bd=3,  # 边框的大小
            height=3,  # 高度
            width=10,  # 宽度
            padx=1,  # 内间距，字体与边框的X距离
            pady=1,  # 内间距，字体与边框的Y距离
            state='normal',  # 设置状态 normal、active、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('黑体', 20),  # 字体
            wrap='none',  # 字数够width后是否换行 char, none,  word
            yscrollcommand=s_y.set,  # 滚动条
            xscrollcommand=s_x.set,  # 滚动条
            )
    s_y.config(command=text.yview)
    s_x.config(command=text.xview)
    text.pack()

    win.mainloop()
