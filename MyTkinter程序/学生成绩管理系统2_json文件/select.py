# -*- encoding=utf-8 -*-
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import common
import edit
import login
from pub import load_json
from pub import write_dict

NAME = 'name'
WIDTH = 'width'
DEFAULT_WIDTH = 100
GRADE_FILE_NAME = 'grade.json'
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
CLASS_NAME = "class_name"
COURSE_TITLE = "course_title"
USUAL_SCORE = "usual_score"
TEST_SCORE = "test_score"
FINAL_SCORE = "final_score"
import tkinter.colorchooser as cc
from tkinter import *


def choose_color():
    choose = cc.askcolor()
    print(choose)
    color_value = choose[1]
    # button.config(bg=color_value)


def save(grades):
    success = True
    msg = ''
    new = []
    for one in grades:
        data_dict = dict()
        data_dict[STUDENT_ID] = one[0]
        data_dict[STUDENT_NAME] = one[1]
        data_dict[CLASS_NAME] = one[2]
        data_dict[COURSE_TITLE] = one[3]
        data_dict[USUAL_SCORE] = one[4]
        data_dict[TEST_SCORE] = one[5]
        data_dict[FINAL_SCORE] = one[6]
        new.append(data_dict)
    try:
        write_dict(GRADE_FILE_NAME, new, encoding='utf-8')
    except Exception as e:
        success = False
        msg = '{}'.format(e)
    return success, msg


