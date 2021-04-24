# -*- encoding=utf-8 -*-
import tkinter


def set_size_position(window, width=400, height=500, x=0, y=0):
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def set_size_center(window, width=400, height=500):
    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def set_title(window, title):
    window.title(title)


def clear_child(window):
    # mode_lower = mode.lower()
    # 获取子控件
    for child in window.children.values():
        try:
            child.pack_forget()
        except:
            pass
        try:
            child.grid_forget()
        except:
            pass
        try:
            child.place_forget()
        except:
            pass
        # if mode_lower == 'pack':
        #     child.pack_forget()
        # elif mode_lower == 'grid':
        #     child.grid_forget()
        # elif mode_lower == 'place':
        #     child.place_forget()
        # else:
        #     print('Invalid mode, should in [pack,grid,place]')
        #     pass


if __name__ == '__main__':
    pass
    w1 = tkinter.Tk()
    set_size_center(w1)
    # set_size_position(w1)
    set_title(w1, '嘿嘿')
    w1.mainloop()
