# -*- encoding=utf-8 -*-
import tkinter
from tkinter import *


def keyboard_event(event):
    char = event.char
    print('回车 char:{}'.format(char))
    key_code = event.keycode
    print('回车 key code:{}'.format(key_code))


def entry_enter(event):
    print('输入的内容为:' + entry.get())


def shift_f(event):
    print('SHIFT + F')
    print(event.char)
    print(event.keycode)


def num_lock(event):
    print('num_lock')
    print(event.char)
    print(event.keycode)


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

    label = Label(text='标签', relief='g', font=('黑体', 20))
    label.pack(pady=10)
    label.focus_set()
    label.bind('<Return>', keyboard_event)  # 按下回车
    label.bind('<Shift F>', shift_f)
    label.bind('<Num_Lock>', num_lock)

    entry = Entry()
    entry.pack()
    entry.bind('<Return>', entry_enter)  # 按下回车

    win.mainloop()
