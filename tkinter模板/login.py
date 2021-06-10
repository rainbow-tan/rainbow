# -*- encoding=utf-8 -*-
import tkinter
from tkinter import *
from tkinter import messagebox

import common
import select

USERNAME = 'username'
PASSWORD = 'password'
RETURN = '<Return>'


class LoginFrame(object):

    @staticmethod
    def set_users():
        # 重构这个函数,拼接出users
        users = [
            {USERNAME: 'admin', PASSWORD: 'admin'},
            ]
        return users

    @staticmethod
    def save_user(username, password):
        # 重构这个函数，保存用户名密码
        success = True
        msg = ''
        return success, msg

    def __init__(self, window, title='信息认证', head='图书管理系统', width=600, height=450):
        self.window = window
        self.user_entry = None  # 用户名输入框
        self.pwd_entry = None  # 密码输入框

        window.title(title)  # 设置标题
        common.middle_windows(window, width, height)  # 设置位置大小
        self.set_frame(head)  # 布局页面

    def login(self):
        username = self.user_entry.get().strip().lower()  # 获取用户名
        password = self.pwd_entry.get().strip().lower()  # 获取密码
        if username == '' or password == '':  # 合法性校验
            messagebox.showwarning('提示信息', '请输入用户名和密码!')
        else:
            users = self.set_users()  # 获取所有用户
            can_login = False
            for user in users:  # 遍历所有用户
                usr = user.get(USERNAME)  # 取出用户名
                pwd = user.get(PASSWORD)  # 取出密码
                if username.lower() == usr.lower() and password.lower() == pwd.lower():
                    can_login = True  # 可以登录
            if can_login:
                common.clear_child(self.window)  # 移除界面上的控件
                select.SelectFrame(self.window)  # 查询界面
            else:
                messagebox.showerror('提示信息', '用户名或密码错误!')

    def register(self):
        username = self.user_entry.get().strip().lower()  # 获取用户名
        password = self.pwd_entry.get().strip().lower()  # 获取密码
        if username == '' or password == '':  # 输入都不为空串
            messagebox.showwarning('提示信息', '请输入用户名和密码!')
            return False
        users = self.set_users()  # 获取所有用户
        names = []
        for user in users:  # 遍历用户
            usr = user.get(USERNAME)  # 取到用户名
            if usr:
                names.append(usr)  # 保存所有用户名
        if username in names:  # 判断用户是否已经存在
            messagebox.showwarning('提示信息', '用户名已存在!')
        else:
            success, msg = self.save_user(username, password)  # 保存用户名密码
            if success:
                messagebox.showinfo('提示信息', '恭喜你注册成功!')
            else:
                messagebox.showinfo('提示信息', '注册失败!\n异常信息:{}'.format(msg))

    def set_frame(self, title):
        frame = tkinter.Frame(self.window)  # Frame控件
        title_label = Label(self.window, text=title, font=('黑体', 26))  # title label控件
        size = 20  # 字体大小
        user_label = tkinter.Label(frame, text='用户名', font=('', size))  # label控件
        pwd_label = tkinter.Label(frame, text='密  码', font=('', size))  # label控件
        width = 16  # 输入框宽度
        self.user_entry = tkinter.Entry(frame, font=('', size), width=width)
        self.user_entry.focus()  # 输入框聚焦
        self.user_entry.bind(RETURN, lambda x: self.pwd_entry.focus())  # 绑定回车事件
        self.pwd_entry = tkinter.Entry(frame, show='*', font=('', size), width=width)  # 密码输入框
        register_btn = tkinter.Button(frame, text='注册', bg='#ff8000', font=('', size),
                                      command=self.register)  # 注册按钮
        login_btn = tkinter.Button(frame, text='登录', bg='green', font=('', size),
                                   command=self.login)  # 登录按钮
        self.pwd_entry.bind(RETURN, lambda x: self.login())  # 密码按钮绑定回车事件
        title_label.pack(side=tkinter.TOP, padx=10, pady=40)
        frame.pack()
        padx = 5
        pady = 20
        user_label.grid(row=0, column=0, padx=padx, pady=0)  # grid布局,放置组件
        pwd_label.grid(row=1, column=0, padx=padx, pady=pady)  # grid布局,放置组件
        self.user_entry.grid(row=0, column=1, padx=padx, pady=pady)  # grid布局,放置组件
        self.pwd_entry.grid(row=1, column=1, padx=padx, pady=pady)  # grid布局,放置组件
        pady2 = 40
        register_btn.grid(row=2, column=0, padx=10, pady=pady2)  # grid布局,放置组件
        login_btn.grid(row=2, column=1, padx=10, pady=pady2, sticky='e')  # grid布局,放置组件


if __name__ == '__main__':
    win = tkinter.Tk()
    login_window = LoginFrame(win)
    win.mainloop()
