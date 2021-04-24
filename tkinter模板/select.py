# -*- encoding=utf-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import common
import edit
import login

NAME = 'name'
WIDTH = 'width'
DEFAULT_WIDTH = 100


class SelectFrame:
    @staticmethod
    def get_head():
        # 重构
        head = [{NAME: '姓名', WIDTH: '100', ANCHOR: CENTER},
                {NAME: '性别', WIDTH: '50', ANCHOR: CENTER},
                {NAME: '年龄', WIDTH: '50', ANCHOR: E},
                {NAME: '班级', WIDTH: '100', ANCHOR: CENTER},
                {NAME: '备注', WIDTH: '100', ANCHOR: CENTER},
                ]
        return head

    @staticmethod
    def get_data():
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
        return success, msg

    def __init__(self,
                 win,  # 窗口
                 title='查询',  # 窗口标题
                 width=500,  # 窗口宽度
                 height=400,  # 窗口高度
                 line=10,  # 显示的行数
                 min_column_width=50,  # 最小的列宽
                 button_distance=10,  # 按钮的间距
                 button_width=10):  # 按钮的宽度
        self.win = win

        win.title(title)
        common.set_size_center(win, width, height)  # 设置位置
        self._set_frame(line, min_column_width, button_distance, button_width)
        self.refresh()

    def _table_frame(self, height, min_column_width):
        frame = Frame(self.win)
        frame.pack()
        scrollbar_y = Scrollbar(frame, orient=VERTICAL)
        scrollbar_x = Scrollbar(frame, orient=HORIZONTAL)
        head = self.get_head()
        columns = list(map(lambda x: x.get(NAME), head))
        self.table = ttk.Treeview(
            master=frame,  # 父容器
            height=height,  # 高度,可显示height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列
            yscrollcommand=scrollbar_y.set,  # 滚动条
            xscrollcommand=scrollbar_x.set,  # 滚动条
            )
        for one in head:
            name = one.get(NAME, '')
            anchor = one.get(ANCHOR, LEFT)
            width = one.get(WIDTH, DEFAULT_WIDTH)
            self.table.heading(name, text=name, anchor=anchor)
            self.table.column(name, width=width, anchor=anchor, minwidth=min_column_width)
        scrollbar_y.config(command=self.table.yview)
        scrollbar_x.config(command=self.table.xview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        self.table.pack()

    def _head_frame(self):
        frame = Frame(self.win)
        Label(frame, text='信息详情阅览', font=('黑体', 20)).pack()
        frame.pack(pady=30)

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

    def _set_frame(self, height, min_column_width, button_distance, button_width):
        self._head_frame()
        self._table_frame(height, min_column_width)
        self._button_frame(button_distance, button_width)
        pass

    def refresh(self):
        self._clear()  # 清空所有数据
        data = self.get_data()  # 获取数据
        self._insert_data(data)  # 插入数据

    def add(self):
        common.clear_child(self.win)  # 清空元素
        edit.MyFrame(self.win, update_data=[])  # 添加页面
        pass

    def update(self):
        selects = self.table.selection()
        if len(selects) != 1:
            messagebox.showwarning('提示', '选择一条记录进行修改')
        else:
            data = self.table.item(selects[0], 'values')  # 获取选中的数据
            common.clear_child(self.win)  # 清空组件
            edit.MyFrame(self.win, update_data=data)  # 修改界面
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
