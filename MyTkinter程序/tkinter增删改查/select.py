# -*- encoding=utf-8 -*-
import tkinter
import PublicMethod
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import add
import update


class SelectFrame(object):
    def __init__(self, window=None, field_names=['字段1', '字段2', '字段3', '字段4', '字段5'],
                 field_data=[('值1', '值2', '值3', '值4', '值5'), ('值11', '值22', '值33', '值44', '值55')]):
        self.window = window
        self.field_names = field_names
        self.tree = None
        self.field_data = field_data
        pass

    def clear_item(self):
        # 获取item并移除
        for child in self.tree.get_children():
            self.tree.delete(child)
        pass

    def add(self):
        PublicMethod.clear_child(self.window, 'pack')
        add_window = add.AddFrame(self.window)
        PublicMethod.set_title(self.window, '添加')
        PublicMethod.set_size_center(self.window, 340, 520)
        add_window.set_frame()
        pass

    def insert_data(self, field_data):
        for data in field_data:  # 插入数据
            self.tree.insert('', END, value=data)

    def update(self):
        selects = self.tree.selection()
        if len(selects) != 1:
            messagebox.showwarning('提示', '选择一条记录进行修改')
        else:
            data = self.tree.item(selects[0], 'values')
            PublicMethod.clear_child(self.window, 'pack')
            update_window = update.UpdateFrame(self.window)
            PublicMethod.set_title(self.window, '修改')
            PublicMethod.set_size_center(self.window, 340, 520)
            update_window.set_frame()
            print(data)

    def delete(self):
        selects = self.tree.selection()
        if len(selects) > 0:
            all_data = []
            for select in selects:
                all_data.append(self.tree.item(select, 'values'))  # 获取item的值
            for data in all_data:
                print(data)
            choose = messagebox.askyesno('提示', '确认删除已选择记录吗？')
            print(choose)
        else:
            messagebox.showwarning('提示', '至少选择一条记录进行删除')

    def set_frame(self):
        frame = tkinter.Frame(self.window)
        select_label = Label(self.window, text='查看信息', font=('', 20))
        self.tree = ttk.Treeview(frame, columns=self.field_names, show='headings')
        for field_name in self.field_names:
            self.tree.column(field_name, width=100)  # 对列进行定义
            self.tree.heading(field_name, text=field_name)
        self.insert_data(self.field_data)
        s = Scrollbar(frame)  # 滚动条
        s.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=s.set)
        frame2 = tkinter.Frame(self.window)
        add_btn = tkinter.Button(frame2, text='添加', command=self.add)
        update_btn = tkinter.Button(frame2, text='修改', command=self.update)
        clear_item_btn = tkinter.Button(frame2, text='清除', command=self.clear_item)
        delete_btn = tkinter.Button(frame2, text='删除', command=self.delete)

        s.pack(side=RIGHT, fill=Y)
        self.tree.pack()
        select_label.pack(side=tkinter.TOP, padx=10, pady=40)
        frame.pack()
        add_btn.grid(row=0, column=0, padx=10, pady=20)
        update_btn.grid(row=0, column=1, padx=10, pady=20)
        delete_btn.grid(row=0, column=2, padx=10, pady=20)
        clear_item_btn.grid(row=0, column=3, padx=10, pady=20)
        frame2.pack()


if __name__ == '__main__':
    pass
    main_win = tkinter.Tk()
    select_window = SelectFrame(main_win)
    PublicMethod.set_title(select_window.window, '查询')
    PublicMethod.set_size_center(select_window.window, 600, 600)
    select_window.set_frame()
    main_win.mainloop()
