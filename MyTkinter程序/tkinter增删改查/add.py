# -*- encoding=utf-8 -*-
import tkinter
import PublicMethod
from tkinter import *

import select


class AddFrame(object):
    def __init__(self, window=None, field_names=['字段1', '字段2', '字段3', '字段4', '字段5']):
        self.window = window
        self.field_names = field_names
        self.labels = []
        self.entrys = []
        pass

    def add(self):
        data = []
        for entry in self.entrys:
            data.append(entry.get())
        print(data)
        pass

    def clear_entry(self):
        for entry in self.entrys:
            entry.delete(0, END)
        pass

    def go_back(self):
        PublicMethod.clear_child(self.window, 'pack')
        select_window = select.SelectFrame(self.window)
        PublicMethod.set_title(self.window, '查询')
        PublicMethod.set_size_center(self.window, 600, 600)
        select_window.set_frame()
        pass

    def set_frame(self):
        frame = tkinter.Frame(self.window)
        add_label = Label(self.window, text='添加信息', font=('', 20))
        for field_name in self.field_names:
            field_name_label = Label(frame, text=field_name)
            self.labels.append(field_name_label)
            self.entrys.append(Entry(frame))
        for row, label in enumerate(self.labels):
            label.grid(row=row, column=0, padx=10, pady=10)
        for row, entry in enumerate(self.entrys):
            entry.grid(row=row, column=1, padx=10, pady=20)
        add_btn = tkinter.Button(frame, text='添加', command=self.add)
        clear_entry_btn = tkinter.Button(frame, text='清除', command=self.clear_entry)
        return_btn = tkinter.Button(frame, text='返回', command=self.go_back)
        add_label.pack(side=tkinter.TOP, padx=10, pady=40)
        frame.pack()
        add_btn.grid(row=len(self.labels) + 1, column=0, padx=10, pady=20)
        clear_entry_btn.grid(row=len(self.labels) + 1, column=1, padx=10, pady=20, )
        return_btn.grid(row=len(self.labels) + 1, column=2, padx=0, pady=20, )


if __name__ == '__main__':
    pass
    main_win = tkinter.Tk()
    add_window = AddFrame(main_win)
    PublicMethod.set_title(add_window.window, '添加')
    PublicMethod.set_size_center(add_window.window, 340, 520)
    add_window.set_frame()
    main_win.mainloop()
