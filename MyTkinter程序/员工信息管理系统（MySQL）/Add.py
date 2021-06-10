# coding:utf-8
from datetime import datetime
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import Login
from MyDatabase import db
from MyDatabase import insert_database
from MyDatabase import select_database
import Select


def add_html():
    def add():
        number = number_entry.get().strip()
        name = name_entry.get().strip()
        sex = sex_combobox.get().strip()
        into_date = intodate_entry.get().strip()
        job = job_entry.get().strip()
        pay = pay_entry.get().strip()
        check_empty = [number, name, sex, into_date, job, pay]
        for i in check_empty:
            if i == '':
                messagebox.showwarning('提示信息', '请完善数据')
                return
        db_data = select_database(db, 'employee', ['number'], {'number': number})
        if db_data:
            messagebox.showwarning('提示信息', '该员工编号已存在，请更换!')
            return
        try:
            datetime.strptime(into_date, '%Y-%m-%d')
        except Exception as e:
            messagebox.showwarning('提示信息', '日期填写格式（2012-05-04）')
            return
        try:
            float(pay)
        except Exception as e:
            messagebox.showwarning('提示信息', '薪资填错误')
            return
        insert_data = {'number': number, 'name': name, 'sex': sex, 'hiredate': into_date, 'position': job, 'pay': pay, }
        insert_database(db, 'employee', [insert_data])
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
    win.title('南风丶轻语')  # 标题
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
    Label(text='员工入职', font=('粗体', 26), fg='green').pack()
    Label(frame, text='编    号', font=('', 20)).grid(row=0, column=0, padx=30, pady=15)
    Label(frame, text='姓    名', font=('', 20)).grid(row=1, column=0, padx=30, pady=15)
    Label(frame, text='性    别', font=('', 20)).grid(row=2, column=0, padx=30, pady=15)
    Label(frame, text='入职日期', font=('', 20)).grid(row=3, column=0, padx=30, pady=15)
    Label(frame, text='职    位', font=('', 20)).grid(row=4, column=0, padx=30, pady=15)
    Label(frame, text='薪    资', font=('', 20)).grid(row=5, column=0, padx=30, pady=15)
    number_entry = Entry(frame, font=('', 15), )
    number_entry.grid(row=0, column=1)
    name_entry = Entry(frame, font=('', 15), )
    name_entry.grid(row=1, column=1)
    sex_value = StringVar()
    sex_value.set('')
    sex_values = ['', '男', '女']
    sex_combobox = ttk.Combobox(
        master=frame,  # 父容器
        height=10,  # 高度,下拉显示的条目数量
        width=13,  # 宽度
        state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
        cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
        font=('', 20),  # 字体
        textvariable=sex_value,  # 通过StringVar设置可改变的值
        values=sex_values,  # 设置下拉框的选项
        )
    # sex_combobox = Entry(frame, font=('', 15), )
    sex_combobox.grid(row=2, column=1)
    intodate_entry = Entry(frame, font=('', 15), )
    intodate_entry.grid(row=3, column=1, padx=30, )
    job_entry = Entry(frame, font=('', 15), )
    job_entry.grid(row=4, column=1)
    pay_entry = Entry(frame, font=('', 15), )
    pay_entry.grid(row=5, column=1)
    pay_entry.bind('<Return>', do)

    Button(frame2, text='添加', font=('', 16), relief='g', command=add).pack(side=LEFT, padx=20)
    Button(frame2, text='主页', font=('', 16), relief='g', command=fanhui).pack(side=LEFT, padx=60)
    Button(frame2, text='注销', font=('', 16), relief='g', command=login_html).pack(side=LEFT, padx=20)

    frame.pack(pady=20)
    frame2.pack()
    win.mainloop()


if __name__ == '__main__':
    add_html()
