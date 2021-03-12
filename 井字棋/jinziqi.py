# coding=utf-8
import random
import tkinter
import tkinter.colorchooser as cc
from tkinter import *
from tkinter import messagebox


def init_win():
    win.title('Rainbow')  # 标题
    screenwidth = win.winfo_screenwidth()
    screenheight = win.winfo_screenheight()
    w_width = 500
    w_height = 256
    x = int((screenwidth - w_width) / 2)
    y = int((screenheight - w_height) / 2)
    win.resizable(0, 0)
    win.geometry('{}x{}+{}+{}'.format(w_width, w_height, x, y))  # 大小以及位置


def who_begin():
    global cells
    if people_x_o.get() == 'X':
        machine_x_o = 'O'
    else:
        machine_x_o = 'X'
    if random.randint(0, 1) == 0:  # 0是人机先下
        print('人机先下')
        number = random.randint(0, 8)
        print(number)
        print(machine_x_o)
        print(cells[number])
        # cells[number].config(bg='pink')
        cells[number].config(text=machine_x_o)
        # cells[number].update()
        # win.update()
        print(cells[number].cget('text'))
    else:
        print('人先下')


def left_mouse_down(event):
    # print('鼠标左键按下')
    # 事件的属性
    widget = event.widget
    # choose_color(widget)
    # print('触发事件的组件:{}'.format(widget))
    # print('组件颜色:{}'.format(widget.cget('bg')))
    # widget_x = event.x  # 相对于组件的横坐标x
    # print('相对于组件的横坐标:{}'.format(widget_x))
    # widget_y = event.y  # 相对于组件的纵坐标y
    # print('相对于组件的纵坐标:{}'.format(widget_y))
    # x_root = event.x_root  # 相对于屏幕的左上角的横坐标
    # print('相对于屏幕的左上角的横坐标:{}'.format(x_root))
    # y_root = event.y_root  # 相对于屏幕的左上角的纵坐标
    # print('相对于屏幕的左上角的纵坐标:{}'.format(y_root))

    # print(widget.__dict__)
    # print()
    global cells
    # print(cells.index(widget))

    global people_x_o
    var = people_x_o.get()
    if widget.cget('text') in ['X', 'O']:
        alert('该位置已经有子,请重新下')
        return
    widget.config(text=var)

    if people_x_o.get() == 'X':
        machine_x_o = 'O'
    else:
        machine_x_o = 'X'
    cells_values = obj_to_x_o()
    ret = people_is_win(cells_values, var)
    if ret == people_x_o.get():
        alert('恭喜恭喜,你获得了胜利!')
    elif ret == machine_x_o:
        alert('再接再厉,人机获得了胜利!')
    else:
        machine()


def right_mouse_down(event):
    print('鼠标左键按下')
    # 事件的属性
    widget = event.widget
    # choose_color(widget)
    print('触发事件的组件:{}'.format(widget))
    print('组件颜色:{}'.format(widget.cget('bg')))
    widget_x = event.x  # 相对于组件的横坐标x
    print('相对于组件的横坐标:{}'.format(widget_x))
    widget_y = event.y  # 相对于组件的纵坐标y
    print('相对于组件的纵坐标:{}'.format(widget_y))
    x_root = event.x_root  # 相对于屏幕的左上角的横坐标
    print('相对于屏幕的左上角的横坐标:{}'.format(x_root))
    y_root = event.y_root  # 相对于屏幕的左上角的纵坐标
    print('相对于屏幕的左上角的纵坐标:{}'.format(y_root))
    print('==========')
    print(people_x_o)
    widget.config(text=people_x_o)


def choose_color(component):
    choose = cc.askcolor()
    print(choose)
    color_value = choose[1]
    component.config(fg=color_value)


# def bind_mouse(component, mode, event):
#     component.bind(mode, event)
#     pass

def init_chessboard():
    frame = tkinter.Frame(win)
    labels = []
    # for i in range(9):
    #     labels.append(tkinter.Label(
    #             master=frame,  # 父容器
    #             text='标签',  # 文本
    #             bg='#00ff80',  # 背景颜色
    #             # fg='red',  # 文本颜色
    #             activebackground='pink',  # 状态为active时的背景颜色
    #             activeforeground='blue',  # 状态为active的文字颜色
    #             relief='groove',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。默认为 FLAT。
    #             bd=1,  # 边框的大小
    #             height=2,  # 高度
    #             width=5,  # 宽度
    #             padx=1,  # 内间距，字体与边框的X距离
    #             pady=1,  # 内间距，字体与边框的Y距离
    #             state='normal',  # 设置状态 normal、active、 disabled 默认 normal
    #             cursor='circle',  # 鼠标移动时样式 arrow, circle, cross, plus...
    #             font=('黑体', 20),  # 字体
    #             ))
    # for label in labels:
    #     label.bind('<Button-1>', left_mouse_down)  # 鼠标左键按下
    # bind_mouse(label, '<Button-1>', left_mouse_down)
    # bind_mouse(label, '<Button-3>', choose_color)

    # label.pack()
    for x in range(3):
        for y in range(3):
            label = Label(
                    master=frame,  # 父容器
                    text='',  # 文本
                    bg='#00ff80',  # 背景颜色
                    # fg='red',  # 文本颜色
                    activebackground='pink',  # 状态为active时的背景颜色
                    activeforeground='blue',  # 状态为active的文字颜色
                    relief='groove',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。默认为 FLAT。
                    bd=1,  # 边框的大小
                    height=3,  # 高度
                    width=6,  # 宽度
                    padx=1,  # 内间距，字体与边框的X距离
                    pady=1,  # 内间距，字体与边框的Y距离
                    state='normal',  # 设置状态 normal、active、 disabled 默认 normal
                    cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
                    font=('黑体', 20),  # 字体
                    )
            # label.bind('<Button-1>', left_mouse_down)  # 鼠标左键按下
            label.bind('<Button-3>', right_mouse_down)  # 鼠标左键按下
            label.grid(row=x, column=y)
            labels.append(label)
    # for label in labels:
    #     print(label)
    # frame.grid(row=0, column=0)
    frame.pack(side=LEFT)
    return labels


