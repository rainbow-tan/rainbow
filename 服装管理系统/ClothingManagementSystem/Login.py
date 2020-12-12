# coding:utf-8

# -*- encoding=utf-8 -*-
import os
import tkinter
from tkinter import *
from tkinter import messagebox

import shujuku
from shujuku import db


def user_enter(event):
    login()


def register():
    username = user.get().strip()
    password = pwd.get().strip()
    if username == '' or password == '':
        messagebox.showwarning('提示信息', '用户名密码不能为空!')
        return
    data = shujuku.select_all(db, 'user')
    usr = {}
    for i in data:
        usr[i[0]] = i[1]
    # print('当前用户:{}'.format(usr))
    if username.lower() not in usr:

        if shujuku.insert_user(db, username, password):
            messagebox.showinfo('提示信息', '注册成功！！！')
        else:
            messagebox.showerror('提示信息', '注册失败！！！')
    else:
        messagebox.showwarning('提示信息', '用户名已存在！')


def login():
    username = user.get().strip()
    password = pwd.get().strip()
    if username == '' or password == '':
        messagebox.showwarning('提示信息', '用户名密码不能为空！')
        return
    # print(db)
    data = shujuku.select_all(db, 'user')
    usr = {}
    for i in data:
        usr[i[0]] = i[1]
    # print('当前用户:{}'.format(usr))
    # usr = {'admin': 'admin'}
    if username in usr and password == usr[username]:
        win.destroy()
        db.close()
        os.system('python MainWin.py')
    else:
        messagebox.showerror('提示信息', '用户名密码错误！')


if __name__ == '__main__':
    win = tkinter.Tk()  # 窗口
    win.title('南风丶轻语')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 500
    height = 360
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置
    win.resizable(0, 0)

    f0 = Frame(win)
    Label(text='彩蝶服装管理', font=('', 20)).pack(pady=20)
    f = Frame(win)
    Label(f, text='用户名', font=('', 20)).grid(row=0, column=0, padx=30, pady=30)
    Label(f, text='密  码', font=('', 20)).grid(row=1, column=0)
    user = Entry(f, font=('', 20), width=12)
    user.grid(row=0, column=1)
    pwd = Entry(f, font=('', 20), show='*', width=12)
    pwd.grid(row=1, column=1)
    pwd.bind('<Return>', user_enter)
    Button(f, text='登陆', font=('', 20), relief='g', command=login).grid(row=2, column=0, pady=40)
    Button(f, text='注册', font=('', 20), relief='g', command=register).grid(row=2, column=1)
    f0.pack(pady=0)
    f.pack()

    win.mainloop()
