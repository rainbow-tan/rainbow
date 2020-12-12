# -*- encoding=utf-8 -*-

import tkinter
from tkinter import *

if __name__ == '__main__':
    pass
    win = tkinter.Tk()  # 窗口
    win.title('南风丶轻语')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 400
    height = 500
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

    all_count = 20
    line_count = 4
    color = ['red', 'blue', 'yellow', 'pink', 'green']
    color_index = 0
    for j in range(int(all_count / line_count)):
        f = Frame()
        f.pack(fill=BOTH, expand=True)
        for i in range(line_count):
            Button(f, text='排列按钮', bg=color[color_index]).pack(side='left', expand='true',
                                                               fill=BOTH)
            color_index += 1
            if color_index >= len(color):
                color_index = 0

    win.mainloop()
