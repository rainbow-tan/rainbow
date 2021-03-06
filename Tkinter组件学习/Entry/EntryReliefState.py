import tkinter
from tkinter import *


def event():
    print('点击事件')


if __name__ == '__main__':
    win = tkinter.Tk()  # 窗口
    win.title('南风丶轻语')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 980
    height = 300
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

    values = ['flat', 'sunken', 'raised', 'groove', 'ridge', 'solid']
    for index, value in enumerate(values):
        entry = Entry(
                master=win,  # 父容器
                text=value,  # 文本
                bg='yellow',  # 背景颜色
                fg='red',  # 文本颜色
                relief=value,  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
                bd=5,  # 边框的大小
                width=10,  # 宽度
                state='normal',  # 设置状态 normal、readonly、 disabled
                cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
                font=('Yu Gothic Medium', 15),  # 字体
                )
        entry.grid(row=0, column=index, padx=10, pady=10)
        entry.insert('end', value)  # 插入字符串

    values = ['normal', 'readonly', 'disabled']
    for index, value in enumerate(values):
        entry = Entry(
                master=win,  # 父容器
                text=value,  # 文本
                bg='yellow',  # 背景颜色
                fg='red',  # 文本颜色
                relief='raised',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
                bd=3,  # 边框的大小
                width=10,  # 宽度
                state=value,  # 设置状态 normal、readonly、 disabled
                cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
                font=('Yu Gothic Medium', 15),  # 字体
                )
        entry.grid(row=1, column=index, padx=10, pady=10)
        entry.insert('end', value)  # 插入字符串

    win.mainloop()
