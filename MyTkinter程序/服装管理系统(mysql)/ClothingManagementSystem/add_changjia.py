# coding:utf-8
import os
import tkinter
from tkinter import *
from tkinter import messagebox

import shujuku
from shujuku import db


def add():
    value1 = entry1.get().strip()
    value2 = entry2.get().strip()
    value3 = entry3.get().strip()
    value4 = entry4.get().strip()
    value5 = entry5.get().strip()
    value6 = entry6.get().strip()
    print('value1:{}'.format(value1))
    print('value2:{}'.format(value2))
    print('value3:{}'.format(value3))
    print('value4:{}'.format(value4))
    print('value5:{}'.format(value5))
    print('value6:{}'.format(value6))
    if value1 == '' or value2 == '':
        messagebox.showwarning('提示信息', '编号和名称不能为空')
        return
    cursor = db.cursor()
    bianhao = shujuku.select_one(db, 'changjia', 'bianhao')
    xingming = shujuku.select_one(db, 'changjia', 'mingchen')
    print(bianhao)
    if value1 in bianhao:
        messagebox.showwarning('提示信息', '编号重复')
        return
    if value2 in xingming:
        messagebox.showwarning('提示信息', '姓名重复')
        return
        # SQL 插入语句
    sql = "INSERT INTO changjia VALUES ('{}','{}','{}','{}','{}','{}')".format(value1, value2,
                                                                               value3, value4,
                                                                               value5,
                                                                               value6)
    print(sql)
    flag = False
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # messagebox.showinfo('提示信息','添加成功！！！')
        flag = True
    except Exception as e:
        # 发生错误时回滚
        db.rollback()
        # print('Fail:{}'.format(e))
        messagebox.showerror('提示信息', '添加失败:{}'.format(e))
    if flag:
        fanhui()

    pass


def do(event):
    add()
    pass


def fanhui():
    win.destroy()
    os.system('python chakanchangjia.py')
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

    f = Frame(win)
    Label(f, text='厂家编号', font=('', 20)).grid(row=0, column=0, padx=30, pady=15)
    Label(f, text='厂家名称', font=('', 20)).grid(row=1, column=0, padx=30, pady=15)
    Label(f, text='厂家性质', font=('', 20)).grid(row=2, column=0, padx=30, pady=15)
    Label(f, text='厂家地址', font=('', 20)).grid(row=3, column=0, padx=30, pady=15)
    Label(f, text='联 系 人', font=('', 20)).grid(row=4, column=0, padx=30, pady=15)
    Label(f, text='联系方式', font=('', 20)).grid(row=5, column=0, padx=30, pady=15)
    entry1 = Entry(f, font=('', 20), )
    entry1.grid(row=0, column=1)
    entry2 = Entry(f, font=('', 20), )
    entry2.grid(row=1, column=1)
    entry3 = Entry(f, font=('', 20), )
    entry3.grid(row=2, column=1)
    entry4 = Entry(f, font=('', 20), )
    entry4.grid(row=3, column=1, padx=30, )
    entry5 = Entry(f, font=('', 20), )
    entry5.grid(row=4, column=1)
    entry6 = Entry(f, font=('', 20), )
    entry6.grid(row=5, column=1)
    entry6.bind('<Return>', do)

    Button(f, text='添加', font=('', 20), relief='g', command=add).grid(row=7, column=0, pady=20)
    Button(f, text='厂家', font=('', 20), relief='g', command=fanhui).grid(row=7, column=1)

    f.pack(pady=20)
    win.mainloop()
