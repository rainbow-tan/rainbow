import json
import os
import tkinter
from datetime import datetime
from threading import Timer
from tkinter import *
from tkinter import messagebox

from PIL import Image
from PIL import ImageTk


def prinTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    t = Timer(inc, prinTime, (inc,))
    t.start()
    t.cancel()


def login():
    user = a.get().strip()
    pwd = b.get().strip()
    # print('user:{}'.format(user))
    # print('pwd:{}'.format(pwd))
    if user == '' or pwd == '':
        messagebox.showwarning('提示信息', '请输入用户名和密码！')
        return
    with open('user', encoding='utf-8') as f:
        users = json.load(f)
    # print('用户:{}'.format(users))
    if user in users and users[user] == pwd:
        print('可以登录')
        win.destroy()
        os.system('python jsq.py')
    else:
        messagebox.showerror('提示信息', '用户名或密码错误！')
    pass


def register():
    user = a.get().strip()
    pwd = b.get().strip()
    # print('user:{}'.format(user))
    # print('pwd:{}'.format(pwd))
    if user == '' or pwd == '':
        messagebox.showwarning('提示信息', '请输入用户名和密码！')
        return
    with open('user', encoding='utf-8') as f:
        users = json.load(f)
    if user not in users:
        users[user] = pwd
        with open('user', 'w', encoding='utf-8') as f:
            json.dump(users, f)
        messagebox.showinfo('提示信息', '恭喜你注册成功!')
    else:
        messagebox.showwarning('提示信息', '用户名已存在，注册失败!')
    pass


if __name__ == '__main__':

    win = tkinter.Tk()
    win.title('个人DIV计算器')
    screenwidth = win.winfo_screenwidth()
    screenheight = win.winfo_screenheight()
    width = 500
    height = 500
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置
    win.resizable(0, 0)

    img_open = Image.open('user48.png')
    img = ImageTk.PhotoImage(img_open)
    img_open1 = Image.open('pwd48.png')
    img1 = ImageTk.PhotoImage(img_open1)
    img2 = ImageTk.PhotoImage(Image.open('进入.png'))
    img3 = ImageTk.PhotoImage(Image.open('注册1.png'))

    Label(win, text='欢迎使用', font=('楷体', 20)).pack(pady=20)
    frame = Frame(win, )

    frame.pack()
    Label(frame, image=img).grid(row=0, column=0, pady=30)
    Label(frame, image=img1).grid(row=1, column=0)
    a = Entry(frame, font=('', 20))
    a.grid(row=0, column=1, padx=30)
    b = Entry(frame, font=('', 20), show='*')
    b.grid(row=1, column=1, padx=30, pady=40)

    frame1 = Frame(win, )
    frame1.pack()
    Button(frame1, image=img3, relief='groove', command=register).grid(row=2, column=0, padx=90,
                                                                       pady=40)
    Button(frame1, image=img2, command=login).grid(row=2, column=2, padx=90, pady=40)

    win.mainloop()
