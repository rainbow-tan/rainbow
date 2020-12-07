# -*- encoding=utf-8 -*-
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import PublicMethod
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
        with open('grade', 'w')as f:
            pass
        pass

    def add(self):
        PublicMethod.clear_child(self.window, 'pack')
        add_window = add.AddFrame(self.window, field_names=['学号', '姓名', '高数', '大物', '英语'])
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
            update_window = update.UpdateFrame(self.window, ['学号', '姓名', '高数', '大物', '英语'], data,
                                               ['学号'])
            PublicMethod.set_title(self.window, '修改')
            PublicMethod.set_size_center(self.window, 340, 520)
            update_window.set_frame()

    def delete(self):
        selects = self.tree.selection()
        if len(selects) > 0:
            all_data = []
            for select in selects:
                all_data.append(self.tree.item(select, 'values'))  # 获取item的值
            remove_ids = []
            for data in all_data:
                remove_ids.append(data[0])
            # print('要删掉的id：{}'.format(remove_ids))
            choose = messagebox.askyesno('提示', '确认删除已选择记录吗？')
            if choose:
                with open('grade', 'r', encoding='utf-8') as f:
                    grade = f.readlines()
                new = []
                for id1 in grade:
                    if id1.strip() != '':
                        if id1.split(',')[0] in remove_ids:
                            pass
                        else:
                            new.append(id1)
                with open('grade', 'w')as f:
                    pass
                for i in new:
                    with open('grade', 'a', encoding='utf-8') as f:
                        f.write(i)

                PublicMethod.clear_child(self.window)
                self.window.update()

                with open('grade', 'r', encoding='utf-8') as f:
                    grade = f.readlines()
                field_data = []
                for i in grade:
                    if i.strip() != '':
                        score = i.split(',')
                        one = (score[0], score[1], score[2], score[3], score[4].strip(),)
                        field_data.append(one)
                field_names = ['学号', '姓名', '高数', '大物', '英语']
                select_window = SelectFrame(self.window, field_names, field_data)
                PublicMethod.set_title(self.window, '查询')
                PublicMethod.set_size_center(self.window, 600, 600)
                select_window.set_frame()
        else:
            messagebox.showwarning('提示', '至少选择一条记录进行删除')

    def total_points(self):
        with open('grade', 'r', encoding='utf-8') as f:
            grade = f.readlines()
        gaoshu = []
        dawu = []
        yingyu = []
        for i in grade:
            if i.strip() != '':
                score = i.split(',')
                gaoshu.append(score[2])
                dawu.append(score[3])
                yingyu.append(score[4].strip())
        print('高数:{}'.format(gaoshu))
        print('大物:{}'.format(dawu))
        print('英语:{}'.format(yingyu))
        s = 0
        for i in gaoshu:
            if i != '':
                s += float(i)
        self.label_score1.config(text='高数总分:{:.2f}'.format(s))
        self.label_score4.config(text='高数平均分:{:.2f}'.format(s / len(gaoshu)))
        s1 = 0
        for i in dawu:
            if i != '':
                s1 += float(i)
        self.label_score2.config(text='大物总分:{:.2f}'.format(s1))
        self.label_score5.config(text='大物平均分:{:.2f}'.format(s1 / len(dawu)))
        s2 = 0
        for i in yingyu:
            if i != '':
                s2 += float(i)
        self.label_score3.config(text='英语总分:{:.2f}'.format(s2))
        self.label_score6.config(text='英语平均分:{:.2f}'.format(s2 / len(yingyu)))

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
        self.frame2 = tkinter.Frame(self.window)
        add_btn = tkinter.Button(self.frame2, text='添加', command=self.add)
        update_btn = tkinter.Button(self.frame2, text='修改', command=self.update)
        clear_item_btn = tkinter.Button(self.frame2, text='清除', command=self.clear_item)
        delete_btn = tkinter.Button(self.frame2, text='删除', command=self.delete)
        a = tkinter.Button(self.frame2, text='总分和平均分', command=self.total_points)

        s.pack(side=RIGHT, fill=Y)
        self.tree.pack()
        select_label.pack(side=tkinter.TOP, padx=10, pady=40)
        frame.pack()
        add_btn.grid(row=0, column=0, padx=10, pady=20)
        update_btn.grid(row=0, column=1, padx=10, pady=20)
        delete_btn.grid(row=0, column=2, padx=10, pady=20)
        clear_item_btn.grid(row=0, column=3, padx=10, pady=20)
        a.grid(row=0, column=4, padx=10, pady=20)
        self.frame2.pack()

        fame3 = Frame(width=300, height=200, relief='g', )
        self.label_score1 = Label(fame3, text='全班高数总分:')
        self.label_score1.grid(row=0, column=0)
        self.label_score2 = Label(fame3, text='全班大物总分:')
        self.label_score2.grid(row=1, column=0)
        self.label_score3 = Label(fame3, text='全班英语总分:')
        self.label_score3.grid(row=2, column=0)
        self.label_score4 = Label(fame3, text='全班高数平均分:')
        self.label_score4.grid(row=0, column=1, padx=30)
        self.label_score5 = Label(fame3, text='全班大物平均分:')
        self.label_score5.grid(row=1, column=1)
        self.label_score6 = Label(fame3, text='全班英语平均分:')
        self.label_score6.grid(row=2, column=1)
        fame3.pack()


if __name__ == '__main__':
    pass
    main_win = tkinter.Tk()
    select_window = SelectFrame(main_win)
    PublicMethod.set_title(select_window.window, '查询')
    PublicMethod.set_size_center(select_window.window, 600, 600)
    select_window.set_frame()
    main_win.mainloop()
