# coding:utf-8
import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

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
    if value1 == '' or value2 == '' or value3 == '' or value4 == '' or value5 == '' or value6 == '':
        messagebox.showwarning('提示信息', '请完整填写信息')
        return
    try:
        value2 = float(value2)
    except:
        messagebox.showwarning('提示信息', '价格填写错误')
        return
    # names = shujuku.select_one(db, 'yifu', 'mingcheng')
    # if value1 in names:
    #     messagebox.showwarning('提示信息', '名称重复')
    #     return
    if value4 not in mingcheng:
        messagebox.showwarning('提示信息', '厂家不存在')
        do = messagebox.askyesno('提示信息', '是否要去添加厂家？')
        if do:
            win.destroy()
            os.system('python add_changjia.py')
        return
    if value5 not in xinming:
        messagebox.showwarning('提示信息', '员工不存在')
        do = messagebox.askyesno('提示信息', '是否要去添加员工？')
        if do:
            win.destroy()
            os.system('python add_yuangong.py')
        return
    if value6 not in mingcheng2:
        messagebox.showwarning('提示信息', '仓库不存在')
        do = messagebox.askyesno('提示信息', '是否要去添加仓库？')
        if do:
            win.destroy()
            os.system('python add_cangku.py')
        return

    # SQL 更新语句
    sql = 'UPDATE yifu SET jiage="{}",jijie="{}",changjia="{}",yuangong="{}",canku="{}" WHERE mingcheng="{}"'.format(
            value2, value3, value4, value5, value6, value1, )
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # messagebox.showinfo('提示信息','修改成功')
        flag = True
    except Exception as e:
        # 发生错误时回滚
        db.rollback()
        flag = False
        messagebox.showerror('提示信息', '修改失败：{}'.format(e))
    if flag:
        fanhui()
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
    win.title('南风丶轻语')  # 标题
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
        sql = 'select * from yifu where mingcheng="{}"'.format(choose_id)
        cursor = db.cursor()
        print(sql)
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        data = results[0]
        old_name = data[1]
        print(data)
    else:
        data = ['服装名称', '服装价格', '适用季节', '来源厂家', '导购职工', '存放仓库']

    mingcheng = shujuku.select_one(db, 'changjia', 'mingchen')
    print(mingcheng)
    xinming = shujuku.select_one(db, 'yuangong', 'xingming')
    print(xinming)
    mingcheng2 = shujuku.select_one(db, 'cangku', 'mingchen')
    print(mingcheng2)

    f = Frame(win)
    Label(f, text='服装名称', font=('', 20)).grid(row=0, column=0, padx=30, pady=15)
    Label(f, text='服装价格', font=('', 20)).grid(row=1, column=0, padx=30, pady=15)
    Label(f, text='适用季节', font=('', 20)).grid(row=2, column=0, padx=30, pady=15)
    Label(f, text='来源厂家', font=('', 20)).grid(row=3, column=0, padx=30, pady=15)
    Label(f, text='导购职工', font=('', 20)).grid(row=4, column=0, padx=30, pady=15)
    Label(f, text='存放仓库', font=('', 20)).grid(row=5, column=0, padx=30, pady=15)
    entry1 = Entry(f, font=('', 20), )
    entry1.grid(row=0, column=1)
    entry1.insert(END, data[0])
    entry1.config(state='disabled')
    entry2 = Entry(f, font=('', 20), )
    entry2.insert(END, data[2 - 1])
    entry2.grid(row=1, column=1)
    entry3 = Entry(f, font=('', 20), )
    entry3.insert(END, data[2])
    entry3.grid(row=2, column=1)
    entry4 = ttk.Combobox(f, font=('', 20), )
    entry4.insert(END, data[3])

    entry4['values'] = mingcheng
    entry4.grid(row=3, column=1, padx=30, )
    entry5 = ttk.Combobox(f, font=('', 20), )
    entry5.insert(END, data[4])
    entry5['values'] = xinming
    entry5.grid(row=4, column=1)
    entry6 = ttk.Combobox(f, font=('', 20), )
    entry6.insert(END, data[5])
    entry6['values'] = mingcheng2
    entry6.grid(row=5, column=1)
    entry6.bind('<Return>', do)

    Button(f, text='修改', font=('', 20), relief='g', command=add).grid(row=7, column=0, pady=20)
    Button(f, text='服饰', font=('', 20), relief='g', command=fanhui).grid(row=7, column=1)

    f.pack(pady=20)
    win.mainloop()
