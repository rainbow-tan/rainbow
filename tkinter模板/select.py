# -*- encoding=utf-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import common
import edit
import login

NAME = 'name'
WIDTH = 'width'


class SelectFrame:
    @staticmethod
    def get_head():  # 显示的字段
        # 重构
        head = [{NAME: '姓名', WIDTH: '100', ANCHOR: CENTER},
                {NAME: '性别', WIDTH: '50', ANCHOR: CENTER},
                {NAME: '年龄', WIDTH: '50', ANCHOR: E},
                {NAME: '班级', WIDTH: '100', ANCHOR: CENTER},
                {NAME: '备注', WIDTH: '100', ANCHOR: CENTER},
                ]
        return head

    @staticmethod
    def get_data():  # 显示的数据
        # 重构
        data = [
            ['小红1', '~', '+', '高2015-3班', '~'],
            ['小红1', '~', '+', '高2015-4班', '~'],
            ['小红1', '~', '/', '高2015-5班', '~'],
            ['小红1', '~', '+', '高2015-6班', '~'],
            ['小红1', '~', '+', '高2015-7班', '~'],
            ]
        return data

    @staticmethod
    def delete(data):
        # 重构
        # [('小红1', '~', '+', '高2015-6班', '~'), ('小红1', '~', '+', '高2015-7班', '~')]
        success = True
        msg = ''
        for one in data:  # 遍历选择的数据
            print(one)
            pass  # 一条一条删除
        return success, msg

    def __init__(self,
                 win,  # 窗口
                 title='查询',  # 窗口标题
                 width=500,  # 窗口宽度
                 height=400,  # 窗口高度
                 line=10,  # 显示的行数
                 button_distance=10,  # 按钮的间距
                 button_width=10):  # 按钮的宽度
        self.win = win

        win.title(title)  # 设置标题
        common.middle_windows(win, width, height)  # 设置窗口居中
        self._set_frame(line, button_distance, button_width)  # 布局Frame
        self.refresh()  # 刷新

    def _table_frame(self, height):  # 表格Frame
        frame = Frame(self.win)  # Frame组件
        frame.pack()  # 放置Frame
        scrollbar_y = Scrollbar(frame, orient=VERTICAL)  # y轴滚动条
        scrollbar_x = Scrollbar(frame, orient=HORIZONTAL)  # x轴滚动条
        head = self.get_head()  # 显示的字段
        columns = list(map(lambda x: x.get(NAME), head))  # 获取表头的名称
        self.table = ttk.Treeview(
                master=frame,  # 父容器
                height=height,  # 高度,可显示height行
                columns=columns,  # 显示的列
                show='headings',  # 隐藏首列
                yscrollcommand=scrollbar_y.set,  # y轴滚动条的滚动函数与表绑定
                xscrollcommand=scrollbar_x.set,  # x轴滚动条的滚动函数与表绑定
                )
        for one in head:
            name = one.get(NAME)  # 显示的名称
            anchor = one.get(ANCHOR)  # 显示的对齐方式
            width = one.get(WIDTH)  # 显示的宽度
            self.table.heading(name, text=name, anchor=anchor)  # 设置表头的名称
            self.table.column(name, width=width, anchor=anchor, minwidth=width)  # 设置列
        scrollbar_y.config(command=self.table.yview)  # y轴滚动条滚动函数
        scrollbar_x.config(command=self.table.xview)  # x轴滚动条滚动函数
        scrollbar_y.pack(side=RIGHT, fill=Y)  # 放置y滚动条
        scrollbar_x.pack(side=BOTTOM, fill=X)  # 放置x滚动条
        self.table.pack()  # 放置表格

    def _head_frame(self):
        frame = Frame(self.win)  # Frame组件
        Label(frame, text='信息详情阅览', font=('黑体', 20)).pack()  # label组件
        frame.pack(pady=(30, 0))  # 放置frame

    def _button_frame(self, distance, width):
        frame = Frame(self.win)
        text = 'text'
        color = 'color'
        command = 'command'
        data = [
            {text: '刷新', color: 'yellow', command: self.refresh},
            {text: '添加', color: 'pink', command: self.add},
            {text: '修改', color: '#00ffff', command: self.update},
            {text: '删除', color: 'green', command: self._delete_choose},
            {text: '注销', color: '#ff8000', command: self.logout},
            ]
        for i in data:
            name = i.get(text)
            bg = i.get(color)
            cmd = i.get(command)
            btn = Button(frame, text=name, bg=bg, width=width, command=cmd)
            btn.pack(side=LEFT, padx=(0, distance))
        frame.pack(pady=10)

    def _set_frame(self, height, button_distance, button_width):
        self._head_frame()
        self._table_frame(height)
        self._button_frame(button_distance, button_width)
        pass

    def refresh(self):
        self._clear()  # 清空所有数据
        data = self.get_data()  # 获取数据
        self._insert_data(data)  # 插入数据

    def add(self):
        common.clear_child(self.win)  # 清空元素
        edit.EditFrame(self.win, update_data=[])  # 添加页面
        pass

    def update(self):
        selects = self.table.selection()
        if len(selects) != 1:
            messagebox.showwarning('提示', '选择一条记录进行修改')
        else:
            data = self.table.item(selects[0], 'values')  # 获取选中的数据
            common.clear_child(self.win)  # 清空组件
            edit.EditFrame(self.win, update_data=data)  # 修改界面
            pass

    def _delete_choose(self):
        selection = self.table.selection()  # 获取选中的数据
        data = []
        for select in selection:
            data.append(self.table.item(select, 'values'))  # 获取item的值
        if selection:
            flag = messagebox.askyesno('提示信息', '确认删除选中数据?')
            if flag:
                success, msg = self.delete(data)  # 删除数据
                if success:
                    for item in selection:
                        self.table.delete(item)  # 删除页面行数
                else:
                    messagebox.showinfo('提示信息', '删除失败!\n异常:{}'.format(msg))
        else:
            messagebox.showwarning('提示', '至少选择一条记录进行删除!')

    def _clear(self):
        for child in self.table.get_children():
            self.table.delete(child)  # 清空所有的数据

    def _insert_data(self, data):
        for value in data:
            self.table.insert('', END, value=value)  # 插入数据

    def logout(self):
        common.clear_child(self.win)  # 清空组件
        login.LoginFrame(self.win)  # 登录界面
        pass


if __name__ == '__main__':
    pass
    w = Tk()
    obj = SelectFrame(w)
    w.mainloop()
