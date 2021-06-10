# -*- encoding=utf-8 -*-
import json
import tkinter
from datetime import datetime
from threading import Timer
from tkinter import *
from tkinter import messagebox

import PublicMethod
from select import SelectFrame


class LoginFrame(object):
    def __init__(self, window):
        self.window = window
        self.user_entry = None
        self.pwd_entry = None
        self.timer = None
        self.label1 = None

    def login(self):
        user = self.user_entry.get().strip()
        pwd = self.pwd_entry.get().strip()
        # print('user:{}'.format(user))
        # print('pwd:{}'.format(pwd))
        if user == '' or pwd == '':
            messagebox.showwarning('提示信息', '请输入用户名和密码！')
            return
        with open('user.json', encoding='utf-8') as f:
            users = json.load(f)
        # print('用户:{}'.format(users))
        if user in users and users[user] == pwd:
            # 移除界面上的控件
            PublicMethod.clear_child(self.window, 'pack')

            # 跳转到其他页面
            with open('grade', 'r', encoding='utf-8') as f:
                grade = f.readlines()
            field_data = []
            for i in grade:
                if i.strip() != '':
                    score = i.split(',')
                    one = (score[0], score[1], score[2], score[3], score[4].strip(),)
                    field_data.append(one)
            # print('所有学生信息:{}'.format(field_data))
            field_names = ['学号', '姓名', '高数', '大物', '英语']
            select_window = SelectFrame(self.window, field_names, field_data)
            PublicMethod.set_title(self.window, '查询')
            PublicMethod.set_size_center(self.window, 600, 600)
            select_window.set_frame()
            self.timer.cancel()
        else:
            messagebox.showerror('提示信息', '用户名或密码错误！')
        pass

    def real_time(self, inc):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # print(now)
        self.label1.config(text='时间:{}'.format(now))
        self.timer = Timer(inc, self.real_time, (inc,))
        self.timer.start()

    def register(self):
        user = self.user_entry.get().strip()
        pwd = self.pwd_entry.get().strip()
        # print('user:{}'.format(user))
        # print('pwd:{}'.format(pwd))
        if user == '' or pwd == '':
            messagebox.showwarning('提示信息', '请输入用户名和密码！')
            return
        with open('user.json', encoding='utf-8') as f:
            users = json.load(f)
        if user not in users:
            users[user] = pwd
            with open('user.json', 'w', encoding='utf-8') as f:
                json.dump(users, f)
            messagebox.showinfo('提示信息', '恭喜你注册成功!')
        else:
            messagebox.showwarning('提示信息', '用户名已存在，注册失败!')
        pass

    def set_frame(self):
        self.window.resizable(0, 0)
        frame = tkinter.Frame(self.window)
        frame1 = tkinter.Frame(self.window)
        Label(frame1, text='作者:南风丶轻语', font=('', 10)).pack(side=LEFT, pady=20)
        self.label1 = Label(frame1, text='时间:', font=('', 10))
        self.label1.pack(side=RIGHT)
        self.real_time(1)
        welcome_label = Label(self.window, text='学生成绩管理系统', font=('', 20))

        user_label = tkinter.Label(frame, text='用户名')
        pwd_label = tkinter.Label(frame, text='密码')
        login_btn = tkinter.Button(frame, text='登录', command=self.login)
        register_btn = tkinter.Button(frame, text='注册', command=self.register)
        self.user_entry = tkinter.Entry(frame)
        self.pwd_entry = tkinter.Entry(frame, show='*')

        welcome_label.pack(side=tkinter.TOP, padx=10, pady=40)
        frame.pack()
        frame1.pack(side=BOTTOM, fill=X)

        user_label.grid(row=0, column=0, padx=10, pady=0)
        pwd_label.grid(row=1, column=0, padx=10, pady=35)
        self.user_entry.grid(row=0, column=1, padx=10, pady=0)
        self.pwd_entry.grid(row=1, column=1, padx=10, pady=20)
        login_btn.grid(row=2, column=0, padx=10, pady=20)
        register_btn.grid(row=2, column=1, padx=10, pady=20, sticky='e')


if __name__ == '__main__':
    pass

    main_win = tkinter.Tk()
    login_window = LoginFrame(main_win)
    PublicMethod.set_title(login_window.window, '登录')
    PublicMethod.set_size_center(login_window.window, 450, 400)
    login_window.set_frame()
    main_win.mainloop()
