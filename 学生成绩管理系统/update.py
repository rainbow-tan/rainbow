# -*- encoding=utf-8 -*-
import tkinter
from tkinter import *
from tkinter import messagebox

import PublicMethod
import select


class UpdateFrame(object):
    def __init__(self, window=None, field_names=['字段1', '字段2', '字段3', '字段4', '字段5'],
                 field_values=['值1', '值2', '值3', '值4', '值5'],
                 disable_fields=['字段1']):
        # field_names和field_values长度需要一致
        # disable_fields需要是field_names的真子集
        self.window = window
        self.field_names = field_names
        self.field_values = field_values
        self.disable_fields = disable_fields
        self.labels = []
        self.entrys = []
        pass

    def go_back(self):
        PublicMethod.clear_child(self.window, 'pack')
        with open('grade', 'r', encoding='utf-8') as f:
            grade = f.readlines()
        field_data = []
        for i in grade:
            if i.strip() != '':
                score = i.split(',')
                one = (score[0], score[1], score[2], score[3], score[4].strip(),)
                field_data.append(one)
        field_names = ['学号', '姓名', '高数', '大物', '英语']
        select_window = select.SelectFrame(self.window, field_names, field_data)
        PublicMethod.set_title(self.window, '查询')
        PublicMethod.set_size_center(self.window, 600, 600)
        select_window.set_frame()
        pass

    def set_entry_value(self):
        for index, entry in enumerate(self.entrys):
            entry.insert(END, self.field_values[index])

    def set_disable_entry(self):
        disable_index = []
        for index, label in enumerate(self.labels):
            if label.cget('text') in self.disable_fields:
                disable_index.append(index)
        for index in disable_index:
            self.entrys[index].config(state='disabled')

    def update(self):
        data = []
        for entry in self.entrys:
            data.append(entry.get().strip())
        print(data)
        if data[1] == '':
            messagebox.showwarning('提示信息', '姓名不能为空！')
            return
        with open('grade', 'r', encoding='utf-8') as f:
            grade = f.readlines()
        new = []
        for id1 in grade:
            if id1.strip() != '':
                if id1.split(',')[0] == data[0]:
                    id1_new = data[0] + ',' + data[1] + ',' + data[2] + ',' + data[3] + ',' + data[
                        4] + '\n'
                else:
                    new.append(id1)
        a = [id1_new] + new
        with open('grade', 'w')as f:
            pass
        for i in a:
            with open('grade', 'a', encoding='utf-8') as f:
                f.write(i)
                # f.write('\n')
        self.go_back()
        pass

    def clear_entry(self):
        for entry in self.entrys:
            entry.delete(0, END)
        pass

    def set_frame(self):
        frame = tkinter.Frame(self.window)
        update_label = Label(self.window, text='修改信息', font=('', 20))
        for field_name in self.field_names:
            field_name_label = Label(frame, text=field_name)
            self.labels.append(field_name_label)
            self.entrys.append(Entry(frame))
        for row, label in enumerate(self.labels):
            label.grid(row=row, column=0, padx=10, pady=10)
        for row, entry in enumerate(self.entrys):
            entry.grid(row=row, column=1, padx=10, pady=20)
        self.set_entry_value()
        self.set_disable_entry()
        update_btn = tkinter.Button(frame, text='修改', command=self.update)
        clear_entry_btn = tkinter.Button(frame, text='清除', command=self.clear_entry)
        return_btn = tkinter.Button(frame, text='返回', command=self.go_back)

        update_label.pack(side=tkinter.TOP, padx=10, pady=40)
        frame.pack()
        update_btn.grid(row=len(self.labels) + 1, column=0, padx=10, pady=20)
        clear_entry_btn.grid(row=len(self.labels) + 1, column=1, padx=10, pady=20, )
        return_btn.grid(row=len(self.labels) + 1, column=2, padx=0, pady=20, )


if __name__ == '__main__':
    pass
    main_win = tkinter.Tk()
    update_window = UpdateFrame(main_win)
    PublicMethod.set_title(update_window.window, '修改')
    PublicMethod.set_size_center(update_window.window, 340, 520)
    update_window.set_frame()
    main_win.mainloop()
