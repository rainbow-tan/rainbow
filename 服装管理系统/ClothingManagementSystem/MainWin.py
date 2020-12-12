# coding:utf-8
import os
import tkinter
from tkinter import *

from PIL import Image
from PIL import ImageTk


def add_cloth():
    win.destroy()
    os.system('python add_yifu.py')


def add_changjia():
    win.destroy()
    os.system('python add_changjia.py')


def add_kucun():
    win.destroy()
    os.system('python add_cangku.py')


def chakanyifu():
    win.destroy()
    os.system('python chakanyifu.py')


def chakanchangjia():
    win.destroy()
    os.system('python chakanchangjia.py')


def chakanyungong():
    win.destroy()
    os.system('python chakanyuangong.py')


def chakancangku():
    win.destroy()
    os.system('python chakancangku.py')


def add_yuangong():
    win.destroy()
    os.system('python add_yuangong.py')


if __name__ == '__main__':
    win = tkinter.Tk()  # 窗口
    win.title('南风丶轻语')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 600
    height = 430
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置
    win.resizable(0, 0)

    img1 = ImageTk.PhotoImage(Image.open('1.png'))
    img2 = ImageTk.PhotoImage(Image.open('2.png'))
    img3 = ImageTk.PhotoImage(Image.open('3.png'))
    img4 = ImageTk.PhotoImage(Image.open('4.png'))
    img5 = ImageTk.PhotoImage(Image.open('5.png'))
    img6 = ImageTk.PhotoImage(Image.open('6.png'))
    img7 = ImageTk.PhotoImage(Image.open('7.png'))
    img8 = ImageTk.PhotoImage(Image.open('8.png'))
    img9 = ImageTk.PhotoImage(Image.open('9.png'))
    img10 = ImageTk.PhotoImage(Image.open('10.png'))
    img11 = ImageTk.PhotoImage(Image.open('11.png'))
    img12 = ImageTk.PhotoImage(Image.open('12.png'))

    menu11 = Menu(font=('', 16), tearoff=0)
    menu11.add_command(label='添置新衣', command=add_cloth)
    menu11.add_command(label='浏览服饰', command=chakanyifu)
    menu1 = Menu(font=('', 16), tearoff=0)
    menu1.add_cascade(label='功能选择', menu=menu11)

    menu21 = Menu(font=('', 16), tearoff=0)
    menu21.add_command(label='厂家入驻', command=add_changjia)
    menu21.add_command(label='所有厂家', command=chakanchangjia)
    menu2 = Menu(font=('', 16), tearoff=0)
    menu2.add_cascade(label='功能选择', menu=menu21)

    menu31 = Menu(font=('', 16), tearoff=0)
    menu31.add_command(label='员工入职', command=add_yuangong)
    menu31.add_command(label='管理员工', command=chakanyungong)
    menu3 = Menu(font=('', 16), tearoff=0)
    menu3.add_cascade(label='功能选择', menu=menu31)

    menu41 = Menu(font=('', 16), tearoff=0)
    menu41.add_command(label='服饰入库', command=add_kucun)
    menu41.add_command(label='库存查询', command=chakancangku)
    menu4 = Menu(font=('', 16), tearoff=0)
    menu4.add_cascade(label='功能选择', menu=menu41)

    menu = Menu(font=('', 16), tearoff=0)
    menu.add_cascade(label='服装管理', menu=menu1)
    menu.add_cascade(label='厂家管理', menu=menu2)
    menu.add_cascade(label='员工管理', menu=menu3)
    menu.add_cascade(label='库存管理', menu=menu4)

    win.config(menu=menu)
    f = Frame()
    Button(f, image=img1, relief='g').grid(row=0, column=0)
    Button(f, image=img2, relief='g').grid(row=0, column=1)
    Button(f, image=img3, relief='g').grid(row=0, column=2)
    Button(f, image=img4, relief='g').grid(row=0, column=3)
    Button(f, image=img5, relief='g').grid(row=1, column=0)
    Button(f, image=img6, relief='g').grid(row=1, column=1)
    Button(f, image=img7, relief='g').grid(row=1, column=2)
    Button(f, image=img8, relief='g').grid(row=1, column=3)
    Button(f, image=img9, relief='g').grid(row=2, column=0)
    Button(f, image=img10, relief='g').grid(row=2, column=1)
    Button(f, image=img11, relief='g').grid(row=2, column=2)
    Button(f, image=img12, relief='g').grid(row=2, column=3)

    f.pack(pady=10)
    win.mainloop()
