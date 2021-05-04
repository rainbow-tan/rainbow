# -*- encoding=utf-8 -*-
import tkinter
from tkinter import *
from tkinter import messagebox

import common
import pub
import select

USERNAME = 'username'
PASSWORD = 'password'
RETURN = '<Return>'
USERS_FILE_NAME = 'users.json'


class LoginFrame(object):

    @staticmethod
    def set_users():
        # 重构这个函数,拼接出users
        json_data = pub.load_json(USERS_FILE_NAME)
        print('用户文件数据是:{}'.format(json_data))
        users = []
        for key, value in json_data.items():
            users.append({USERNAME: key, PASSWORD: value})
        # users = [
        #     {USERNAME: 'admin', PASSWORD: 'admin'},
        #     ]
        print("所有用户信息是:{}".format(users))
        return users

    @staticmethod
    def save_user(username, password):
        # 重构这个函数，保存用户名密码

        success = True
        msg = ''
        try:
            json_data = pub.load_json(USERS_FILE_NAME)
            json_data[username] = password
            pub.write_dict(USERS_FILE_NAME, json_data, encoding='utf-8')
        except Exception as e:
            success = False
            msg = '保存到文件失败{}'.format(e)
            pass
        return success, msg

    def __init__(self, window, title='信息认证', head='学生成绩管理系统', width=600, height=450):
        self.window = window
        self.user_entry = None  # 用户名输入框
        self.pwd_entry = None  # 密码输入框

        window.title(title)  # 设置标题
        common.set_size_center(window, width, height)  # 设置位置大小
        self.set_frame(head)

    def login(self):
        username = self.user_entry.get().strip().lower()  # 获取用户名
        password = self.pwd_entry.get().strip().lower()  # 获取密码
        if username == '' or password == '':
            messagebox.showwarning('提示信息', '请输入用户名和密码!')
        else:
            users = self.set_users()  # 获取所有用户
            can_login = False
            for user in users:
                usr = user.get(USERNAME)
                pwd = user.get(PASSWORD)
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
        if username == '' or password == '':
            messagebox.showwarning('提示信息', '请输入用户名和密码!')
            return
        users = self.set_users()  # 获取所有用户
        names = []
        for user in users:
            usr = user.get(USERNAME)
            if usr:
                names.append(usr)  # 所有用户名
        if username in names:
            messagebox.showwarning('提示信息', '用户名已存在!')
        else:
            success, msg = self.save_user(username, password)  # 保存用户名密码
            if success:
                messagebox.showinfo('提示信息', '恭喜你注册成功!')
            else:
                messagebox.showinfo('提示信息', '注册失败!\n异常信息:{}'.format(msg))

    def set_frame(self, title):
        # self.window.resizable(0, 0)
        frame = tkinter.Frame(self.window)
        title_label = Label(self.window, text=title, font=('黑体', 26))
        size = 20
        user_label = tkinter.Label(frame, text='用户名', font=('', size))
        pwd_label = tkinter.Label(frame, text='密  码', font=('', size))
        width = 16
        self.user_entry = tkinter.Entry(frame, font=('', size), width=width)
        self.user_entry.focus()
        self.user_entry.bind(RETURN, lambda x: self.pwd_entry.focus())
        self.pwd_entry = tkinter.Entry(frame, show='*', font=('', size), width=width)
        register_btn = tkinter.Button(frame, text='注册', bg='#ff8000', font=('', size), command=self.register)
        login_btn = tkinter.Button(frame, text='登录', bg='green', font=('', size), command=self.login)
        self.pwd_entry.bind(RETURN, lambda x: self.login())
        title_label.pack(side=tkinter.TOP, padx=10, pady=40)
        frame.pack()
        padx = 5
        pady = 20
        user_label.grid(row=0, column=0, padx=padx, pady=0)
        pwd_label.grid(row=1, column=0, padx=padx, pady=pady)
        self.user_entry.grid(row=0, column=1, padx=padx, pady=pady)
        self.pwd_entry.grid(row=1, column=1, padx=padx, pady=pady)
        pady2 = 40
        register_btn.grid(row=2, column=0, padx=10, pady=pady2)
        login_btn.grid(row=2, column=1, padx=10, pady=pady2, sticky='e')


if __name__ == '__main__':
    win = tkinter.Tk()
    login_window = LoginFrame(win)
    win.mainloop()
