# coding:utf-8
import tkinter
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import Login
import Select
from common import NEWS_TXT
from common import TITLE


def add_html():
    def add():
        value1 = number_entry.get().strip()
        print('value1:{}'.format(value1))
        value2 = name_entry.get().strip()
        print('value2:{}'.format(value2))
        value3 = job_entry.get().strip()
        print('value3:{}'.format(value3))
        value4 = sex_combobox.get().strip()
        print('value4:{}'.format(value4))
        check_empty = [value1, value2, value3, value4, ]
        for i in check_empty:
            if i == '':
                messagebox.showwarning('提示信息', '请完善数据')
                return
        with open(NEWS_TXT,'r',encoding='utf-8') as f:
            news = f.readlines()
        print('news:{}'.format(news))
        xuhaos=[]
        for new in news:
            xuhaos.append(new.split('-')[0].strip())
        print('xuhaos:{}'.format(xuhaos))
        if value1 in xuhaos:
            messagebox.showwarning('提示信息', '该编号已存在!')
            return
        add_info = value1+'-'+value2+'-'+value3+'-'+value4+'\n'
        print('add_info:{}'.format(add_info))
        with open(NEWS_TXT,'a',encoding='utf-8') as f:
            f.write(add_info)
        fanhui()

    def login_html():
        win.destroy()
        Login.login_html()

    def do(event):
        add()

    def fanhui():
        win.destroy()
        Select.select_html()

    win = tkinter.Tk()  # 窗口
    win.title(TITLE)  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 580
    height = 560
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置
    win.resizable(0, 0)

    frame = Frame(win)
    frame1 = Frame(win)
    frame2 = Frame(win)
    frame1.pack(pady=10)
    Label(text='新增新闻', font=('粗体', 26), ).pack()
    Label(frame, text='编    号', font=('', 20)).grid(row=0, column=0, padx=30, pady=15)
    Label(frame, text='标    题', font=('', 20)).grid(row=1, column=0, padx=30, pady=15)
    Label(frame, text='内    容', font=('', 20)).grid(row=2, column=0, padx=30, pady=15)
    Label(frame, text='状    态', font=('', 20)).grid(row=3, column=0, padx=30, pady=15)
    number_entry = Entry(frame, font=('', 15), )
    number_entry.grid(row=0, column=1)
    name_entry = Entry(frame, font=('', 15), )
    name_entry.grid(row=1, column=1)
    job_entry = Entry(frame, font=('', 15), )
    job_entry.grid(row=2, column=1)
    zhuangtai = StringVar()
    zhuangtai.set('')
    sex_values = ['未发布', '发布']
    sex_combobox = ttk.Combobox(
            master=frame,  # 父容器
            height=10,  # 高度,下拉显示的条目数量
            width=13,  # 宽度
            state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('', 20),  # 字体
            textvariable=zhuangtai,  # 通过StringVar设置可改变的值
            values=sex_values,  # 设置下拉框的选项
            )
    sex_combobox.grid(row=3, column=1)

    Button(frame2, text='添加', font=('', 16), relief='g', command=add).pack(side=LEFT, padx=20)
    Button(frame2, text='主页', font=('', 16), relief='g', command=fanhui).pack(side=LEFT, padx=60)
    Button(frame2, text='注销', font=('', 16), relief='g', command=login_html).pack(side=LEFT,
                                                                                  padx=20)

    frame.pack(pady=20)
    frame2.pack()
    win.mainloop()


if __name__ == '__main__':
    add_html()
