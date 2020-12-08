import tkinter
from tkinter import *

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

        checkbutton = Checkbutton(
                master=win,  # 父容器
                text=value,  # 文本
                bg='yellow',  # 背景颜色
                fg='red',  # 文本颜色
                activebackground='pink',  # 状态为active时的背景颜色
                activeforeground='blue',  # 状态为active的文字颜色
                relief=value,  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
                bd=3,  # 边框的大小
                height=1,  # 高度
                width=10,  # 宽度
                padx=1,  # 内间距，字体与边框的X距离
                pady=1,  # 内间距，字体与边框的Y距离
                state='normal',  # 设置状态 normal、active、 disabled
                cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
                font=('Yu Gothic Medium', 15),  # 字体
                )
        checkbutton.grid(row=0, column=index, padx=10, pady=10)

    values = ['normal', 'active', 'disabled']
    for index, value in enumerate(values):
        checkbutton = Checkbutton(
                master=win,  # 父容器
                text=value,  # 文本
                bg='yellow',  # 背景颜色
                fg='red',  # 文本颜色
                activebackground='pink',  # 状态为active时的背景颜色
                activeforeground='blue',  # 状态为active的文字颜色
                relief='flat',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
                bd=3,  # 边框的大小
                height=1,  # 高度
                width=10,  # 宽度
                padx=1,  # 内间距，字体与边框的X距离
                pady=1,  # 内间距，字体与边框的Y距离
                state=value,  # 设置状态 normal、active、 disabled
                cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
                font=('Yu Gothic Medium', 15),  # 字体
                )
        checkbutton.grid(row=1, column=index, padx=10, pady=10)

    win.mainloop()
