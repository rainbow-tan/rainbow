# -*- encoding=utf-8 -*-
from tkinter import *
from tkinter import messagebox

import common
import page2


def page1(win):
    def begin_use():
        print('开始使用')  # 开始使用按钮
        common.clear_child(win)  # 清空控件
        page2.usingpage(win)

    def introduce():
        print('软件介绍')
        msg = "识别相似的签名\n同文件夹下比较\n可拍照保存~~\n按下S保存~~\n按下Q退出~~\n可手动选择~~\n开始使用叭~~"
        messagebox.showinfo('提示信息', msg)

    common.set_size_center(win, 400, 350)
    f = Frame()
    f.pack()
    label = Label(
        master=win,  # 父容器
        text='签名识别软件',  # 文本
        font=('宋体', 30),  # 字体
        )
    label.pack(pady=(20, 0))

    f1 = Frame()
    f1.pack()
    button = Button(
        master=f1,  # 父容器
        text='开始使用',  # 文本
        relief='g',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。默认为 raised。
        bd=2,  # 边框的大小
        height=1,  # 高度
        padx=1,  # 内间距，字体与边框的X距离
        pady=1,  # 内间距，字体与边框的Y距离
        state='normal',  # 设置状态 normal、active、 disabled 默认 normal
        cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
        font=('黑体', 20),  # 字体
        command=begin_use,  # 点击事件
        )
    button.pack(pady=(100, 0))
    f2 = Frame()
    f2.pack()
    button1 = Button(
        master=f2,  # 父容器
        text='软件介绍',  # 文本
        relief='g',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。默认为 raised。
        bd=2,  # 边框的大小
        height=1,  # 高度
        padx=1,  # 内间距，字体与边框的X距离
        pady=1,  # 内间距，字体与边框的Y距离
        state='normal',  # 设置状态 normal、active、 disabled 默认 normal
        cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
        font=('黑体', 20),  # 字体
        command=introduce,  # 点击事件
        )
    button1.pack(pady=(30, 0))


if __name__ == '__main__':
    tk = Tk()
    page1(tk)
    tk.mainloop()
