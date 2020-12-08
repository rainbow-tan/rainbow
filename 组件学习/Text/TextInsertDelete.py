# -*- encoding=utf-8 -*-

import tkinter
from tkinter import *


def end_insert():
    text.insert('end', 'A')  # 插入到末尾


def point_insert():
    text.insert('insert', 'B')  # 插入到光标处


def insert_x_y():
    # 插入指定位置(x.y)，1.0表示1行1列，1.2表示1行3列，行x从1开始，列y从0开始
    # 如果x.y之前没内容，则添加到前面
    text.insert(1.2, 'C')


def get():
    # 获取输入的信息(x.y)，1.0表示1行1列，1.2表示1行3列，行x从1开始，列y从0开始
    msg = text.get(1.0, 1.6)  # 获取1行1列至1行7列
    print('1行1列至1行7列:{}'.format(msg))
    msg = text.get(1.0, '1.end')  # 获取1行1列至1行末尾
    print('1行1列至1行末尾:{}'.format(msg))
    msg = text.get(1.4, '2.end')  # 获取1行5列至2行末尾
    print('获取1行5列至2行末尾:{}'.format(msg))
    msg = text.get(1.2, 'end')  # 获取1行3列至内容结尾
    print('获取1行3列至内容结尾:{}'.format(msg))


def delete():
    text.delete(1.0, 1.6)  # 删除1行1列至1行7列
    text.delete(1.0, '1.end')  # 删除1行1列至1行末尾
    text.delete(1.4, '2.end')  # 删除1行5列至2行末尾
    text.delete(1.2, 'end')  # 删除1行3列至内容结尾


if __name__ == '__main__':
    win = tkinter.Tk()  # 窗口
    win.title('南风丶轻语')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 500
    height = 300
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

    text = Text(
            master=win,  # 父容器
            bg='pink',  # 背景颜色
            fg='red',  # 文本颜色
            relief='sunken',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            bd=3,  # 边框的大小
            width=5,  # 宽度
            height=5,  # 高度
            state='normal',  # 设置状态 normal、readonly、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('黑体', 20),  # 字体
            wrap='char',  # 字数够width后是否换行 char, none,  word
            )
    text.pack()
    Button(text='插入到末尾', command=end_insert).pack()
    Button(text='插入到鼠标位置', command=point_insert).pack()
    Button(text='插入到几行几列', command=insert_x_y).pack()
    Button(text='获取输入的信息', command=get).pack()
    Button(text='删除', command=delete).pack()
    win.mainloop()
