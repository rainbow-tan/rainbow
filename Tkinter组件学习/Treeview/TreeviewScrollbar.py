# -*- encoding=utf-8 -*-

import tkinter
from tkinter import *
from tkinter import ttk


def show_data():
    # 插入数据
    info = [
        ['1001', '李华', '男', '2014-01-25', '广东', '计算5班', ],
        ['1002', '小米', '男', '2015-11-08', '深圳', '计算5班', ],
        ['1003', '刘亮', '男', '2015-09-12', '福建', '计算5班', ],
        ['1004', '白鸽', '女', '2016-04-01', '湖南', '计算5班', ],
        ]
    for index, data in enumerate(info):
        table.insert('', END, values=data)


if __name__ == '__main__':
    pass
    win = tkinter.Tk()  # 窗口
    win.title('南风丶轻语')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 1200
    height = 500
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置
    frame = Frame(win)
    frame.pack()
    scrollbar_y = Scrollbar(frame, orient=VERTICAL)
    scrollbar_x = Scrollbar(frame, orient=HORIZONTAL)
    columns = ['学号', '姓名', '性别', '出生年月', '籍贯', '班级']
    table = ttk.Treeview(
            master=frame,  # 父容器
            height=10,  # 高度,可显示height行
            columns=columns,  # 显示的列
            show='headings',
            yscrollcommand=scrollbar_y.set,  # 滚动条
            xscrollcommand=scrollbar_x.set,  # 滚动条
            )
    table.heading('学号', text='学号', )  # 定义表头
    table.heading('姓名', text='姓名', )  # 定义表头
    table.heading('性别', text='性别', )  # 定义表头
    table.heading('出生年月', text='出生年月', )  # 定义表头
    table.heading('籍贯', text='籍贯', )  # 定义表头
    table.heading('班级', text='班级', )  # 定义表头
    table.column('学号', width=100, anchor=CENTER)  # 定义列
    table.column('姓名', width=150, anchor=CENTER)  # 定义列
    table.column('性别', width=50, anchor=CENTER)  # 定义列
    table.column('出生年月', width=150, anchor=CENTER)  # 定义列
    table.column('籍贯', width=150, anchor=CENTER)  # 定义列
    table.column('班级', width=150, anchor=CENTER)  # 定义列

    scrollbar_y.config(command=table.yview)
    scrollbar_x.config(command=table.xview)
    scrollbar_y.pack(side=RIGHT, fill=Y)
    scrollbar_x.pack(side=BOTTOM, fill=X)
    table.pack(fill=BOTH, expand=True)

    Button(text='显示信息', command=show_data).pack()
    win.mainloop()
