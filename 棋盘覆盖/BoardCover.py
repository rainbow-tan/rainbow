# -*- encoding=utf-8 -*-
import math
import time
import tkinter
import tkinter.colorchooser as color
from tkinter import *

shunxu_cur = 0


class chessboard:

    def __init__(self, sx, sy, k):
        self.sx = sx
        self.sy = sy
        self.size = pow(2, k)
        self.chess = [[-1 for i in range(self.size)] for i in range(self.size)]
        self.shunxu = {}
        global shunxu_cur
        shunxu_cur = 0
        self.count = [0 for i in range(10)]
        self.draw(0, 0, self.size, self.sx, self.sy)
        self.calc_var()
        self.show()
        self.pr()

    def draw(self, m, n, c, x, y):
        """
        @param m,n 棋盘坐上定点横纵坐标
        @param x,y: 残缺方格的坐标
        @param c: 棋盘尺寸
        """
        global shunxu_cur
        if c <= 1:
            return
        cm = m - 1 + int(c / 2)
        cn = n - 1 + int(c / 2)
        if x <= cm and y <= cn:
            x1 = cm + 1
            y1 = cn
            x2 = cm
            y2 = cn + 1
            x3 = cm + 1
            y3 = cn + 1
            self.chess[y1][x1] = 1
            self.chess[y2][x2] = 1
            self.chess[y3][x3] = 1
            self.shunxu[shunxu_cur] = {0: [y1, x1], 1: [y2, x2], 2: [y3, x3]}
            shunxu_cur += 1

            self.draw(m, n, int(c / 2), x, y)
            self.draw(cm + 1, n, int(c / 2), x1, y1)
            self.draw(m, cn + 1, int(c / 2), x2, y2)
            self.draw(cm + 1, cn + 1, int(c / 2), x3, y3)
            return
        if x <= cm and y > cn:
            x1 = cm
            y1 = cn
            x2 = cm + 1
            y2 = cn
            x3 = cm + 1
            y3 = cn + 1
            self.chess[y1][x1] = 3
            self.chess[y2][x2] = 3
            self.chess[y3][x3] = 3
            self.shunxu[shunxu_cur] = {0: [y1, x1], 1: [y2, x2], 2: [y3, x3]}
            shunxu_cur += 1

            self.draw(m, n, int(c / 2), x1, y1)
            self.draw(cm + 1, n, int(c / 2), x2, y2)
            self.draw(m, cn + 1, int(c / 2), x, y)
            self.draw(cm + 1, cn + 1, int(c / 2), x3, y3)
            return

        if x > cm and y <= cn:
            x1 = cm
            y1 = cn
            x2 = cm
            y2 = cn + 1
            x3 = cm + 1
            y3 = cn + 1

            self.chess[y1][x1] = 2
            self.chess[y2][x2] = 2
            self.chess[y3][x3] = 2
            self.shunxu[shunxu_cur] = {0: [y1, x1], 1: [y2, x2], 2: [y3, x3]}
            shunxu_cur += 1

            self.draw(m, n, int(c / 2), x1, y1)
            self.draw(cm + 1, n, int(c / 2), x, y)
            self.draw(m, cn + 1, int(c / 2), x2, y2)
            self.draw(cm + 1, cn + 1, int(c / 2), x3, y3)
            return

        if x > cm and y > cn:
            x1 = cm
            y1 = cn
            x2 = cm + 1
            y2 = cn
            x3 = cm
            y3 = cn + 1

            self.chess[y1][x1] = 4
            self.chess[y2][x2] = 4
            self.chess[y3][x3] = 4

            self.shunxu[shunxu_cur] = {0: [y1, x1], 1: [y2, x2], 2: [y3, x3]}
            shunxu_cur += 1

            self.draw(m, n, c / 2, x1, y1)
            self.draw(cm + 1, n, c / 2, x2, y2)
            self.draw(m, cn + 1, c / 2, x3, y3)
            self.draw(cm + 1, cn + 1, c / 2, x, y)
            return

    def calc_var(self):
        """
        计算4种三角板的数量，存在count数组内
        """
        for i in range(self.size):
            for j in range(self.size):
                self.count[self.chess[i][j]] += 1

        for i in range(4):
            self.count[i + 1] = int(self.count[i + 1] / 3)
            # print(self.count[i + 1])

        # def calc_size(k):
        """
        @param k用户输入的棋盘尺寸  k=log2(row_size),一般范围是[1,10]，整数。
        """
        # return pow(2, k)

    def show(self):  #
        """
        @param t 原始生成的棋盘,t[y][x]代表(x,y)的种类   t[y][x]∈【1,4】
        11 12
        """
        for i in range(self.size):
            for j in range(self.size):
                print("%d\t" % self.chess[j][i], end="")
            print("\n")

        for i in range(4):
            print(self.count[i + 1])

    def pr(self):
        """
        shunxu字典中按显示顺序存储着每次要显示的三个坐标对   shunxu[id][i][0]和shunxu[id][i][1]分别代表第id次画出的第i个格子的纵坐标！！（这里注意一下，先是纵坐标）  和  横坐标
        """
        for i in range(shunxu_cur):
            for j in range(3):
                print(self.shunxu[i][j][1], self.shunxu[i][j][0])
                print('类型:{}'.format(self.chess[self.shunxu[i][j][0]][self.shunxu[i][j][1]]))
                ty = self.chess[self.shunxu[i][j][0]][self.shunxu[i][j][1]]
                if ty == 1:
                    bg = button1.cget('bg')
                elif ty == 2:
                    bg = button2.cget('bg')
                elif ty == 3:
                    bg = button3.cget('bg')
                elif ty == 4:
                    bg = button4.cget('bg')
                buttons[self.shunxu[i][j][1]][self.shunxu[i][j][0]].config(bg=bg)
                buttons[self.shunxu[i][j][1]][self.shunxu[i][j][0]].update()
            print("===========\n")
            time.sleep(time_sleep)


