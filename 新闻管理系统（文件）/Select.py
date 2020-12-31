# -*- encoding=utf-8 -*-

import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import Add
import Login
import Update
from common import NEWS_TXT
from common import TITLE


def select_html():
    def show_data():
        info = []
        with open(NEWS_TXT, 'r', encoding='utf-8') as f:
            news = f.readlines()
        print('news:{}'.format(news))
        for new in news:
            new = new.strip()
            new = new.split('-')
            info.append(new)
        for index, data in enumerate(info):
            table.insert('', END, values=data)

    def chaxuan():
        pass

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
                with open(NEWS_TXT, 'r', encoding='utf-8') as f:
                    news = f.readlines()
                print('news:{}'.format(news))
                update_new = []
                for new in news:
                    new_strip = new.strip()
                    new_strip = new_strip.split('-')
                    if new_strip[0] in numbers:
                        pass
                    else:
                        update_new.append(new)
                with open(NEWS_TXT, 'w', encoding='utf-8') as f:
                    f.write(''.join(update_new))

        else:
            messagebox.showinfo('提示信息', '请选择一条或多条记录进行删除')

    def fabu():
        selection = table.selection()  # 获取选中的数据
        length = len(selection)
        print('选中的条数:{}'.format(length))  # 选中的条数
        print('选中的对象:{}'.format(selection))  # 选中的数据对象
        if length:
            flag = messagebox.askyesno('提示信息', '是否发布所选新闻')
            if flag:
                numbers = list()
                for item in selection:
                    number = table.item(item, 'values')[0]
                    numbers.append(number)
                    table.delete(item)
                with open(NEWS_TXT, 'r', encoding='utf-8') as f:
                    news = f.readlines()
                print('news:{}'.format(news))
                update_new = []
                for new in news:
                    new_strip = new.strip()
                    new_strip = new_strip.split('-')
                    if new_strip[0] in numbers:
                        new_info = new_strip[0] + '-' + new_strip[1] + '-' + new_strip[
                            2] + '-' + '发布' + '\n'
                        update_new.append(new_info)
                    else:
                        update_new.append(new)
                with open(NEWS_TXT, 'w', encoding='utf-8') as f:
                    f.write(''.join(update_new))

        else:
            messagebox.showinfo('提示信息', '请选择一条或多条记录')

        children = table.get_children()  # 获取所有的数据
        for child in children:
            table.delete(child)
        show_data()

    def chexiaofabu():
        selection = table.selection()  # 获取选中的数据
        length = len(selection)
        print('选中的条数:{}'.format(length))  # 选中的条数
        print('选中的对象:{}'.format(selection))  # 选中的数据对象
        if length:
            flag = messagebox.askyesno('提示信息', '是否撤销发布所选新闻')
            if flag:
                numbers = list()
                for item in selection:
                    number = table.item(item, 'values')[0]
                    numbers.append(number)
                    table.delete(item)
                with open(NEWS_TXT, 'r', encoding='utf-8') as f:
                    news = f.readlines()
                print('news:{}'.format(news))
                update_new = []
                for new in news:
                    new_strip = new.strip()
                    new_strip = new_strip.split('-')
                    if new_strip[0] in numbers:
                        new_info = new_strip[0] + '-' + new_strip[1] + '-' + new_strip[
                            2] + '-' + '未发布' + '\n'
                        update_new.append(new_info)
                    else:
                        update_new.append(new)
                with open(NEWS_TXT, 'w', encoding='utf-8') as f:
                    f.write(''.join(update_new))

        else:
            messagebox.showinfo('提示信息', '请选择一条或多条记录')

        children = table.get_children()  # 获取所有的数据
        for child in children:
            table.delete(child)
        show_data()

    pass
    win = tkinter.Tk()  # 窗口
    win.title(TITLE)  # 标题
    screenwidth = win.winfo_screenwidth()  # 屏幕宽度
    screenheight = win.winfo_screenheight()  # 屏幕高度
    width = 800
    height = 500
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
    Label(frame2, text='姓名', font=('宋体', 20)).pack(side=LEFT, padx=10)
    name_entry = Entry(frame2, font=('宋体', 20), width=10)
    name_entry.pack(side=LEFT, padx=20)
    Button(frame2, text='查询', command=chaxuan, relief='g', font=('宋体', 12)).pack(side=LEFT, fill=Y,
                                                                                 expand=True,
                                                                                 padx=20)
    frame4.pack(pady=30)
    Label(frame4, text='查看所有新闻信息', font=('粗体', 26), ).pack()
    # frame2.pack(pady=20)
    frame.pack(pady=20)
    frame3.pack(pady=20)
    scrollbar_y = Scrollbar(frame, orient=VERTICAL)
    scrollbar_x = Scrollbar(frame, orient=HORIZONTAL)
    columns = ['编号', '标题', '内容', '状态', ]
    table = ttk.Treeview(
            master=frame,  # 父容器
            height=10,  # 高度,可显示height行
            columns=columns,  # 显示的列
            show='headings',
            yscrollcommand=scrollbar_y.set,  # 滚动条
            xscrollcommand=scrollbar_x.set,  # 滚动条
            )
    table.heading('编号', text='编号')
    table.heading('标题', text='标题')
    table.heading('内容', text='内容')
    table.heading('状态', text='状态')

    table.column('编号', width=100, anchor=CENTER)
    table.column('标题', width=100, anchor=CENTER)
    table.column('内容', width=200, anchor='w')
    table.column('状态', width=100, anchor=CENTER)

    scrollbar_y.config(command=table.yview)
    scrollbar_x.config(command=table.xview)
    scrollbar_y.pack(side=RIGHT, fill=Y)
    scrollbar_x.pack(side=BOTTOM, fill=X)
    table.pack(fill=BOTH, expand=True)
    show_data()

    Button(frame3, text='添加', command=add_html, relief='g', font=('宋体', 12)).pack(side=LEFT,
                                                                                  padx=20)
    Button(frame3, text='修改', command=update_html, relief='g', font=('宋体', 12)).pack(side=LEFT,
                                                                                     padx=20)
    Button(frame3, text='删除', command=delete_choose, relief='g', font=('宋体', 12)).pack(side=LEFT,
                                                                                       padx=20)
    Button(frame3, text='发布', command=fabu, relief='g', font=('宋体', 12)).pack(side=LEFT, padx=20)
    Button(frame3, text='撤销发布', command=chexiaofabu, relief='g', font=('宋体', 12)).pack(side=LEFT,
                                                                                       padx=20)
    Button(frame3, text='注销', command=login_html, relief='g', font=('宋体', 12)).pack(side=LEFT,
                                                                                    padx=20)

    win.mainloop()


if __name__ == '__main__':
    select_html()
