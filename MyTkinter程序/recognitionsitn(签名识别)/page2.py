# -*- encoding=utf-8 -*-
import os
from tkinter import *
import tkinter.colorchooser as cc
from tkinter.filedialog import askopenfilename

from PIL import Image
from PIL import ImageTk

import common
import compare
import page1
from photograph import take_a_picture

img = None
path = None


def usingpage(tk):
    def shibie():
        global path
        text = compare.function2(os.path.dirname(path), os.path.basename(path))
        text_result.delete(0.0, END)
        text_result.insert('end', text)

    def choose_color():
        choose = cc.askcolor()
        print(choose)
        color_value = choose[1]
        text_result.config(bg=color_value)

    def take_photo():
        global img
        global path
        print('进入拍照程序入口')
        path = take_a_picture()
        print('path:{}'.format(path))
        if path:
            img = ImageTk.PhotoImage(Image.open(path).resize((500, 400), Image.ANTIALIAS))
            lable_img.config(image=img)
            text_result.delete(0.0, END)

    def bendi():
        global img
        global path
        print('选择本地照片程序入口')
        path = askopenfilename()
        print('path:{}'.format(path))
        if path:
            img = ImageTk.PhotoImage(Image.open(path).resize((500, 400), Image.ANTIALIAS))
            lable_img.config(image=img)
            text_result.delete(0.0, END)
        pass

    def fanhui():
        # 返回按钮
        common.clear_child(tk)
        page1.page1(tk)
        pass

    common.set_size_center(tk, 800, 700)
    f_top = Frame()
    f_top_left = Frame(f_top, width=400, bg='pink', height=100)
    f_top_left.propagate(False)
    label_pai = Label(f_top_left, text='摄像头拍照', width=10, bg='#ff00ff', height=2, font=('', 16))
    label_pai.pack()
    btn_pai = Button(f_top_left, bg='#ff8000', width=10, height=2, text='拍  照', command=take_photo)
    btn_pai.pack()
    f_top_left.pack(side=LEFT, fill=X)

    f_top_right = Frame(f_top, width=400, height=100, bg='yellow')
    f_top_right.propagate(False)
    label_bendi = Label(f_top_right, text='本地照片', width=10, height=2, bg='#ff0080', font=('', 16))
    label_bendi.pack()
    btn_bendi = Button(f_top_right, bg='#f5010a', width=10, height=2, text='选 择', command=bendi)
    btn_bendi.pack()
    f_top_right.pack(side=LEFT, fill=X)
    f_top.pack()

    f_middle = Frame(width=500, height=400, bd=2, relief='g')
    f_middle.propagate(False)
    lable_img = Label(f_middle)
    lable_img.pack(fill=BOTH, expand=True)
    f_middle.pack()

    f_bootm = Frame()
    f_bootm.pack()
    btn_shibie = Button(f_bootm, bg='#00ff00', width=10, height=2, text='识  别', command=shibie)
    btn_shibie.pack(side=LEFT)
    btn_shibie = Button(f_bootm, bg='#00ffff', width=10, height=2, text='返  回', command=fanhui)
    btn_shibie.pack(side=LEFT, padx=50)

    text_result = Text(tk, bg='#8080ff', relief='g', width=20, height=2, font=('', 10))
    text_result.pack(fill=BOTH, expand=True)


if __name__ == '__main__':
    win = Tk()
    usingpage(win)
    win.mainloop()
