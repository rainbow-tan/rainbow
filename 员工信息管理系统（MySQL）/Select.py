# -*- encoding=utf-8 -*-

import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import Add
import Login
from MyDatabase import db
from MyDatabase import delete_database_by_keyname
from MyDatabase import select_database
import Update


def select_html():
    def show_data():
        info = []
        db_data = select_database(db, 'employee', ['number', 'name', 'sex', 'hiredate', 'position', 'pay'])
        for data in db_data:
            one = [data['number'], data['name'], data['sex'], data['hiredate'], data['position'], data['pay']]
            info.append(one)
        for index, data in enumerate(info):
            table.insert('', END, values=data)

    def chaxuan():
        children = table.get_children()  # 获取所有的数据
        for child in children:
            table.delete(child)
        number = bianhao_entry.get().strip()
        name = name_entry.get().strip()
        if number == '' and name == '':
            show_data()
            return
        select_option = dict()
        if number:
            select_option['number'] = number
        if name:
            select_option['name'] = name
        db_data = select_database(db, 'employee', ['number', 'name', 'sex', 'hiredate', 'position', 'pay'],
                                  select_option)
        if db_data:

            info = []
            for data in db_data:
                one = [data['number'], data['name'], data['sex'], data['hiredate'], data['position'], data['pay']]
                info.append(one)
            for index, data in enumerate(info):
                table.insert('', END, values=data)
        else:
            messagebox.showinfo('提示信息', '未查询到符合的数据')

    def login_html():
        win.destroy()
        Login.login_html()

    def add_html():
        win.destroy()
        Add.add_html()

    def update_html():
        selection = table.selection()  # 获取选中的数据
        length = len(selection)
        print('选中的条数:{}'.format(length))  # 选中的条数
        print('选中的对象:{}'.format(selection))  # 选中的数据对象
        if length == 1:
            number = table.item(selection[0], 'values')[0]
            win.destroy()
            Update.update_html(number)
        else:
            messagebox.showinfo('提示信息', '请选择一条记录进行修改')

    def delete_choose():
        selection = table.selection()  # 获取选中的数据
        length = len(selection)
        print('选中的条数:{}'.format(length))  # 选中的条数
        print('选中的对象:{}'.format(selection))  # 选中的数据对象
        if length:
            flag = messagebox.askyesno('提示信息', '是否删除所选数据?')
            if flag:
                numbers = list()
                for item in selection:
                    number = table.item(item, 'values')[0]
                    numbers.append(number)
                    table.delete(item)
                delete_database_by_keyname(db, 'employee', 'number', numbers)

        else:
            messagebox.showinfo('提示信息', '请选择一条或多条记录进行删除')

    def shuaxin():
        children = table.get_children()  # 获取所有的数据
        for child in children:
            table.delete(child)
        show_data()

    pass
    win = tkinter.Tk()  # 窗口
    win.title('南风丶轻语')  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 1000
    height = 520
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置
    win.resizable(0, 0)
    frame = Frame(win)
    frame2 = Frame(win)
    frame3 = Frame(win)
    frame4 = Frame(win)
    Label(frame2, text='编号', font=('宋体', 20)).pack(side=LEFT, padx=10)
    bianhao_entry = Entry(frame2, font=('宋体', 20), width=10)
    bianhao_entry.pack(side=LEFT, padx=20)
    Label(frame2, text='姓名', font=('宋体', 20)).pack(side=LEFT, padx=20)
    name_entry = Entry(frame2, font=('宋体', 20), width=10)
    name_entry.pack(side=LEFT, padx=20)
    Button(frame2, text='查询', command=chaxuan, relief='g', font=('宋体', 12)).pack(side=LEFT, fill=Y, expand=True,
                                                                                 padx=20)
    frame4.pack(pady=20)
    Label(frame4, text='员工信息阅览', font=('粗体', 26), fg='green').pack()
    frame2.pack(pady=20)
    frame.pack(pady=20)
    frame3.pack(pady=20)
    scrollbar_y = Scrollbar(frame, orient=VERTICAL)
    scrollbar_x = Scrollbar(frame, orient=HORIZONTAL)
    columns = ['编号', '姓名', '性别', '入职日期', '职位', '薪资']
    table = ttk.Treeview(
        master=frame,  # 父容器
        height=10,  # 高度,可显示height行
        columns=columns,  # 显示的列
        show='headings',
        yscrollcommand=scrollbar_y.set,  # 滚动条
        xscrollcommand=scrollbar_x.set,  # 滚动条
        )
    table.heading('编号', text='编号')
    table.heading('姓名', text='姓名')
    table.heading('性别', text='性别')
    table.heading('入职日期', text='入职日期')
    table.heading('职位', text='职位')
    table.heading('薪资', text='薪资')

    table.column('编号', width=100, anchor=CENTER)
    table.column('姓名', width=100, anchor=CENTER)
    table.column('性别', width=100, anchor=CENTER)
    table.column('入职日期', width=100, anchor=CENTER)
    table.column('职位', width=200, anchor=CENTER)
    table.column('薪资', width=100, anchor=CENTER)

    scrollbar_y.config(command=table.yview)
    scrollbar_x.config(command=table.xview)
    scrollbar_y.pack(side=RIGHT, fill=Y)
    scrollbar_x.pack(side=BOTTOM, fill=X)
    table.pack(fill=BOTH, expand=True)
    show_data()

    Button(frame3, text='刷新', command=shuaxin, relief='g', font=('宋体', 12)).pack(side=LEFT, padx=40)
    Button(frame3, text='添加', command=add_html, relief='g', font=('宋体', 12)).pack(side=LEFT, padx=40)
    Button(frame3, text='修改', command=update_html, relief='g', font=('宋体', 12)).pack(side=LEFT, padx=40)
    Button(frame3, text='删除', command=delete_choose, relief='g', font=('宋体', 12)).pack(side=LEFT, padx=40)
    Button(frame3, text='注销', command=login_html, relief='g', font=('宋体', 12)).pack(side=LEFT, padx=40)

    win.mainloop()


if __name__ == '__main__':
    select_html()
