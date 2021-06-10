# -*- encoding=utf-8 -*-
import tkinter
from tkinter import *
from tkinter import messagebox

from MyDatabase import db
from MyDatabase import insert_database
from MyDatabase import select_database
import Select


def login_html():
    def user_enter(event):
        login()

    def register():
        username = user.get().strip()
        password = pwd.get().strip()
        if username == '' or password == '':
            messagebox.showwarning('提示信息', '用户名密码不能为空!')
            return
        data = select_database(db, 'user', ['username', 'password'])

        usr = []
        for item in data:
            usr.append(item['username'])
        if username not in usr:
            ret = insert_database(db, 'user', [{'username': username, 'password': password}])
            if ret == '':
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

        data = select_database(db, 'user', ['username', 'password'])
        for i in data:
            if username == i['username'] and password == i['password']:
                print('可以登录')
                win.destroy()
                Select.select_html()
                break
        else:
            messagebox.showerror('提示信息', '用户名密码错误！')

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

    frame1 = Frame(win)
    Label(text='员工信息管理系统', font=('', 20)).pack(pady=20)
    frame2 = Frame(win)
    Label(frame2, text='用户名', font=('', 20)).grid(row=0, column=0, padx=30, pady=30)
    Label(frame2, text='密  码', font=('', 20)).grid(row=1, column=0)
    user = Entry(frame2, font=('', 20), width=12)
    user.grid(row=0, column=1)
    pwd = Entry(frame2, font=('', 20), show='*', width=12)
    pwd.grid(row=1, column=1)
    pwd.bind('<Return>', user_enter)
    Button(frame2, text='注册', font=('', 20), relief='g', command=register).grid(row=2, column=0)
    Button(frame2, text='登陆', font=('', 20), relief='g', command=login).grid(row=2, column=1, pady=40)
    frame1.pack(pady=0)
    frame2.pack()

    win.mainloop()


if __name__ == '__main__':
    login_html()
