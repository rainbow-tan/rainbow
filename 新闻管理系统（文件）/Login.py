# -*- encoding=utf-8 -*-
import json
import tkinter
from tkinter import *
from tkinter import messagebox

import Select
from common import TITLE
from common import USER_JSON


def login_html():
    def user_enter(event):
        login()

    def register():
        username = user.get().strip()
        password = pwd.get().strip()
        if username == '' or password == '':
            messagebox.showwarning('提示信息', '用户名密码不能为空!')
            return
        with open(USER_JSON, encoding='utf-8') as f:
            users = json.load(f)
        if username not in users:
            users[username] = password
            with open(USER_JSON, 'w', encoding='utf-8') as f:
                json.dump(users, f)
            messagebox.showinfo('提示信息', '恭喜你注册成功!')
        else:
            messagebox.showwarning('提示信息', '用户名已存在，注册失败!')

    def login():
        username = user.get().strip()
        password = pwd.get().strip()
        if username == '' or password == '':
            messagebox.showwarning('提示信息', '用户名密码不能为空！')
            return

        with open(USER_JSON, encoding='utf-8') as f:
            users = json.load(f)
        print('用户:{}'.format(users))
        if username in users and users[username] == password:
            print('可以登录')
            win.destroy()
            Select.select_html()
        else:
            messagebox.showerror('提示信息', '用户名密码错误！')

    win = tkinter.Tk()  # 窗口
    win.title('新闻信息管理系统')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 500
    height = 360
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置
    win.resizable(0, 0)

    frame1 = Frame(win)
    Label(text=TITLE, font=('', 20)).pack(pady=20)
    frame2 = Frame(win)
    Label(frame2, text='用户名', font=('', 20)).grid(row=0, column=0, padx=30, pady=30)
    Label(frame2, text='密  码', font=('', 20)).grid(row=1, column=0)
    user = Entry(frame2, font=('', 20), width=12)
    user.grid(row=0, column=1)
    pwd = Entry(frame2, font=('', 20), show='*', width=12)
    pwd.grid(row=1, column=1)
    pwd.bind('<Return>', user_enter)
    Button(frame2, text='注册', font=('', 20), relief='g', command=register).grid(row=2, column=0)
    Button(frame2, text='登陆', font=('', 20), relief='g', command=login).grid(row=2, column=1,
                                                                             pady=40)
    frame1.pack(pady=0)
    frame2.pack()

    win.mainloop()


if __name__ == '__main__':
    login_html()
