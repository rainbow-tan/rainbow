import json

WHITE_DISK = "\u26AA"
BLACK_DISK = "\u26AB"
FW_SPACE = "\u3000"
FW_LINE = "\u2015"
WHO_IS_PLAN = 1  # 2是黑色方,1是白色方
WIN = False
FILL = False
FILENAME = "Connect-n.txt"

game = {
    "N": 4,
    "board": [],
    "moves": []
    }


def create_board(n):
    """create the board for the Connect-N game"""
    game["N"] = n
    board = []
    for i in range(n + 3):
        columns = []
        for j in range(n + 2):
            columns.append(0)
        board.append(columns)  # 保存数据结构
    game["board"] = board
    game['moves'] = []


def display_board():
    """print the board content"""
    w = f"{WHITE_DISK:^3}"
    b = f"{BLACK_DISK:^3}"
    e = f"{FW_SPACE:^3}"
    n = game["N"]
    board = game["board"]
    for i in range(n + 3):  # 显示黑白棋
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
    if c > n + 2 or c <= 0:  # 输入的列数范围不符合
        print("列数范围[1,{}],你选择的是({}),请重新选择".format(n + 2, c))
        return False
    for i in range(n + 2, -1, -1):
        cell = board[i][c - 1]
        if cell == 0:
            board[i][c - 1] = WHO_IS_PLAN  # 谁的棋填谁的值1或2
            print("Planer({})drop disk at column({})".format(WHO_IS_PLAN, c))
            if WHO_IS_PLAN == 2:
                game["moves"].append("B{}".format(c))  # 记录下棋步骤
                WHO_IS_PLAN = 1
            else:
                game["moves"].append("W{}".format(c))  # 记录下棋步骤
                WHO_IS_PLAN = 2
            return True
    else:
        print("该列({})已经满载,请重新选择".format(c))  # 列已经满载
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
                    xie_zy.append(data_list[i + k][j + k])  # 斜左右判断
                except:
                    xie_zy.append("")
                try:
                    xie_yz.append(data_list[i + k][j - k])  # 斜右左判断
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
            if len(new_xie_zy) == 1 and new_xie_zy[0] == value:  # 斜左右满足
                return True
            if len(new_xie_yz) == 1 and new_xie_yz[0] == value:  # 斜右左满足
                return True
    return False  # 未嬴


def check_winning():
    """check if there is a winner"""
    global WIN
    n = game["N"]
    board = game["board"]
    if win(board, 2, n):
        print("黑色方获胜")
        WIN = True
        show_moves()
    if win(board, 1, n):
        print("白色方获胜")
        WIN = True
        show_moves()
    check_fill()


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
        f.write(str(WHO_IS_PLAN))  # 保存下棋人
    print("存档完成!")
    exit()


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
        global WHO_IS_PLAN
        WHO_IS_PLAN = int(data[3].strip())  # 加载下棋人
        return True
    except Exception as e:
        print("读档失败,开始新游戏")
        return False


def check_fill():
    fill = True
    board = game["board"]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                fill = False
                break
    if fill:  # 棋盘下满了
        print('棋盘已满,平局！！！')
        global FILL
        FILL = True
        show_moves()


def show_moves():
    """show all previous moves"""
    print("show all moves")
    print(game["moves"])


def check_input(char):
    if char in ["s", "S"]:
        is_letter = True
    else:
        try:
            int(char)
            is_letter = False
        except:
            print("输入错误,", end="")
            is_letter = None
    return is_letter


def begin():
    print("请输入字母L加载存档,N开始新游戏,均不区分大小写")
    flag = False
    char = ''
    while not flag:
        char = input("请输入你的选择:")
        if char in ["L", "N", "l", "n"]:
            flag = True
        else:
            print("输入错误,", end="")
    if char.lower() == "n":  # 开始新游戏
        new_game()
        play(game["N"])
    elif char.lower() == "l":  # 加载存档
        if load_board(FILENAME):
            play(game["N"])
        else:
            new_game()
            play(game["N"])
    else:
        pass


def play(n):
    display_board()
    while not WIN and not FILL:
        if WHO_IS_PLAN == 2:
            msg = "黑色方"
        else:
            msg = "白色方"
        c = input(("{}--请选择下的位置[{},{}] 或输入S(不区分大小写)存档:".format(msg, 1, n + 2)))
        is_letter = check_input(c)
        if is_letter is True:
            save_board(FILENAME)
        elif is_letter is False:
            c = int(c)
            drop_disk(c)
            display_board()
            check_winning()
        else:
            pass


def new_game():
    n = int(input("请输入N的值:"))
    create_board(n)
    display_board()


begin()
