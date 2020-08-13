# -*- encoding=utf-8 -*-
import tkinter
import PublicMethod
from tkinter import *

import select


class DeleteFrame(object):
    def __init__(self, window=None, field_names=['字段1', '字段2', '字段3', '字段4', '字段5'],
                 field_values=['值1', '值2', '值3', '值4', '值5']):
        # field_names和field_values长度需要一致
        # disable_fields需要是field_names的真子集
        self.window = window
        self.field_names = field_names
        self.field_values = field_values
        self.labels = []
        self.entrys = []
        pass

    def set_entry_value(self):
        for index, entry in enumerate(self.entrys):
            entry.insert(END, self.field_values[index])
            entry['state'] = 'disabled'

    def delete(self):
        data = []
        for entry in self.entrys:
            data.append(entry.get())
        print(data)
        pass

    def go_back(self):
        PublicMethod.clear_child(self.window, 'pack')
        PublicMethod.clear_child(self.window, 'pack')
        select_window = select.SelectFrame(self.window)
        PublicMethod.set_title(self.window, '查询')
        PublicMethod.set_size_center(self.window, 600, 600)
        select_window.set_frame()
        pass

    def set_frame(self):
        frame = tkinter.Frame(self.window)
        delete_label = Label(self.window, text='删除信息', font=('', 20))
        for field_name in self.field_names:
            field_name_label = Label(frame, text=field_name)
            self.labels.append(field_name_label)
            self.entrys.append(Entry(frame))
        for row, label in enumerate(self.labels):
            label.grid(row=row, column=0, padx=10, pady=10)
        for row, entry in enumerate(self.entrys):
            entry.grid(row=row, column=1, padx=10, pady=20)
        self.set_entry_value()
        return_btn = tkinter.Button(frame, text='返回', command=self.go_back)
        delete_btn = tkinter.Button(frame, text='删除', command=self.delete)
        delete_label.pack(side=tkinter.TOP, padx=10, pady=40)
        frame.pack()
        delete_btn.grid(row=len(self.labels) + 1, column=0, padx=10, pady=20)
        return_btn.grid(row=len(self.labels) + 1, column=1, padx=10, pady=20, sticky='e')


if __name__ == '__main__':
    pass
    main_win = tkinter.Tk()
    delete_window = DeleteFrame(main_win)
    PublicMethod.set_title(delete_window.window, '删除')
    PublicMethod.set_size_center(delete_window.window, 340, 520)
    delete_window.set_frame()
    main_win.mainloop()
