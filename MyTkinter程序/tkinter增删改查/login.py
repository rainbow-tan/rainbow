# -*- encoding=utf-8 -*-
import tkinter
import PublicMethod
from tkinter import *
from select import SelectFrame


class LoginFrame(object):
    def __init__(self, window):
        self.window = window
        self.user_entry = None
        self.pwd_entry = None

    def login(self):
        user = self.user_entry.get()
        pwd = self.pwd_entry.get()
        print('user:{}'.format(user))
        print('pwd:{}'.format(pwd))
        # 移除界面上的控件
        PublicMethod.clear_child(self.window, 'pack')

        # 跳转到其他页面
        select_window = SelectFrame(self.window)
        PublicMethod.set_title(self.window, '查询')
        PublicMethod.set_size_center(self.window, 600, 600)
        select_window.set_frame()
        pass

    def register(self):
        user = self.user_entry.get()
        pwd = self.pwd_entry.get()
        print('user:{}'.format(user))
        print('pwd:{}'.format(pwd))
        pass

    def set_frame(self):
        frame = tkinter.Frame(self.window)
        welcome_label = Label(self.window, text='欢迎使用', font=('', 20))
        user_label = tkinter.Label(frame, text='用户名')
        pwd_label = tkinter.Label(frame, text='密码')
        login_btn = tkinter.Button(frame, text='登录', command=self.login)
        register_btn = tkinter.Button(frame, text='注册', command=self.register)
        self.user_entry = tkinter.Entry(frame)
        self.pwd_entry = tkinter.Entry(frame)

        welcome_label.pack(side=tkinter.TOP, padx=10, pady=40)
        frame.pack()

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
    PublicMethod.set_size_center(login_window.window, 300, 350)
    login_window.set_frame()
    main_win.mainloop()
