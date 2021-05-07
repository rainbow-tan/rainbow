import json
from tkinter import *

import common


def event1():
    print('加载event')
    global todo_list
    global todo_list_StringVar
    global checkbuttons
    var = entry.get().strip()
    todo_list.append({'title': var, 'state': '0'}, )
    pass
    show()


def event2():
    print('完成event')
    global todo_list
    global todo_list_StringVar
    global checkbuttons
    todo_list_value = list(map(lambda x: x.get(), todo_list_StringVar))
    print('todo_list_value:{}'.format(todo_list_value))
    for i, value in enumerate(todo_list_value):
        if value == '1':
            print('index:{}'.format(i))
            checkbuttons[i].config(bg='#00ff80')
            win.update()
            todo_list[i]['state'] = '1'
    print('todo_list:{}'.format(todo_list))

    pass


def event3():
    print('删除event')
    global todo_list_StringVar
    global checkbuttons
    global todo_list
    todo_list_value = list(map(lambda x: x.get(), todo_list_StringVar))
    print('todo_list_value:{}'.format(todo_list_value))
    delete_indexs = []
    for i, value in enumerate(todo_list_value):
        if value == '1':
            delete_indexs.append(i)
    delete_indexs.sort()
    delete_indexs.reverse()
    print('要删除的下标:{}'.format(delete_indexs))

    # global todo_list_StringVar
    # global checkbuttons
    for j in delete_indexs:
        todo_list.pop(j)

    common.clear_child(f1)

    checkbuttons = []
    todo_list_StringVar = []
    show()

    pass


def event4():
    print('保存event')
    with open('todo_list.json', 'w', encoding='utf-8') as f:
        data = json.dumps(todo_list, indent=4, ensure_ascii=False)
        f.write(data)
    pass


def event5():
    print('加载event')
    global todo_list
    global todo_list_StringVar
    global checkbuttons
    with open('todo_list.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        todo_list = data
    common.clear_child(f1)
    todo_list_StringVar = []
    checkbuttons = []
    show()


def show():
    global todo_list
    global todo_list_StringVar
    global checkbuttons
    todo_list_StringVar = []
    checkbuttons = []
    row = 0
    column = 0
    for index, item in enumerate(todo_list):
        string_val = StringVar(f1, '0')
        todo_list_StringVar.append(string_val)
        title = item['title']
        state = item['state']
        checkbutton = Checkbutton(
                master=f1,  # 父容器
                text=title,  # 文本
                relief='g',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
                onvalue='1',  # 选中传递的值，默认是1
                offvalue='0',  # 取消选中后传递的值，默认是0
                variable=string_val,  # 通过onvalue和offvalue传递
                wraplength=70,
                width=12,
                height=5,
                justify='left',
                )
        if state == '1':
            checkbutton.configure(bg='#00ff80')
        checkbutton.grid(row=row, column=column)
        checkbuttons.append(checkbutton)
        column += 1
        if column % 4 == 0:
            row += 1
            column = 0


if __name__ == '__main__':
    win = Tk()
    common.set_size_center(win, 500, 500)
    f = Frame()
    entry = Entry(
            master=f,  # 父容器
            text='标签',  # 文本
            relief='g',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。
            bd=3,  # 边框的大小
            width=15,  # 宽度
            state='normal',  # 设置状态 normal、readonly、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('宋体', 16),  # 字体
            )
    entry.pack(side=LEFT)
    todo_list = [
        {'text': '添加', 'command': event1},
        {'text': '完成', 'command': event2},
        {'text': '删除', 'command': event3},
        {'text': '保存', 'command': event4},
        {'text': '加载', 'command': event5},
        ]
    for item in todo_list:
        button = Button(
                master=f,  # 父容器
                text=item['text'],  # 文本
                relief='g',  # 边框的3D样式 flat、sunken、raised、groove、ridge、solid。默认为 raised。
                font=('宋体', 12),  # 字体
                command=item['command'],  # 点击事件
                ).pack(side=LEFT, padx=(10, 0))
    f.pack(pady=(10, 0))

    f1 = Frame(width=480, height=460, relief='g', bd='2')
    f1.pack(pady=(10, 0))

    # todo_list = [
    #     {'title': '明天吃鱼1', 'state': '0'},
    #     {'title': '明天吃鱼2', 'state': '0'},
    #     {'title': '明天吃鱼3', 'state': '0'},
    #     {'title': '明天吃鱼4', 'state': '0'},
    #     {'title': '明天吃鱼5', 'state': '0'},
    #     {'title': '明天吃鱼6', 'state': '0'},
    #     {'title': '明天吃鱼7', 'state': '0'},
    #     {'title': '明天吃鱼8', 'state': '0'},
    #     {'title': '明天吃鱼9', 'state': '0'},
    #     {'title': '明天吃鱼1008611', 'state': '0'},
    #     ]
    todo_list = []
    todo_list_StringVar = []
    checkbuttons = []
    show()

    win.mainloop()
