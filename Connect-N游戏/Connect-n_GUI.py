import json
from tkinter import *
from tkinter import messagebox

WHITE_DISK = "\u26AA"
BLACK_DISK = "\u26AB"
FW_SPACE = "\u3000"
FW_LINE = "\u2015"
WHO_IS_PLAN = 1  # 2是黑色方,1是白色方
BLUE = 'blue'  # 1是白色方
GREEN = 'green'  # 2是黑色方
WIN = False  # 是否赢了
FILL = False  # 棋盘是否满了
FILENAME = "Connect-n.txt"  # 保存的文件
LABELS = []

game = {
    "N": 4,
    "board": [],
    "moves": []
    }


def create_board(n):
    """create the board for the Connect-N game"""
    game["N"] = n
    board = []
    for i in range(n + 3):  # 创建棋盘,默认都是0
        columns = []
        for j in range(n + 2):
            columns.append(0)
        board.append(columns)
    game["board"] = board


def display_board():
    """print the board content"""
    w = f"{WHITE_DISK:^3}"
    b = f"{BLACK_DISK:^3}"
    e = f"{FW_SPACE:^3}"
    n = game["N"]
    board = game["board"]
    for i in range(n + 3):  # 显示棋盘
        s = ""
        for j in range(n + 2):
            cell = board[i][j]
            if cell == 0:
                s = s + f"| {e}"
            elif cell == 1:
                s = s + f"| {w}"
            elif cell == 2:
                s = s + f"| {b}"
            else:
                pass
        print(s)


def drop_disk(c):
    """drop disk at column c"""
    global WHO_IS_PLAN
    n = game["N"]
    board = game["board"]
    for i in range(n + 2, -1, -1):
        cell = board[i][c - 1]
        if cell == 0:
            board[i][c - 1] = WHO_IS_PLAN  # 记录下棋的位置
            print("Planer({})drop disk at column({})".format(WHO_IS_PLAN, c))
            if WHO_IS_PLAN == 2:
                WHO_IS_PLAN = 1
                game["moves"].append("W{}".format(c))  # 保存黑色玩家下棋的位置
            else:
                game["moves"].append("B{}".format(c))  # 保存白色玩家下棋的位置
                WHO_IS_PLAN = 2
            return True
    else:
        messagebox.showwarning('提示信息', '该列已经满载,请重新选择')
        return False


def win(data_list, value, count):
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            row = []
            column = []
            xie_zy = []
            xie_yz = []
            for k in range(count):
                try:
                    row.append(data_list[i][j + k])  # 行判断
                except:
                    row.append("")
                try:
                    column.append(data_list[i + k][j])  # 列判断
                except:
                    column.append("")
                try:
                    xie_zy.append(data_list[i + k][j + k])  # 斜从左到右判断
                except:
                    xie_zy.append("")
                try:
                    xie_yz.append(data_list[i + k][j - k])  # 斜从右到左判断
                except:
                    xie_yz.append("")
            new_row = list(set(row))
            new_column = list(set(column))
            new_xie_zy = list(set(xie_zy))
            new_xie_yz = list(set(xie_yz))
            if len(new_row) == 1 and new_row[0] == value:  # 行满足
                return True
            if len(new_column) == 1 and new_column[0] == value:  # 列满足
                return True
            if len(new_xie_zy) == 1 and new_xie_zy[0] == value:  # 斜从左到右满足
                return True
            if len(new_xie_yz) == 1 and new_xie_yz[0] == value:  # 斜从右到左满足
                return True
    return False


def check_winning():
    """check if there is a winner"""
    global WIN
    n = game["N"]
    board = game["board"]
    if win(board, 2, n):
        messagebox.showinfo('提示信息', "黑色方获胜")
        WIN = True
    if win(board, 1, n):
        messagebox.showinfo('提示信息', "白色方获胜")
        WIN = True
    check_fill()


def save_board_event():
    save_board(FILENAME)


def save_board(fname):
    """save the game"""
    n = game["N"]
    board = game["board"]
    moves = game["moves"]
    with open(fname, "w", encoding="utf-8") as  f:
        f.write(str(n))  # 保存N
        f.write("\n")
        f.write(str(board))  # 保存棋盘
        f.write("\n")
        f.write(str(moves))  # 保存移动
        f.write("\n")
        f.write(black_entry.get())  # 保存黑色方名字
        f.write("\n")
        f.write(white_entry.get())  # 保存白色方名字
        f.write("\n")
        f.write(current_entry.get())  # 保存下棋人
    messagebox.showinfo('提示信息', "存档完成!")


def load_board_event():
    load_board(FILENAME)  # 加载存档的事件


