import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import shujuku


def insert_data(field_data):
    for data in field_data:  # 插入数据
        tree.insert('', END, value=data)


def clear_item():
    win.destroy()
    os.system('python MainWin.py')
    pass


def add():
    win.destroy()
    os.system('python add_yuangong.py')
    pass


def update():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showwarning('提示', '选择一条记录进行修改')
    else:
        choose_data = tree.item(selects[0], 'values')
        print(choose_data)
        win.destroy()
        os.system('python update_yuangong.py {}'.format(choose_data[0]))


def delete():
    selects = tree.selection()
    if len(selects) > 0:
        all_data = []
        for select in selects:
            all_data.append(tree.item(select, 'values'))  # 获取item的值
        remove_ids = []
        for data in all_data:
            remove_ids.append(data[0])
        # print('要删掉的id：{}'.format(remove_ids))
        choose = messagebox.askyesno('提示', '确认删除已选择记录吗？')

    else:
        messagebox.showwarning('提示', '至少选择一条记录进行删除')


if __name__ == '__main__':
    win = tkinter.Tk()  # 窗口
    win.title('服装管理系统')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = screenwidth
    height = screenheight
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

    field_names = ['员工编号', '员工姓名', '员工性别', '员工职位', '员工薪资', '联系方式', ]
    data = shujuku.select_all(shujuku.db, 'yuangong')

    field_data_value = [['员工编号', '员工姓名', '员工性别', '员工职位', '员工薪资', '联系方式', ],
                        ['员工编号', '员工姓名', '员工性别', '员工职位', '员工薪资', '联系方式', ]]
    field_data_value = data
    frame = tkinter.Frame(win)
    select_label = Label(win, text='员工信息', font=('', 20))
    tree = ttk.Treeview(frame, height=20, columns=field_names, show='headings')
    for field_name in field_names:
        tree.column(field_name, width=220, )  # 对列进行定义
        tree.heading(field_name, text=field_name)
    insert_data(field_data_value)
    s = Scrollbar(frame)  # 滚动条
    s.config(command=tree.yview)
    sx = Scrollbar(frame)  # 滚动条
    sx.config(command=tree.xview)
    tree.config(yscrollcommand=s.set)
    tree.config(xscrollcommand=sx.set)
    frame2 = tkinter.Frame(win)
    add_btn = tkinter.Button(frame2, font=('', 20), relief='g', text='添加', command=add)
    update_btn = tkinter.Button(frame2, font=('', 20), relief='g', text='修改', command=update)
    clear_item_btn = tkinter.Button(frame2, font=('', 20), relief='g', text='首页',
                                    command=clear_item)
    delete_btn = tkinter.Button(frame2, font=('', 20), relief='g', text='删除', command=delete)

    s.pack(side=RIGHT, fill=Y)
    tree.pack()
    select_label.pack(side=tkinter.TOP, padx=10, pady=40)
    frame.pack()
    add_btn.grid(row=0, column=0, padx=30, pady=20)
    update_btn.grid(row=0, column=1, padx=30, pady=20)
    delete_btn.grid(row=0, column=2, padx=30, pady=20)
    clear_item_btn.grid(row=0, column=3, padx=40, pady=20)
    frame2.pack()

    win.mainloop()
