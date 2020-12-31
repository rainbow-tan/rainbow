# coding:utf-8
import os
import tkinter
from datetime import datetime
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
    if value4 != '':
        try:
            datetime.strptime(value4, "%Y-%m-%d")
        except Exception as e:
            messagebox.showwarning('提示信息', '日期格式：年-月-日')
            return
    cursor = db.cursor()
    bianhao = shujuku.select_one(db, 'cangku', 'bianhao')
    xingming = shujuku.select_one(db, 'cangku', 'mingchen')
    print(bianhao)
    print('old_name：{}'.format(old_name))
    xingming.remove(old_name)
    print('xingming:{}'.format(xingming))
    if value2 in xingming:
        messagebox.showwarning('提示信息', '姓名重复')
        return
    cursor = db.cursor()

    # SQL 更新语句
    sql = 'UPDATE cangku SET mingchen="{}",dizhi="{}",chengli="{}",guanliyuan="{}",lianxifangshi="{}" WHERE bianhao="{}"'.format(
            value2, value3, value4, value5, value6, value1, )
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # messagebox.showinfo('提示信息','修改成功')
        flag1 = True
        # win.destroy()
        # os.system('python chakancangku.py')
    except:
        # 发生错误时回滚
        db.rollback()
        flag1 = False
        messagebox.showerror('提示信息', '修改失败')

    # SQL 更新语句
    sql = 'UPDATE yifu SET canku="{}" WHERE canku="{}"'.format(value2, old_name)
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # messagebox.showinfo('提示信息','修改成功')
        flage2 = True
        # win.destroy()
        # os.system('python chakancangku.py')
    except:
        # 发生错误时回滚
        flage2 = False
        db.rollback()
        messagebox.showerror('提示信息', '修改失败')
    if flag1 and flage2:
        win.destroy()
        os.system('python chakancangku.py')
    pass


def do(event):
    add()
    pass


def fanhui():
    win.destroy()
    os.system('python chakancangku.py')
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
    old_name = ''
    if len(sys.argv) >= 2:
        choose_id = sys.argv[1]
        print('choose id:{}'.format(choose_id))
        sql = 'select * from cangku where bianhao="{}"'.format(choose_id)
        cursor = db.cursor()
        print(sql)
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        data = results[0]
        old_name = data[1]
        print(data)
    else:
        data = ['仓库编号', '仓库名称', '仓库地址', '建成日期', '管理员', '联系方式', ]

    f = Frame(win)
    Label(f, text='仓库编号', font=('', 20)).grid(row=0, column=0, padx=30, pady=15)
    Label(f, text='仓库名称', font=('', 20)).grid(row=1, column=0, padx=30, pady=15)
    Label(f, text='仓库地址', font=('', 20)).grid(row=2, column=0, padx=30, pady=15)
    Label(f, text='建成日期', font=('', 20)).grid(row=3, column=0, padx=30, pady=15)
    Label(f, text='管理员', font=('', 20)).grid(row=4, column=0, padx=30, pady=15)
    Label(f, text='联系方式', font=('', 20)).grid(row=5, column=0, padx=30, pady=15)
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
    Button(f, text='仓库', font=('', 20), relief='g', command=fanhui).grid(row=7, column=1)

    f.pack(pady=20)
    win.mainloop()
