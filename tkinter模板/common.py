# -*- encoding=utf-8 -*-
import tkinter


def set_size_position(window, width=400, height=500, x=0, y=0):  # 设置窗口位置
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 放置窗口


def middle_windows(window, width=400, height=500):  # 设置窗口居中
    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    x = int((screenwidth - width) / 2)  # x轴坐标
    y = int((screenheight - height) / 2)  # y轴坐标
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 放置窗口
    window.update()  # 更新窗口


def set_title(window, title):  # 设置窗口标题
    window.title(title)  # 设置窗口标题


def clear_child(window):  # 清除父窗口所有的组件
    for child in window.children.values():  # 获取并遍历所有孩子
        try:
            child.pack_forget()  # 取消pack放置的组件
        except:
            pass
        try:
            child.grid_forget()  # 取消grid放置的组件
        except:
            pass
        try:
            child.place_forget()  # 取消place放置的组件
        except:
            pass


if __name__ == '__main__':
    win = tkinter.Tk()
    middle_windows(win)
    set_title(win, '标题')
    win.mainloop()
