# -*- encoding=utf-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import common
import login
import select

NAME = 'name'
TYPE = 'type'
DATA = 'data'
ENTRY = 'entry'
COMBOBOX = 'combobox'
OPTIONS = 'options'
MUST = 'must'


class EditFrame:
    @staticmethod
    def custom_content():  # 显示的字段
        content = [
            {NAME: '姓名', TYPE: ENTRY, MUST: True, DATA: {}, },
            {NAME: '性别', TYPE: COMBOBOX, MUST: False, DATA: {OPTIONS: ['男', '女']}},
            {NAME: '年龄', TYPE: ENTRY, MUST: True, DATA: {}},
            {NAME: '班级', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '备注', TYPE: ENTRY, MUST: False, DATA: {}},
            ]
        return content

    @staticmethod
    def save_add_data(data):  # 添加数据时,保存数据
        success = True
        msg = ''
        return success, msg

    @staticmethod
    def save_update_data(data):  # 修改数据时,保存数据
        success = True
        msg = ''
        return success, msg

    def save(self, data):
        # 重构保存和修改信息
        # ['盖聂', '男', '20', '计算15-9班', '学习委员']
        if self.update_data:  # 如果是修改页面
            success, msg = self.save_update_data(data)  # 修改数据时,保存数据
        else:  # 如果是添加页面
            success, msg = self.save_add_data(data)  # 添加数据时,保存数据
        return success, msg

    def when_update_set_readonly(self):  # 修改页面设置一些字段只读
        self.fields[0].config(state='readonly')

    def init_for_update(self):  # 修改页面的一些操作
        if self.update_data:
            self.win.title('修改信息')  # 修改标题
            self.head_label.config(text='修改信息')  # 修改显示头信息
            self.when_update_set_readonly()  # 修改页面设置一些字段只读

    def __init__(self, win,
                 win_width=500,  # 窗口宽度
                 win_height=500,  # 窗口高度
                 win_title='数据编辑',  # 窗口标题
                 head='添加信息',  # 显示头信息
                 frame_top_distance=40,  # 显示头信息frame与窗口上边界的的Y轴距离
                 frame_middle_distance=40,  # 输入框frame与显示头信息frame的Y轴距离
                 frame_below_distance=40,  # 按钮frame与输入框frame的Y轴距离
                 font_family='宋体',  # 字体
                 font_size=20,  # 字体大小
                 entry_width=12,  # 输入框宽度
                 entry_height=5,  # 下拉显示的条目数量
                 entry_space_x=20,  # label和entry在x轴的间距
                 entry_space_y=10,  # 上一行和下一行y轴的间距
                 combobox_indent=1,  # 输入框和下拉框长度之差
                 label_bg='#80ffff',  # label背景
                 label_width=10,  # label宽度
                 label_relief='g',  # label边框样式
                 btn_space=10,  # 按钮在x轴间距
                 btn_width=10,  # 按钮的宽度
                 split_column=1,  # 1表示显示在一列,其他大于1的数字表示每列显示几个元素
                 update_data=[]  # 修改传入的数据,调试时设置None用来模拟修改数据
                 ):
        self.win = win  # 窗口
        self.head_label = None  # 显示头信息
        self.fields = []  # 所有组件(下拉框+输入框)
        if update_data is None:  # 调试时用来模拟修改数据
            self.update_data = ['盖聂', '男', '20', '计算15-9班', '学习委员']  # 模拟修改数据
        else:
            self.update_data = update_data  # 接收修改数据
        win.title(win_title)  # 设置标题
        common.middle_windows(win, win_width, win_height)  # 设置窗口居中
        self.set_frame(head, frame_top_distance, frame_middle_distance, frame_below_distance,
                       font_family, font_size, entry_width, entry_height, entry_space_x,
                       entry_space_y, combobox_indent, label_bg, label_width, label_relief,
                       btn_space, btn_width, split_column,
                       )  # 布局整个页面
        self.clear_btn_event()  # 清空所有组件(下拉框+输入框)
        self.set_update_data()  # 设置修改的数据
        self.all_do()  # 修改页面和添加页面,共同需要完成的操作
        self.init_for_update()  # 当做为修改页面时的一些操作

    def all_do(self):  # 修改页面和添加页面,共同需要完成的操作
        self.fields[0].focus()  # 第一个聚焦

    def set_head(self, head, family, size, top_distance):  # 设置最上面的文字
        frame = Frame(self.win)  # Frame组件
        self.head_label = Label(frame, text=head, font=(family, size))  # 显示头label组件
        self.head_label.pack()  # 放置显示的头label组件
        frame.pack(pady=(top_distance, 0))  # 放置Frame组件

    def must(self):  # 获取必填字段
        content = self.custom_content()  # 显示的字段
        required_fields = []  # 必填字段
        for index, one in enumerate(content):
            name = one.get(NAME)  # 名称
            must = one.get(MUST)  # 必填
            if must:  # 是必填则记录下标和名称
                required_fields.append((index, name))  # 以元组的放置保存必填项e.g[(0,'姓名'),(2,'年龄')]
        return required_fields

    def set_content(self, family, size, label_width, height, distance_x, distance_y, split_column,
                    difference, bg, input_width, relief, frame_y_distance):
        frame = Frame(self.win)  # Frame组件
        frame.pack(pady=(frame_y_distance, 0))  # 放置Frame组件
        content = self.custom_content()  # 显示的字段
        labels = []  # 所有的label
        for one in content:  # 遍历显示的字段设置label
            text = one.get(NAME)  # 名称
            label = Label(master=frame,  # 父容器
                          text=text,  # 文本
                          font=(family, size),  # 字体
                          bg=bg,  # 背景
                          width=label_width,  # 宽度
                          relief=relief  # 边框样式
                          )
            labels.append(label)  # 保存所以label用于放置
        fields = []  # 所有的字段(下拉框+输入框)
        for one in content:  # 遍历显示的字段设置输入框与下拉框
            name = one.get(NAME)  # 名称
            typeof = one.get(TYPE)  # 类型
            if typeof == ENTRY:  # 输入框
                widget = Entry(frame, text=name, font=(family, size), width=input_width)  # 输入框
            elif typeof == COMBOBOX:  # 下拉框
                options = one.get(DATA, {}).get(OPTIONS)  # 获取下拉框选项
                widget = ttk.Combobox(
                        master=frame,  # 父容器
                        height=height,  # 高度,下拉显示的条目数量
                        width=input_width - difference,  # 宽度
                        state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
                        cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
                        font=(family, size),  # 字体
                        values=options,  # 设置下拉框的选项
                        )
            else:
                widget = None
                print('错误:组件类型有误')
            if one == content[-1]:
                widget.bind(login.RETURN, lambda x: self.ok_btn_event())  # 最后一个组件绑定确认按钮事件
            fields.append(widget)  # 保存所有组件(下拉框+输入框)用于布局
        self.fields = fields  # 所有组件(下拉框+输入框)
        if split_column == 1:  # 只显示一列
            for i, label in enumerate(labels):  # 遍历所有的label
                label.grid(row=i, column=0, padx=(0, distance_x), sticky='e')  # 布局labels
            for i, field in enumerate(fields):  # 遍历输入框和下拉框
                field.grid(row=i, column=1, pady=distance_y)  # 布局所有组件(下拉框+输入框)
        else:  # 显示多列,每列显示split_column个元素
            column = 0
            labels_group = list(self.group(labels, split_column))  # 对labels分组
            fields_group = list(self.group(fields, split_column))  # 对所有组件(下拉框+输入框)分组
            for i, label in enumerate(labels_group):  # 遍历分组字段
                row = 0
                for index in range(len(label)):  # 遍历所有的label
                    label[index].grid(row=row, column=column, padx=distance_x,
                                      sticky='e')  # 布局labels
                    fields_group[i][index].grid(row=row, column=column + 1,
                                                pady=distance_y)  # 布局所有组件(下拉框+输入框)
                    row += 1
                column += 2
        self.bind_enter_focus()  # 绑定回车聚焦事件,不是最后一个组件时按下回车键自动聚焦下一个组件

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

    def _button_frame(self, distance, width, distance_y):
        frame = Frame(self.win)  # Frame组件
        text = 'text'
        color = 'color'
        command = 'command'
        data = [
            {text: '清空', color: 'yellow', command: self.clear_btn_event},  # 清空按钮
            {text: '返回', color: '#00ffff', command: self.return_btn_event},  # 返回按钮
            {text: '确认', color: 'pink', command: self.ok_btn_event},  # 确认按钮
            ]
        for one in data:
            name = one.get(text)  # 文本
            bg = one.get(color)  # 颜色
            cmd = one.get(command)  # 命令
            btn = Button(frame, text=name, bg=bg, width=width, command=cmd)  # 创建按钮
            btn.pack(side=LEFT, padx=(0, distance))  # 放置按钮
        frame.pack(pady=(distance_y, 0))  # 放置Frame

    def set_frame(self, head, frame_top_distance, frame_middle_distance, frame_below_distance,
                  font_family, font_size, entry_width, entry_height, entry_space_x, entry_space_y,
                  combobox_indent, label_bg, label_width, label_relief, btn_space, btn_width,
                  split_column, ):  # 布局整个页面
        self.set_head(head, font_family, font_size, frame_top_distance)  # 布局显示头
        self.set_content(font_family, font_size, label_width, entry_height, entry_space_x,
                         entry_space_y, split_column, combobox_indent, label_bg, entry_width,
                         label_relief, frame_middle_distance)  # 布局输入框和下拉框
        self._button_frame(btn_space, btn_width, frame_below_distance)  # 布局按钮

    def return_btn_event(self):  # 返回按钮事件
        common.clear_child(self.win)  # 清空组件
        self.clear_btn_event()  # 清空数据
        select.SelectFrame(self.win)  # 返回查询页面

    def ok_btn_event(self):  # 确认按钮事件
        data = list(map(lambda x: x.get(), self.fields))  # 获取填入的数据
        must = self.must()  # 必填项
        for i in must:  # 判断必填项
            if data[i[0]].strip() == '':  # 必填项为空
                messagebox.showinfo('提示信息', '[{}]是必填项'.format(i[1]))
                return False

        success, msg = self.save(data)  # 保存数据
        if success:
            self.return_btn_event()  # 返回按钮事件
        else:
            messagebox.showerror('错误信息', '储存信息失败!\n原因:{}'.format(msg))

    def clear_btn_event(self):  # 清空按钮事件
        # 清空所有组件(下拉框+输入框)
        for field in self.fields:
            if isinstance(field, ttk.Combobox):  # 如果是下拉框
                field.set('')  # 下拉框清空
            else:  # 如果是输入框
                field.delete(0, END)  # entry清空输入内容

    def bind_enter_focus(self):  # 绑定Enter聚焦事件
        for index, widget in enumerate(self.fields):
            if index + 1 < len(self.fields):  # 不是最后一个组件时按下回车键自动聚焦下一个组件
                widget.bind(login.RETURN, lambda x, y=index + 1: self.fields[y].focus())


if __name__ == '__main__':
    w = Tk()
    EditFrame(w)
    w.mainloop()