class SelectFrame:
    @staticmethod
    def get_head():
        # 重构
        head = [{NAME: '学号', WIDTH: '80', ANCHOR: CENTER, },
                {NAME: '姓名', WIDTH: '80', ANCHOR: CENTER, },
                {NAME: '班级', WIDTH: '80', ANCHOR: CENTER, },
                {NAME: '课程名称', WIDTH: '100', ANCHOR: CENTER, },
                {NAME: '平时成绩', WIDTH: '80', ANCHOR: CENTER, },
                {NAME: '考试成绩', WIDTH: '80', ANCHOR: CENTER, },
                {NAME: '最终成绩', WIDTH: '80', ANCHOR: CENTER, },
                ]
        return head

    @staticmethod
    def get_data():
        # 重构
        json_data = load_json(GRADE_FILE_NAME)
        grades = list(map(lambda x: [
            x.get(STUDENT_ID, ''),
            x.get(STUDENT_NAME, ''),
            x.get(CLASS_NAME, ''),
            x.get(COURSE_TITLE, ''),
            x.get(USUAL_SCORE, ''),
            x.get(TEST_SCORE, ''),
            x.get(FINAL_SCORE, '')
            ], json_data))
        grades.sort()
        print('所有学生的信息:{}'.format(grades))
        # data = [
        #     ['1001', '~', '+', '高2015-3班', '~', '高2015-3班', '~'],
        #     ['小红1', '~', '+', '高2015-3班', '~', '高2015-3班', '~'],
        #     ['小红1', '~', '+', '高2015-3班', '~', '高2015-3班', '~'],
        #     ['小红1', '~', '+', '高2015-3班', '~', '高2015-3班', '~'],
        #     ]
        return grades

    @staticmethod
    def delete(data):
        # 重构
        # [('小红1', '~', '+', '高2015-6班', '~'), ('小红1', '~', '+', '高2015-7班', '~')]

        success = True
        msg = ''
        json_data = load_json(GRADE_FILE_NAME)
        grades = list(map(lambda x: [
            x.get(STUDENT_ID, ''),
            x.get(STUDENT_NAME, ''),
            x.get(CLASS_NAME, ''),
            x.get(COURSE_TITLE, ''),
            x.get(USUAL_SCORE, ''),
            x.get(TEST_SCORE, ''),
            x.get(FINAL_SCORE, '')
            ], json_data))
        print('所有学生成绩信息是:{}'.format(grades))
        remove_ids = []
        for delete_one in data:
            delete_one = list(delete_one)
            print('要删除的信息是{}'.format(delete_one))
            for one in grades:
                # print('原来')
                if delete_one == one:
                    print('找到要删除的下标:{}'.format(grades.index(one)))
                    remove_ids.append(grades.index(one))
                    # print(score_data.index(one))
        remove_ids.sort()
        remove_ids.reverse()
        print('要删除的下标有:{}'.format(remove_ids))
        for remove_id in remove_ids:
            grades.pop(remove_id)
        print('删除后的学生剩余信息:{}'.format(grades))
        success, msg = save(grades)
        return success, msg

    def __init__(self,
                 win,  # 窗口
                 title='查询',  # 窗口标题
                 width=800,  # 窗口宽度
                 height=500,  # 窗口高度
                 line=10,  # 显示的行数
                 button_distance=10,  # 按钮的间距
                 button_width=10):  # 按钮的宽度
        self.win = win

        win.title(title)
        common.set_size_center(win, width, height)  # 设置位置
        self._set_frame(line, button_distance, button_width)
        self.refresh()

    def search(self):
        grades = self.get_data()

        # choose_color()
        stu_id = self.stu_entry.get().strip()
        print('要查询的学号是:{}'.format(stu_id))
        stu_name = self.name_entry.get().strip()
        print('要查询的姓名是:{}'.format(stu_name))
        if stu_id and stu_name:
            see_data = []
            for grade in grades:
                grade_id = grade[0]
                grade_name = grade[1]
                if grade_id == stu_id and grade_name == stu_name:
                    see_data.append(grade)
            self._clear()
            self._insert_data(see_data)
        elif stu_id and not stu_name:
            see_data = []
            for grade in grades:
                grade_id = grade[0]
                if grade_id == stu_id:
                    see_data.append(grade)
            self._clear()
            self._insert_data(see_data)
        elif stu_name and not stu_id:
            see_data = []
            for grade in grades:
                grade_name = grade[1]
                if grade_name == stu_name:
                    see_data.append(grade)
            self._clear()
            self._insert_data(see_data)
        else:
            pass

        pass

    def _head_frame(self):
        frame = Frame(self.win)
        Label(frame, text='信息详情阅览', font=('黑体', 20)).pack()
        frame.pack(pady=30)

    def _table_frame(self, height, ):
        frame = Frame(self.win, )
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
            # min_width = one.get(MINWIDTH, DEFAULT_WIDTH)
            self.table.heading(name, text=name, anchor=anchor)
            self.table.column(name, width=width, anchor=anchor, minwidth=width)
        scrollbar_y.config(command=self.table.yview)
        scrollbar_x.config(command=self.table.xview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        self.table.pack(fill=BOTH, expand=True)

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
            {text: '统计', color: '#8080ff', command: self.statistics},
            {text: '注销', color: '#ff8000', command: self.logout},
            ]
        for i in data:
            name = i.get(text)
            bg = i.get(color)
            cmd = i.get(command)
            btn = Button(frame, text=name, bg=bg, width=width, command=cmd)
            btn.pack(side=LEFT, padx=(0, distance))
        frame.pack(pady=10)

    def statistics(self):
        grades = self.get_data()
        if grades:
            s = 0
            for grade in grades:
                if grade[4]:
                    s += int(grade[4])
            mean = s / len(grades)
            mean = '{:.2f}'.format(mean)
            print('平时成绩的均值是:{}'.format(mean))
            self.usual_label.config(text=mean)
            s = 0
            for grade in grades:
                if grade[5]:
                    s += int(grade[5])
            mean = s / len(grades)
            mean = '{:.2f}'.format(mean)
            print('考试成绩的均值是:{}'.format(mean))
            self.test_label.config(text=mean)
            s = 0
            for grade in grades:
                if grade[6]:
                    s += int(grade[6])
            mean = s / len(grades)
            mean = '{:.2f}'.format(mean)
            print('最终成绩的均值是:{}'.format(mean))
            self.final_label.config(text=mean)
        if grades:
            usual = list(map(lambda x:x[4],grades))
            usual = list(map(lambda x:x if x else '0' ,usual))
            usual = list(map(lambda x:int(x),usual))
            print('平时成绩是:{}'.format(usual))
            variance = '{:.2f}'.format(np.var(usual))
            print('平时成绩方差是:{}'.format(variance))
            self.usual_label2.config(text=variance)

            usual = list(map(lambda x:x[5],grades))
            usual = list(map(lambda x:x if x else '0' ,usual))
            usual = list(map(lambda x:int(x),usual))
            print('考试成绩是:{}'.format(usual))
            variance = '{:.2f}'.format(np.var(usual))
            print('考试成绩方差是:{}'.format(variance))
            self.test_label2.config(text=variance)

            usual = list(map(lambda x:x[6],grades))
            usual = list(map(lambda x:x if x else '0' ,usual))
            usual = list(map(lambda x:int(x),usual))
            print('最终成绩是:{}'.format(usual))
            variance = '{:.2f}'.format(np.var(usual))
            print('最终成绩方差是:{}'.format(variance))
            self.final_label2.config(text=variance)



    def _search_frame(self):
        frame = Frame()
        label_font = ('宋体', 16)
        Label(frame, text='学  号', font=label_font).pack(side=LEFT)
        entry_width = 12
        self.stu_entry = Entry(frame, font=label_font, width=entry_width)
        padx_entry_label = 10
        self.stu_entry.pack(side=LEFT, padx=padx_entry_label)
        Label(frame, text='姓  名', font=label_font).pack(side=LEFT)
        self.name_entry = Entry(frame, font=label_font, width=entry_width)
        self.name_entry.pack(side=LEFT, padx=padx_entry_label)
        frame.pack(pady=(5, 15))
        Button(frame, text='查询', width=8, bg='#00ff00', reli='g', font=('宋体', 12), command=self.search).pack(side=LEFT,
                                                                                                             padx=10)

    def _statistics_frame(self):
        frame = Frame()
        frame.pack()
        frame1 = Frame(frame)
        label_font = ('宋体', 16)
        x_distance = 0
        label_width = 8
        Label(frame1, text='均值:', font=label_font).pack(side=LEFT, padx=(0, 0))
        Label(frame1, text='平时成绩', font=label_font).pack(side=LEFT, padx=(0, 0))
        self.usual_label = Label(frame1, text='', reli='g', width=label_width, font=label_font)
        self.usual_label.pack(side=LEFT, padx=(x_distance, 0))
        Label(frame1, text='考试成绩', font=label_font).pack(side=LEFT, padx=(x_distance, 0))
        self.test_label = Label(frame1, text='', reli='g', width=label_width, font=label_font)
        self.test_label.pack(side=LEFT, padx=(x_distance, 0))
        Label(frame1, text='最终成绩', font=label_font).pack(side=LEFT, padx=(x_distance, 0))
        self.final_label = Label(frame1, text='', reli='g', width=label_width, font=label_font)
        self.final_label.pack(side=LEFT, padx=(x_distance, 0))
        frame1.pack()

        frame2 = Frame(frame)
        label_font = ('宋体', 16)
        Label(frame2, text='方差:', font=label_font).pack(side=LEFT, padx=(0, 0))
        Label(frame2, text='平时成绩', font=label_font).pack(side=LEFT, padx=(0, 0))
        self.usual_label2 = Label(frame2, text='', reli='g', width=label_width, font=label_font)
        self.usual_label2.pack(side=LEFT, padx=(x_distance, 0))
        Label(frame2, text='考试成绩', font=label_font).pack(side=LEFT, padx=(x_distance, 0))
        self.test_label2 = Label(frame2, text='', reli='g', width=label_width, font=label_font)
        self.test_label2.pack(side=LEFT, padx=(x_distance, 0))
        Label(frame2, text='最终成绩', font=label_font).pack(side=LEFT, padx=(x_distance, 0))
        self.final_label2 = Label(frame2, text='', reli='g', width=label_width, font=label_font)
        self.final_label2.pack(side=LEFT, padx=(x_distance, 0))
        frame2.pack()
        pass

    def _set_frame(self, height, button_distance, button_width):
        self._head_frame()
        self._search_frame()
        self._table_frame(height, )
        self._button_frame(button_distance, button_width)
        self._statistics_frame()
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
            edit.MyFrame(self.win, update_data=data,head='修改信息')  # 修改界面
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
