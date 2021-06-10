# -*- encoding=utf-8 -*-
import socket
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import common
import login
import mysqltool
from mysqltool import insert
from mysqltool import select

NAME = 'name'
TYPE = 'type'
DATA = 'data'
ENTRY = 'entry'
COMBOBOX = 'combobox'
OPTIONS = 'options'
MUST = 'must'


class MyFrame:
    @staticmethod
    def custom_content():
        # 显示的字段
        content = [
            {NAME: '账  号', TYPE: ENTRY, MUST: True, DATA: {}, },
            {NAME: '密  码', TYPE: ENTRY, MUST: True, },
            {NAME: '手机号', TYPE: ENTRY, MUST: False, DATA: {}},
            ]
        return content

    @staticmethod
    def save(data):
        # 保存和修改信息
        db_data, msg = select(mysqltool.conn_db, 'useraccount', ['account'], {'account': data[0]})
        if db_data:
            success = False
            msg = '该账号已经存在'
        else:

            ip = socket.gethostbyname(socket.gethostname())  # 获取IP
            insert_data = {'account': data[0], 'password': data[1], 'phone': data[2], 'ip': ip}
            success, msg = insert(mysqltool.conn_db, 'useraccount', insert_data)
        return success, msg

    def __init__(self, win,
                 win_width=460,  # 窗口宽度
                 win_height=340,  # 窗口高度
                 win_title='用户注册',  # 窗口标题
                 head='用户注册',  # 显示头信息
                 font_family='宋体',  # 字体
                 font_size=20,  # 字体大小
                 entry_width=12,  # 输入框宽度
                 entry_height=5,  # 下拉显示的条目数量
                 entry_space_x=20,  # label和entry在x轴的间距
                 entry_space_y=10,  # 上一行和下一行y轴的间距
                 combobox_indent=1,  # 输入框和下拉框长度之差
                 btn_space=10,  # 按钮在x轴间距
                 btn_width=10,  # 按钮的宽度
                 split_column=1,  # 1表示显示在一列,其他大于1的数字表示每列显示几个元素,即几行
                 update_data=[]  # 修改传入的数据
                 ):
        self.win = win  # 窗口
        self.fields = []  # 所有组件(下拉框+输入框)
        if update_data is None:
            pass
        else:
            self.update_data = update_data
        win.title(win_title)  # 设置标题
        common.set_size_center(win, win_width, win_height)  # 设置位置和大小
        self.set_frame(font_family, font_size, entry_width, entry_height, entry_space_x,
                       entry_space_y, head, btn_space,
                       btn_width, split_column, combobox_indent)  # 布局
        self.set_update_data()  # 设置修改的数据
        self.bind_next()

    def set_head(self, head, family, size):
        frame = Frame(self.win)
        Label(frame, text=head, font=(family, size)).pack()  # 设置显示的头
        frame.pack(pady=20)

    def must(self):
        # 获取必填字段
        content = self.custom_content()
        data = []
        for index, one in enumerate(content):
            name = one.get(NAME)  # 名称
            must = one.get(MUST, False)  # 必填
            if must:  # 是必填则记录下标和名称
                data.append((index, name))
        return data

    def set_content(self, family, size, width, height, distance_x, distance_y, split_column,
                    difference):
        frame = Frame(self.win)
        frame.pack()
        content = self.custom_content()
        labels = []
        for one in content:
            text = one.get(NAME)  # 名称
            label = Label(
                master=frame,  # 父容器
                text=text,  # 文本
                font=(family, size),  # 字体
                )
            labels.append(label)  # 保存所以label用于放置
        fields = []
        for one in content:
            name = one.get(NAME)  # 名称
            typeof = one.get(TYPE)  # 类型
            if typeof == ENTRY:
                widget = Entry(frame, text=name, font=(family, size), width=width, )  # 输入框
            elif typeof == COMBOBOX:  # 下拉框
                options = one.get(DATA, {}).get(OPTIONS)  # 获取下拉框选项
                widget = ttk.Combobox(
                    master=frame,  # 父容器
                    height=height,  # 高度,下拉显示的条目数量
                    width=width - difference,  # 宽度
                    state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
                    cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
                    font=(family, size),  # 字体
                    values=options,  # 设置下拉框的选项
                    )
            else:
                widget = None
                print('错误:组件类型有误')
            if one == content[-1]:
                widget.bind(login.RETURN, lambda x: self.affirm())  # 最后一个组件绑定确认按钮事件
            fields.append(widget)  # 保存所有组件(下拉框+输入框)用于布局
        self.fields = fields
        self.fields[0].focus()  # 设置第一个聚焦
        if split_column == 1:  # 只显示一列
            for i, label in enumerate(labels):
                label.grid(row=i, column=0, padx=(0, distance_x), sticky='e')  # 布局labels
            for i, field in enumerate(fields):
                field.grid(row=i, column=1, pady=distance_y)  # 布局所有组件(下拉框+输入框)
        else:  # 显示多列,每列显示split_column个元素
            column = 0
            labels_group = list(self.group(labels, split_column))  # 对labels分组
            fields_group = list(self.group(fields, split_column))  # 对所有组件(下拉框+输入框)分组
            for i, label in enumerate(labels_group):
                row = 0
                for index in range(len(label)):
                    label[index].grid(row=row, column=column, padx=distance_x,
                                      sticky='e')  # 布局labels
                    fields_group[i][index].grid(row=row, column=column + 1,
                                                pady=distance_y)  # 布局所有组件(下拉框+输入框)
                    row += 1
                column += 2

    @staticmethod
    def group(list_data, number):
        # 分组列表数据
        for i in range(0, len(list_data), number):
            yield list_data[i:i + number]  # 迭代器

    def set_update_data(self):
        if self.update_data:  # 如果是修改传入的数据就填入到输入框和下拉框中
            for index, field in enumerate(self.fields):
                if isinstance(field, ttk.Combobox):  # 下拉框
                    field.set(self.update_data[index])  # 设置下拉框的值
                elif isinstance(field, Entry):  # 输入框
                    field.insert(0, self.update_data[index])  # 设置输入框的值
                else:
                    print('错误:对象不存在')

    def _button_frame(self, distance, width):
        frame = Frame(self.win)
        text = 'text'
        color = 'color'
        command = 'command'
        data = [
            {text: '清空', color: 'yellow', command: self.clear},  # 清空按钮
            {text: '取消', color: '#00ffff', command: self.logout},  # 返回按钮
            {text: '确认', color: 'pink', command: self.affirm},  # 确认按钮
            ]
        for i in data:
            name = i.get(text)  # 文本
            bg = i.get(color)  # 颜色
            cmd = i.get(command)
            btn = Button(frame, text=name, bg=bg, width=width, command=cmd)
            btn.pack(side=LEFT, padx=(0, distance))
        frame.pack(pady=20)

    def set_frame(self, family, size, width, height, distance_x, distance_y, head, btn_space,
                  btn_width, split_column,
                  difference):
        self.set_head(head, family, size)
        self.set_content(family, size, width, height, distance_x, distance_y, split_column,
                         difference)
        self._button_frame(btn_space, btn_width)

    def select_frame(self):
        messagebox.showinfo('提示信息', '注册成功')
        common.clear_child(self.win)  # 清空组件
        self.clear()  # 清空数据
        login.LoginFrame(self.win)  # 返回登录页面
        pass

    def logout(self):
        common.clear_child(self.win)  # 清空组件
        self.clear()  # 清空数据
        login.LoginFrame(self.win)  # 返回登录页面
        pass

    def affirm(self):
        # 确认按钮
        data = list(map(lambda x: x.get(), self.fields))  # 获取填入的数据
        must = self.must()  # 必填项
        for i in must:  # 判断必填项
            if data[i[0]].strip() == '':  # 必填项为空
                messagebox.showinfo('提示信息', '[{}]是必填项'.format(i[1]))
                return

        success, msg = self.save(data)  # 保存数据
        if success:
            self.select_frame()
        else:
            messagebox.showerror('错误信息', '注册失败!\n原因:{}'.format(msg))
        pass

    def clear(self):
        # 清空所有组件(下拉框+输入框)
        for field in self.fields:
            if isinstance(field, ttk.Combobox):
                field.set('')  # 下拉框清空
            else:
                field.delete(0, END)  # entry清空输入内容

    def bind_next(self):  # 绑定Enter聚焦事件
        for index, widget in enumerate(self.fields):
            if index + 1 < len(self.fields):
                widget.bind(login.RETURN, lambda x, y=index + 1: self.fields[y].focus())


if __name__ == '__main__':
    w = Tk()
    MyFrame(w)
    w.mainloop()