def load_board(fname):
    """load the game"""
    try:
        with open(fname, "r", encoding="utf-8") as f:
            data = f.readlines()
        n = int(data[0].strip())
        board = json.loads(data[1].strip())
        moves = eval(data[2].strip())
        game["N"] = n  # 加载N
        game["board"] = board  # 加载棋盘
        game["moves"] = moves  # 加载移动
        messagebox.showinfo('提示信息', "读档成功!")
        global WIN
        global FILL
        WIN = False
        FILL = False
        n_entry.delete(0, END)
        n_entry.insert(END, game['N'])
        black_entry.delete(0, END)
        black_entry.insert(END, data[3].strip())
        white_entry.delete(0, END)
        white_entry.insert(END, data[4].strip())
        current_entry.delete(0, END)
        current_entry.insert(END, data[5].strip())  # 加载下棋人
        show_display_board()
        return True
    except Exception as e:
        messagebox.showwarning('提示信息', "读档失败!")
        return False


def check_fill():  # 判断棋盘是否满了
    fill = True
    board = game["board"]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                fill = False
                break
    if fill:
        messagebox.showinfo('棋盘已满,平局！！！')
        global FILL
        FILL = True
        # show_moves()


def show_moves():
    """show all previous moves"""
    print("show all moves")
    messagebox.showinfo('移动步骤', '{}'.format(game["moves"]))


def left_mouse_click(event):
    if WIN or FILL:
        return
    if WHO_IS_PLAN == 1:
        name = white_entry.get()  # 取界面的白色方名字
    else:
        name = black_entry.get()  # 取界面的黑色方名字
    current_entry.delete(0, END)
    current_entry.insert(END, name)
    for i in range(len(LABELS)):
        for j in range(len(LABELS[i])):
            if LABELS[i][j] == event.widget:  # 判断是点击了那个方块
                drop_disk(j + 1)  # 下的列
                show_display_board()
                check_winning()
                check_fill()
                return


def show_display_board():
    for i in frame_bottom.winfo_children():
        i.destroy()
    global LABELS
    board = game['board']
    for i in range(len(board)):
        frame1 = Frame(frame_bottom)
        frame1.pack(fill=BOTH, expand=True)
        labels = []
        for j in range(len(board[i])):
            label = Label(frame1, relief='g')
            labels.append(label)
            label.pack(side=LEFT, fill=BOTH, expand=True)
            label.bind('<Button-1>', left_mouse_click)
            if board[i][j] == 1:  # 设置白色方显示
                label.config(text=WHITE_DISK)
            elif board[i][j] == 2:  # 设置黑色方显示
                label.config(text=BLACK_DISK)
            else:
                pass
        LABELS.append(labels)


def begin():
    global WIN
    global FILL
    WIN = False  # 默认没赢，棋盘也没满
    FILL = False  # 默认没赢，棋盘也没满
    n = int(n_entry.get())  # 获取界面的n
    create_board(n)  # 创建棋盘
    show_display_board()  # 显示棋盘


create_board(3)
window = Tk()  # 窗口
frame = Frame(window, padx=50)
Label(frame, text='黑色方昵称', relief='g').grid(row=0, column=0, sticky=E + W + N + S)
Label(frame, text='白色方昵称', relief='g').grid(row=1, column=0, sticky=E + W + N + S)
Label(frame, text='当前执棋者', relief='g').grid(row=2, column=0, sticky=E + W + N + S)
Label(frame, text='输入N的值', relief='g').grid(row=3, column=0, sticky=E + W + N + S)
black_entry = Entry(frame)  # 黑色昵称输入框
black_entry.insert(END, '我是黑色玩家哟')
black_entry.grid(row=0, column=1)  # 按照行列放置组件
white_entry = Entry(frame)  # 白色昵称输入框
white_entry.insert(END, '我是白色玩家哟')
white_entry.grid(row=1, column=1)  # 按照行列放置组件
current_entry = Entry(frame, fg='red')  # 当前玩家显示框
n_entry = Entry(frame)  # N的输入框
current_entry.grid(row=2, column=1)  # 按照行列放置组件
n_entry.grid(row=3, column=1)  # 按照行列放置组件
n_entry.insert(END, 3)  # 默认N为3
Button(frame, text='存档', relief='g', command=save_board_event).grid(row=0, column=2,
                                                                    sticky=E + W + N + S)
Button(frame, text='读档', relief='g', command=load_board_event).grid(row=1, column=2,
                                                                    sticky=E + W + N + S)
Button(frame, text='显示移动', relief='g', command=show_moves).grid(row=2, column=2,
                                                                sticky=E + W + N + S)
Button(frame, text='开始', relief='g', command=begin).grid(row=3, column=2, sticky=E + W + N + S)
frame.pack(pady=(10, 0))  # pack布局
frame_bottom = Frame(window)  # Frame框架
frame_bottom.pack(fill=BOTH, expand=True, padx=10, pady=10)  # pack布局
show_display_board()  # 显示棋盘

window.title('南风丶轻语')  # 标题
screenwidth = window.winfo_screenwidth()  # 屏幕宽度
screenheight = window.winfo_screenheight()  # 屏幕高度
width = 500  # 窗口宽度
height = 500  # 窗口高度
x = int((screenwidth - width) / 2)  # 居中设置x,y轴坐标
y = int((screenheight - height) / 2)  # 居中设置x,y轴坐标
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置
window.mainloop()
