# -*- encoding=utf-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import common
import login
from pub import load_json
import select

NAME = 'name'
TYPE = 'type'
DATA = 'data'
ENTRY = 'entry'
COMBOBOX = 'combobox'
OPTIONS = 'options'
MUST = 'must'

W = 0.5


class MyFrame:
    @staticmethod
    def custom_content():
        # 重构显示的字段
        content = [
            # {NAME: '姓名', TYPE: ENTRY, MUST: True, DATA: {}, },
            # {NAME: '性别', TYPE: COMBOBOX, MUST: False, DATA: {OPTIONS: ['男', '女']}},
            # {NAME: '年龄', TYPE: ENTRY, MUST: True, DATA: {}},
            # {NAME: '班级', TYPE: ENTRY, MUST: False, DATA: {}},
            # {NAME: '备注', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '学    号', TYPE: ENTRY, MUST: True, },
            {NAME: '姓    名', TYPE: ENTRY, MUST: True, },
            {NAME: '班    级', TYPE: ENTRY, MUST: True, },
            {NAME: '课程名称', TYPE: ENTRY, MUST: True, },
            {NAME: '平时成绩', TYPE: ENTRY, MUST: False, },
            {NAME: '考试成绩', TYPE: ENTRY, MUST: False, },
            {NAME: '最终成绩', TYPE: ENTRY, MUST: False, },
            ]
        return content

    def save(self, data):
        data = list(map(lambda x: str(x).strip(), data))
        # 重构保存和修改信息
        # ['盖聂', '男', '20', '计算15-9班', '学习委员']
        success = True
        msg = ''
        print('界面的数据是:{}'.format(data))
        if data[4]:
            try:
                int(data[4])
            except Exception as e:
                return False, '平时成绩必须是int类型'
                pass
        if data[5]:
            try:
                int(data[5])
            except Exception as e:
                return False, '考试成绩必须是int类型'
                pass
        if data[4] and data[5]:
            data[6] = int(int(data[4]) * W + int(data[5]) * (1 - W))
        data = list(map(lambda x: str(x), data))
        student_id = data[0]
        course_title = data[3]
        json_data = load_json(select.GRADE_FILE_NAME)
        print('成绩文件数据是:{}'.format(json_data))
        grades = list(map(lambda x: [
            x.get(select.STUDENT_ID, ''),
            x.get(select.STUDENT_NAME, ''),
            x.get(select.CLASS_NAME, ''),
            x.get(select.COURSE_TITLE, ''),
            x.get(select.USUAL_SCORE, ''),
            x.get(select.TEST_SCORE, ''),
            x.get(select.FINAL_SCORE, '')
            ], json_data))
        print('所有学生成绩是:{}'.format(grades))
        if self.update_data:
            update_index = -1
            print('此次是修改')
            for index, one in enumerate(grades):
                print('一个学生的成绩是:{}'.format(one))
                one_id = one[0]
                one_course_title = one[3]
                if one_id == student_id and one_course_title == course_title:
                    print('找到学号+课程的唯一值,可以修改了:{}'.format(one))
                    update_index = index
                    break
            if update_index != -1:
                pass
                grades[update_index] = data

            else:
                success = False
                msg = '未找到学号+课程的唯一值!'
            print('修改后的所有学生成绩:{}'.format(grades))
        else:
            print('此次是添加')
            for one in grades:
                print('一个学生的成绩是:{}'.format(one))
                one_id = one[0]
                one_course_title = one[3]
                if one_id == student_id and one_course_title == course_title:
                    print('找到学号+课程的唯一值:{}'.format(one))
                    success = False
                    msg = '学号+课程名称已存在!'
                    break
            else:
                print('未找到学号+课程的唯一值,可以新增')
                grades.append(data)
        # new = []
        # for one in grades:
        #     data_dict = dict()
        #     data_dict[select.STUDENT_ID] = one[0]
        #     data_dict[select.STUDENT_NAME] = one[1]
        #     data_dict[select.CLASS_NAME] = one[2]
        #     data_dict[select.COURSE_TITLE] = one[3]
        #     data_dict[select.USUAL_SCORE] = one[4]
        #     data_dict[select.TEST_SCORE] = one[5]
        #     data_dict[select.FINAL_SCORE] = one[6]
        #     new.append(data_dict)
        # try:
        #     write_dict(select.GRADE_FILE_NAME, new, encoding='utf-8')
        # except Exception as e:
        #     success = False
        #     msg = '{}'.format(e)
        select.save(grades)
        return success, msg
        pass

    def extra_all(self):
        # print('额外函数')
        pass
        self.fields[6].config(state='readonly')

    def extra_for_update(self):
        print('设置只读')
        pass
        # 重构额外函数,一般用于修改时设置readonly
        self.fields[0].config(state='readonly')
        self.fields[3].config(state='readonly')

    def __init__(self, win,
                 win_width=800,  # 窗口宽度
                 win_height=380,  # 窗口高度
                 win_title='数据编辑',  # 窗口标题
                 head='添加信息',  # 显示头信息
                 font_family='宋体',  # 字体
                 font_size=20,  # 字体大小
                 entry_width=12,  # 输入框宽度
                 entry_height=5,  # 下拉显示的条目数量
                 entry_space_x=20,  # label和entry在x轴的间距
                 entry_space_y=10,  # 上一行和下一行y轴的间距
                 combobox_indent=1,  # 输入框和下拉框长度之差
                 btn_space=20,  # 按钮在x轴间距
                 btn_width=18,  # 按钮的宽度
                 split_column=4,  # 1表示显示在一列,其他大于1的数字表示每列显示几个元素,即几行
                 update_data=[]  # 修改传入的数据
                 ):
        self.win = win  # 窗口
        self.fields = []  # 所有组件(下拉框+输入框)
        if update_data is None:
            self.update_data = ['盖聂', '男', '20', '计算15-9班', '学习委员']  # 模拟修改数据
        else:
            self.update_data = update_data
        win.title(win_title)  # 设置标题
        common.set_size_center(win, win_width, win_height)  # 设置位置和大小
        self.set_frame(font_family, font_size, entry_width, entry_height, entry_space_x, entry_space_y, head, btn_space,
                       btn_width, split_column, combobox_indent)  # 布局
        self.set_update_data()  # 设置修改的数据
        self.extra_all()
        if update_data:
            self.extra_for_update()
        else:
            pass
            self.fields[6].config(state='normal')
            self.clear()
            self.fields[6].config(state='readonly')

    def set_head(self, head, family, size):
        frame = Frame(self.win)
        Label(frame, text=head, font=(family, size)).pack()  # 设置显示的头
        frame.pack(pady=20)

    def must(self):
        # 获取必填字段
        # e.g.[(0,'姓名'),(2,'年龄')]
        content = self.custom_content()
        data = []
        for index, one in enumerate(content):
            name = one.get(NAME)  # 名称
            must = one.get(MUST, False)  # 必填
            if must:  # 是必填则记录下标和名称
                data.append((index, name))
        return data

    def set_content(self, family, size, width, height, distance_x, distance_y, split_column, difference):
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
                    label[index].grid(row=row, column=column, padx=distance_x, sticky='e')  # 布局labels
                    fields_group[i][index].grid(row=row, column=column + 1, pady=distance_y)  # 布局所有组件(下拉框+输入框)
                    row += 1
                column += 2

    @staticmethod
    def group(list_data, number):
        # 分组列表数据
        for i in range(0, len(list_data), number):
            yield list_data[i:i + number]  # 迭代器

    def set_update_data(self):
        if self.update_data:  # 如果是修改传入的数据就填入到输入框和下拉框中
            self.fields[6].config(state='normal')
            self.clear()
            for index, field in enumerate(self.fields):
                if isinstance(field, ttk.Combobox):  # 下拉框
                    field.set(self.update_data[index])  # 设置下拉框的值
                elif isinstance(field, Entry):  # 输入框
                    field.insert(0, self.update_data[index])  # 设置输入框的值
                else:
                    print('错误:对象不存在')
            self.fields[6].config(state='normal')

    def _button_frame(self, distance, width):
        frame = Frame(self.win)
        text = 'text'
        color = 'color'
        command = 'command'
        data = [
            {text: '清空', color: 'yellow', command: self.clear},  # 清空按钮
            {text: '返回', color: '#00ffff', command: self.select_frame},  # 返回按钮
            {text: '计算', color: 'blue', command: self.calculate},  # 计算按钮
            {text: '确认', color: 'pink', command: self.affirm},  # 确认按钮
            ]
        for i in data:
            name = i.get(text)  # 文本
            bg = i.get(color)  # 颜色
            cmd = i.get(command)
            btn = Button(frame, text=name, bg=bg, width=width, command=cmd)
            btn.pack(side=LEFT, padx=(0, distance))
        frame.pack(pady=30)

    def set_frame(self, family, size, width, height, distance_x, distance_y, head, btn_space, btn_width, split_column,
                  difference):
        self.set_head(head, family, size)
        self.set_content(family, size, width, height, distance_x, distance_y, split_column, difference)
        self._button_frame(btn_space, btn_width)

    def select_frame(self):
        common.clear_child(self.win)  # 清空组件
        self.clear()  # 清空数据
        select.SelectFrame(self.win)  # 返回查询页面
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
            messagebox.showerror('错误信息', '储存信息失败!\n异常:{}'.format(msg))
        pass

    def calculate(self):
        data = list(map(lambda x: x.get(), self.fields))  # 获取填入的数据
        print('界面的数据是:{}'.format(data))
        self.fields[6].config(state='normal')
        try:
            self.fields[6].delete(0, END)
            data[6] = int(int(data[4]) * W + int(data[5]) * (1 - W))
            self.fields[6].insert(0, data[6])
        except:
            pass
        self.fields[6].config(state='readonly')

    def clear(self):
        # 清空所有组件(下拉框+输入框)
        for field in self.fields:
            if isinstance(field, ttk.Combobox):
                field.set('')  # 下拉框清空
            else:
                field.delete(0, END)  # entry清空输入内容


if __name__ == '__main__':
    w = Tk()
    MyFrame(w)
    w.mainloop()
