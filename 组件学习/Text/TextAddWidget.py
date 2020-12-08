# -*- encoding=utf-8 -*-
import threading
import time
import tkinter
from tkinter import *

from PIL import Image
from PIL import ImageTk


def add_btn():
    btn = Button(text='按钮', relief='g', width=20)
    text.window_create(INSERT, window=btn)  # 鼠标处插入
    text.update()  # 更新

    # text.window_create(1.2,window=btn)#1行3列插入
    # text.update()
    def delete():
        time.sleep(2)
        btn.destroy()  # 销毁
        # text.delete(btn)

    thread = threading.Thread(target=delete)
    thread.start()


def add_image():
    # 图片需要为全局变量
    text.image_create(INSERT, image=img)
    text.update()


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

    img = ImageTk.PhotoImage(Image.open('19.png'))
    text = Text(
            master=win,  # 父容器
            bg='pink',  # 背景颜色
            fg='red',  # 文本颜色
            relief='groove',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            bd=3,  # 边框的大小
            height=3,  # 高度
            width=20,  # 宽度
            padx=1,  # 内间距，字体与边框的X距离
            pady=1,  # 内间距，字体与边框的Y距离
            state='normal',  # 设置状态 normal、active、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('黑体', 20),  # 字体
            wrap='char',  # 字数够width后是否换行 char, none,  word
            )
    text.pack()
    Button(text='添加按钮', command=add_btn).pack()
    Button(text='添加图片', command=add_image).pack()
    win.mainloop()