def button1_event():
    current_color = button1.cget('bg')
    bg = color.askcolor()[1]
    button1.config(bg=bg)
    for i in buttons:
        for j in i:
            if j.cget('bg') == current_color:
                j.config(bg=bg)


def button2_event():
    current_color = button2.cget('bg')
    bg = color.askcolor()[1]
    button2.config(bg=bg)
    for i in buttons:
        for j in i:
            if j.cget('bg') == current_color:
                j.config(bg=bg)


def button3_event():
    current_color = button3.cget('bg')
    bg = color.askcolor()[1]
    button3.config(bg=bg)
    for i in buttons:
        for j in i:
            if j.cget('bg') == current_color:
                j.config(bg=bg)


def button4_event():
    current_color = button4.cget('bg')
    bg = color.askcolor()[1]
    button4.config(bg=bg)
    for i in buttons:
        for j in i:
            if j.cget('bg') == current_color:
                j.config(bg=bg)


def button5_event():
    current_color = button5.cget('bg')
    bg = color.askcolor()[1]
    button5.config(bg=bg)
    for i in buttons:
        for j in i:
            if j.cget('bg') == current_color:
                j.config(bg=bg)


def lone(event):
    button1.config(text='A类形状（0）个')
    button2.config(text='A类形状（0）个')
    button3.config(text='A类形状（0）个')
    button4.config(text='A类形状（0）个')
    me = event.widget
    me_text = event.widget['text']
    index_x, index_y = me_text.split(',')
    index_x = int(index_x)
    index_y = int(index_y)
    for i in buttons:
        for j in i:
            j.config(bg='SystemButtonFace')
    btn5_color = button5.cget('bg')
    buttons[index_x][index_y].config(bg=btn5_color)
    global number
    # print('index_x:{}'.format(index_x))
    # print('index_y:{}'.format(index_y))
    # print('number:{}'.format(number))
    # print('速度:{}'.format(int_value.get()))
    s = int_value.get()
    # s = 0.2
    global time_sleep
    time_sleep = s
    global shunxu_cur
    shunxu_cur = 0

    cb = chessboard(index_x, index_y, number, )
    button1.config(text='A类形状（{}）个'.format(cb.count[1]))
    button2.config(text='A类形状（{}）个'.format(cb.count[2]))
    button3.config(text='A类形状（{}）个'.format(cb.count[3]))
    button4.config(text='A类形状（{}）个'.format(cb.count[4]))