def init_x_o():
    frame = tkinter.Frame(win)
    Label(frame, text='玩家选择X或O', font=('', '15')).pack()
    choose = ['X', 'O']
    people_x_o.set('X')
    for i in choose:
        radiobutton_x = Radiobutton(
                master=frame,  # 父容器
                text=i,  # 文本
                bg='#ffd9ec',  # 背景颜色
                fg='#ff8000',  # 文本颜色
                activebackground='pink',  # 状态为active时的背景颜色
                activeforeground='blue',  # 状态为active的文字颜色
                relief='g',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
                bd=1,  # 边框的大小
                height=1,  # 高度
                width=8,  # 宽度
                padx=5,  # 内间距，字体与边框的X距离
                pady=1,  # 内间距，字体与边框的Y距离
                state='normal',  # 设置状态 normal、active、 disabled
                cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
                font=('黑体', 14),  # 字体
                value=i,  # 默认value，选中后会传递给variable
                variable=people_x_o,  # 通过IntVar设置1为选中,0为未选中
                # command=choose_color,  # 点击时的事件
                )

        radiobutton_x.pack(side=TOP, pady=5)
    # choose_color(radiobutton_x)
    frame.pack()


def start():
    pass

    for label in cells:
        label.config(text='')
        label.bind('<Button-1>', left_mouse_down)  # 鼠标左键按下
    who_begin()


def init_start():
    frame = Frame(win)
    btn = Button(text='开始', font=('', 16), width=10, command=start)
    btn.pack()
    frame.pack(side=BOTTOM)


def obj_to_x_o():
    global cells
    cells_values = []
    for cell in cells:
        cell_value = cell.cget('text')
        cells_values.append(cell_value)
    return cells_values


def people_is_win(cells_values, who):
    # global people_x_o
    # cells_values = []
    # for cell in cells:
    #     cell_value = cell.cget('text')
    # cells_values=obj_to_x_o()
    print(cells_values)

    if (cells_values[0] == who and cells_values[1] == who and cells_values[2] == who) or \
            (cells_values[3] == who and cells_values[4] == who and cells_values[5] == who) or \
            (cells_values[6] == who and cells_values[7] == who and cells_values[8] == who) or \
            (cells_values[0] == who and cells_values[3] == who and cells_values[6] == who) or \
            (cells_values[1] == who and cells_values[4] == who and cells_values[7] == who) or \
            (cells_values[2] == who and cells_values[5] == who and cells_values[8] == who) or \
            (cells_values[0] == who and cells_values[4] == who and cells_values[8] == who) or \
            (cells_values[2] == who and cells_values[4] == who and cells_values[6] == who):
        # if who == people_x_o.get():
        #     alert('恭喜恭喜,你获得了胜利!')
        #     return True
        # else:
        #     alert('再接再厉,人机获得了胜利!')
        #     return False
        return who
    if '' not in cells_values:
        alert('起鼓相当的对手!')
    return None


def can_down(index):
    global cells
    if cells[index].cget('text') == '':
        print('({})能落子'.format(index))
        return True
    else:
        print('({})不能落子'.format(index))
        return False


def alert(msg):
    messagebox.showinfo('游戏结果', msg)


def machine():
    # debug

    global cells

    # cells[random.randint(0,8)].config(text='O')
    # return
    if people_x_o.get() == 'X':
        machine_x_o = 'O'
    else:
        machine_x_o = 'X'
    for i in range(9):
        cells_values = obj_to_x_o()
        if can_down(i):
            # 如果这下机器的棋子
            cells_values[i] = machine_x_o
            ret = people_is_win(cells_values, machine_x_o)
            print('下这({}),结果({})'.format(i, ret))
            if ret == machine_x_o:  # 机器赢
                print('下这({}),机器要赢'.format(i))
                cells[i].config(text=machine_x_o)
                alert('再接再厉,人机获得了胜利!')
                return
            # 如果这下人的棋子
            cells_values[i] = people_x_o.get()
            ret = people_is_win(cells_values, people_x_o.get())
            if ret == people_x_o.get():  # 人赢
                print('不下这({}),人要赢'.format(i))
                cells[i].config(text=machine_x_o)
                return
    # 判断角是否能下
    jiao_list = [0, 2, 6, 8]
    for jiao in jiao_list:
        if can_down(jiao):
            print('在角({})下子'.format(jiao))
            cells[jiao].config(text=machine_x_o)
            return

    # 判断中心是否能下
    if can_down(4):
        print('在中心({})下子'.format(4))
        cells[4].config(text=machine_x_o)
        return

    # 判断边是否能下
    bian_list = [1, 3, 5, 7]
    for bian in bian_list:
        if can_down(bian):
            print('在边({})下子'.format(bian))
            cells[bian].config(text=machine_x_o)
            return


if __name__ == '__main__':
    win = tkinter.Tk()
    people_x_o = StringVar()
    init_win()
    cells = init_chessboard()
    init_x_o()
    init_start()

    win.mainloop()
