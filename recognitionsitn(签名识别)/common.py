# -*- encoding=utf-8 -*-


def set_size_position(window, width=400, height=500, x=0, y=0):
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 设置界面大小和位置


def set_size_center(window, width=400, height=500):
    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 设置界面居中


def set_title(window, title):
    window.title(title)  # 设置界面标题


def clear_child(window):
    # 获取子控件并清空
    for child in window.children.values():
        try:
            child.pack_forget()  # 清空pack
        except:
            pass
        try:
            child.grid_forget()  # 清空grid
        except:
            pass
        try:
            child.place_forget()  # 清空place
        except:
            pass
