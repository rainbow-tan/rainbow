# -*- encoding=utf-8 -*-


import tkinter
from tkinter import *

if __name__ == '__main__':
    pass
    w = tkinter.Tk()  # 窗口
    w.title('测试')  # 标题
    w.geometry('200x100+30+30')  # 大小以及位置
    Button(w, text='按钮1', bg='red').pack(
            fill=X,  # 填充横坐标
            )
    Button(w, text='按钮2', bg='yellow').pack()
    Button(w, text='按钮3', bg='blue').pack()
    w.mainloop()
