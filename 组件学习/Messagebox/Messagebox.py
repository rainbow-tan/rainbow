# -*- encoding=utf-8 -*-
import tkinter
from tkinter import messagebox


def event():
    ret = messagebox.showinfo('提示信息', '你看我还有机会吗？')
    print('ret:{}'.format(ret))
    ret = messagebox.showwarning('提示信息', '你看我还有机会吗？')
    print('ret:{}'.format(ret))
    ret = messagebox.showerror('提示信息', '你看我还有机会吗？')
    print('ret:{}'.format(ret))
    ret = messagebox.askyesno('提示信息', '你看我还有机会吗？')
    print('ret:{}'.format(ret))
    ret = messagebox.askretrycancel('提示信息', '你看我还有机会吗？')
    print('ret:{}'.format(ret))
    ret = messagebox.askquestion('提示信息', '你看我还有机会吗？')
    print('ret:{}'.format(ret))
    ret = messagebox.askokcancel('提示信息', '你看我还有机会吗？')
    print('ret:{}'.format(ret))
    ret = messagebox.askyesnocancel('提示信息', '你看我还有机会吗？')
    print('ret:{}'.format(ret))


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

    tkinter.Button(text='点击', command=event).pack()

    win.mainloop()
