# coding:utf-8
import os
import tkinter
from tkinter import *


def add():
    pass


def do(event):
    add()
    pass


def fanhui():
    win.destroy()
    os.system('python chakanyifu.py')
    pass


if __name__ == '__main__':
    win = tkinter.Tk()  # 窗口
    win.title('服装管理系统')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 580
    height = 500
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置
    # win.resizable(0, 0)

    data = ['服装名称', '服装价格', '适用季节', '来源厂家', '导购职工', '库存数量']

    f = Frame(win)
    Label(f, text='服装名称', font=('', 20)).grid(row=0, column=0, padx=30, pady=15)
    Label(f, text='服装价格', font=('', 20)).grid(row=1, column=0, padx=30, pady=15)
    Label(f, text='适用季节', font=('', 20)).grid(row=2, column=0, padx=30, pady=15)
    Label(f, text='来源厂家', font=('', 20)).grid(row=3, column=0, padx=30, pady=15)
    Label(f, text='导购职工', font=('', 20)).grid(row=4, column=0, padx=30, pady=15)
    Label(f, text='库存数量', font=('', 20)).grid(row=5, column=0, padx=30, pady=15)
    entry1 = Entry(f, font=('', 20), )
    entry1.grid(row=0, column=1)
    entry1.insert(END, data[1 - 1])
    entry1.config(state='readonly')
    print(entry1.get())
    entry2 = Entry(f, font=('', 20), )
    entry2.grid(row=1, column=1)
    entry2.insert(END, data[2 - 1])
    entry3 = Entry(f, font=('', 20), )
    entry3.grid(row=2, column=1)
    entry3.insert(END, data[3 - 1])
    entry4 = Entry(f, font=('', 20), )
    entry4.grid(row=3, column=1, padx=30, )
    entry4.insert(END, data[4 - 1])
    entry5 = Entry(f, font=('', 20), )
    entry5.grid(row=4, column=1)
    entry5.insert(END, data[5 - 1])
    entry6 = Entry(f, font=('', 20), )
    entry6.grid(row=5, column=1)
    entry6.insert(END, data[6 - 1])
    entry6.bind('<Return>', do)

    Button(f, text='修改', font=('', 20), relief='g', command=add).grid(row=7, column=0, pady=20)
    Button(f, text='服饰', font=('', 20), relief='g', command=fanhui).grid(row=7, column=1)

    f.pack(pady=20)
    win.mainloop()
