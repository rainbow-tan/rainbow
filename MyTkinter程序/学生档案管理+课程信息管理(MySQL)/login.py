import socket
import tkinter
from tkinter import *
from tkinter import messagebox

from common import *
import main_page
import register

USERNAME = 'username'
PASSWORD = 'password'
RETURN = '<Return>'


class LoginFrame(object):

    @staticmethod
    def set_users():
        users, msg = mysqltool.select(mysqltool.conn_db, 'useraccount', ['account', 'password'], {})
        # users = [
        #     {'account': '1', 'password': '1'},
        #     {'account': 'admin', 'password': 'admin'},
        #     ]
        return users

    def __init__(self, window, title='欢迎使用', head='数据管理系统', width=600, height=450):
        self.window = window
        self.user_entry = None  # 用户名输入框
        self.pwd_entry = None  # 密码输入框

        window.title(title)  # 设置标题
        set_size_center(window, width, height)  # 设置位置大小
        self.set_frame(head)

    @staticmethod
    def user_history(account, visitdate):
        ip = socket.gethostbyname(socket.gethostname())
        insert_data = dict(account=account, ip=ip, visitdate=visitdate)
        mysqltool.insert(mysqltool.conn_db, 'userhistory', insert_data)
        pass

    def login(self):
        username = self.user_entry.get().strip().lower()  # 获取用户名
        password = self.pwd_entry.get().strip().lower()  # 获取密码
        if username == '' or password == '':
            messagebox.showwarning('提示信息', '请输入用户名和密码!')
            return
            # else:
        users = self.set_users()  # 获取所有用户
        can_login = False
        for user in users:
            usr = user.get('account')
            pwd = user.get('password')
            if username == usr.lower() and password == pwd.lower():
                can_login = True  # 可以登录

        if can_login:
            visitdate = mytool.now('%Y-%m-%d %H:%M:%S')  # 最新访问时间设置
            mysqltool.update(mysqltool.conn_db, 'useraccount', {'visitdate': visitdate},
                             {'account': username})
            current_login_user.CURRENT_LOGIN_ACCOUNT = username  # 保存当前登录的账号,用于退出时间的处理
            self.user_history(username, visitdate)  # 记录历史登录数据
            clear_child(self.window)
            main_page.MainPage(self.window)
        else:
            messagebox.showerror('提示信息', '用户名或密码错误!')

    def register(self):
        clear_child(self.window)  # 清空组件
        register.MyFrame(self.window)  # 返回登录页面

    def set_frame(self, title):
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
        register_btn = tkinter.Button(frame, text='注册', bg='#ff8000', font=('', size),
                                      command=self.register)
        login_btn = tkinter.Button(frame, text='登录', bg='green', font=('', size),
                                   command=self.login)
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
    pass
    win = tkinter.Tk()
    login_window = LoginFrame(win)
    win.mainloop()
