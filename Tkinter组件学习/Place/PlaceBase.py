# -*- encoding=utf-8 -*-
import tkinter
from tkinter import *

if __name__ == '__main__':

    win = tkinter.Tk()  # 窗口
    win.title('南风丶轻语')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 400
    height = 500
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

    Label(text='标签', relief='g').place(
            x=10,  # 绝对的横坐标X位置
            y=10,  # 绝对的纵坐标Y位置
            anchor=NW,  # 对齐方式n, ne, e, se, s, sw, w, nw, or center
            )
    label2 = Label(text='哈哈', relief='g')
    label2.place(
            relx=0.5,  # 相对的横坐标X位置,范围[0,1)
            rely=0.2,  # 相对的纵坐标Y位置,范围[0,1)
            anchor=CENTER,  # 对齐方式 n, ne, e, se, s, sw, w, nw, or center
            width=200,  # 组件的宽度
            height=50,  # 组件的高度
            )

    win.mainloop()