number = 0
time_sleep = 1


def begin():
    # 销毁原有的按钮
    global buttons
    for one_group_button in buttons:
        for one in one_group_button:
            one.destroy()

    buttons = []

    k_value = entry_k.get()
    global number
    number = k_value
    try:
        number = int(float(k_value))
    except Exception as e:
        # messagebox.showinfo('提示信息', '请输入整数')
        return
    buttons = []
    count = int(math.pow(2, number))
    row = 0
    column = 0
    button_group = []
    for i in range(count * count):
        text = '{},{}'.format(row, column)
        btn = Label(ff, text=text, width=5, height=2, relief='g', bd=2)
        button_group.append(btn)
        btn.bind("<Button-1>", lone)
        btn.grid(row=row, column=column, )
        column += 1
        if column % count == 0 and column != 0:
            row += 1
            column = 0
            buttons.append(button_group)
            button_group = []


if __name__ == '__main__':
    win = tkinter.Tk()  # 窗口
    win.title('南风丶轻语')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 800
    height = 900
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

    f = tkinter.Frame()
    f.pack()

    f1 = tkinter.Frame(f, bd=1, relief='groove')
    f11 = tkinter.Frame(f1)
    f11.pack()
    Label(f11, text='K').grid(row=0, column=0, )
    entry_k = Entry(f11, width=10)
    # entry_k.insert('0', '2')
    entry_k.grid(row=0, column=1, padx=10, pady=10)
    f12 = tkinter.Frame(f1, )
    f12.pack(fill=X)
    button5 = Button(f12, text='空缺颜色', command=button5_event, bg='#0000ff')
    button5.pack(fill=X)
    Button(f12, text='开始', command=begin, bg='pink').pack(fill=X)
    f1.grid(row=0, column=0, )

    f2 = tkinter.Frame(f, bd=2, relief='groove')
    button1 = Button(f2, text='A类形状（0）个', bg='#ff0000', command=button1_event)
    button1.grid(row=0, column=0, padx=10, pady=10)
    button2 = Button(f2, text='B类形状（0）个', bg='#ff8040', command=button2_event)
    button2.grid(row=0, column=1)
    button3 = Button(f2, text='C类形状（0）个', bg='#ffff00', command=button3_event)
    button3.grid(row=1, column=0)
    button4 = Button(f2, text='D类形状（0）个', bg='#00ff00', command=button4_event)
    button4.grid(row=1, column=1, padx=10, pady=10)
    f2.grid(row=0, column=1, padx=30)

    f3 = tkinter.Frame(f, bd=2, relief='groove')
    int_value = tkinter.IntVar()
    int_value.set(1)
    Radiobutton(f3, text='缓慢', variable=int_value, value=3).grid(row=0, column=0)
    Radiobutton(f3, text='慢', variable=int_value, value=2.5).grid(row=1, column=0, pady=10)
    Radiobutton(f3, text='适中', variable=int_value, value=2).grid(row=2, column=0, )
    Radiobutton(f3, text='快', variable=int_value, value=1.5).grid(row=0, column=1)
    Radiobutton(f3, text='较快', variable=int_value, value=1).grid(row=1, column=1, pady=10)
    Radiobutton(f3, text='更快', variable=int_value, value=0.5).grid(row=2, column=1, )
    f3.grid(row=0, column=2)

    buttons = []
    ff = Frame(win, bd=2, relief='flat')

    ff.pack()

    win.mainloop()
