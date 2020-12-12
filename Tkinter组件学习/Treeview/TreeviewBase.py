# -*- encoding=utf-8 -*-

import tkinter
from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    pass
    win = tkinter.Tk()  # 窗口
    win.title('南风丶轻语')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 1000
    height = 500
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

    columns = ['学号', '姓名', '性别', '出生年月', '籍贯', '班级']
    table = ttk.Treeview(
            master=win,  # 父容器
            height=10,  # 高度,可显示height行
            columns=columns,  # 显示的列
            show='headings'
            )
    table.heading('学号', text='学号', )  # 定义表头
    table.heading('姓名', text='姓名', )  # 定义表头
    table.heading('性别', text='性别', )  # 定义表头
    table.heading('出生年月', text='出生年月', )  # 定义表头
    table.heading('籍贯', text='籍贯', )  # 定义表头
    table.heading('班级', text='班级', )  # 定义表头
    table.column('学号', width=100, anchor=S)  # 定义列
    table.column('姓名', width=150, anchor=S)  # 定义列
    table.column('性别', width=50, anchor=S)  # 定义列
    table.column('出生年月', width=150, anchor='S')  # 定义列
    table.column('籍贯', width=150, anchor=S)  # 定义列
    table.column('班级', width=150, anchor=S)  # 定义列
    table.pack(pady=20)

    win.mainloop()
