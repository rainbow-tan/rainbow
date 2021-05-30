# -*- encoding=utf-8 -*-
def set_size_center(window, width=400, height=500):
    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    #设置屏幕居中
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
