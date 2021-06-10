from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import common
import course_select
from data.course import course
from data.evaluationmode import evaluation_mode
from data.teachtype import teach_type
from data.units import units
import login
import mysqltool

NAME = 'name'
TYPE = 'type'
DATA = 'data'
ENTRY = 'entry'
COMBOBOX = 'combobox'
OPTIONS = 'options'
MUST = 'must'


class MyFrame:
    @staticmethod
    def custom_content():
        # 显示的字段
        content = [
            {NAME: '开课单位', TYPE: COMBOBOX, MUST: False, DATA: {OPTIONS: units}},
            {NAME: '课程', TYPE: COMBOBOX, MUST: False, DATA: {OPTIONS: list(course.keys())}},
            {NAME: '课程编号', TYPE: ENTRY, MUST: True, DATA: {}},
            {NAME: '课程性质', TYPE: COMBOBOX, MUST: False, DATA: {OPTIONS: ['选修', '必修']}},
            {NAME: '学分', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '课程简称', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '课程指南', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '评教类别', TYPE: COMBOBOX, MUST: False, DATA: {OPTIONS: evaluation_mode}},
            {NAME: '总学时', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '授课类型', TYPE: COMBOBOX, MUST: False, DATA: {OPTIONS: teach_type}},
            {NAME: '考核方式', TYPE: COMBOBOX, MUST: False, DATA: {OPTIONS: ['考试', '考查']}},
            {NAME: '英文名称', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '上机学时', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '实践学时', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '理论学时', TYPE: ENTRY, MUST: False, DATA: {}},
            ]
        return content

    @staticmethod
    def exist_course_code(code):  # 是否存在课程号
        flag = False
        db_data, msg = mysqltool.select(mysqltool.conn_db, 'course', ['id'], {'coursecode': code})
        if db_data:  # 存在
            flag = True
        return flag

    @staticmethod
    def check_time(data):  # 检查总学时是否=上机学时+实践学时+理论学时
        success = True
        msg = ''
        if data[8] and data[12] and data[13] and data[14]:
            if float(data[8]) != float(data[12]) + float(data[13]) + float(data[14]):
                success = False
                msg = '总学时!=上机学时+实践学时+理论学时,请检查'
        else:
            if not data[8] and not data[12] and not data[13] and not data[14]:
                pass
            else:
                success = False
                msg = '总学时,上机学时,实践学时,理论学时需要都填写或都不填写'

        return success, msg

    @staticmethod
    def is_number(number):  # 检查输入是否是数值型
        ok = True
        if number:
            try:
                float(number)
            except:
                ok = False
        return ok

    def check_input(self, data):  # 检查该输入数值的是否输入合格
        success = True
        msg = ''
        ret = self.is_number(data[4])
        if not ret:
            success = False
            msg = '学分不是数值型,请修正'
        ret = self.is_number(data[8])
        if not ret:
            success = False
            msg = '总学时不是数值型,请修正'
        ret = self.is_number(data[12])
        if not ret:
            success = False
            msg = '上机学时不是数值型,请修正'
        ret = self.is_number(data[13])
        if not ret:
            success = False
            msg = '实践学时不是数值型,请修正'
        ret = self.is_number(data[14])
        if not ret:
            success = False
            msg = '理论学时不是数值型,请修正'
        return success, msg

    @staticmethod
    def set_none(number):  # 如果该填数值型的地方填了空串就设置为None
        new = number
        if not number:
            new = None
        return new

    def set_all_none(self, data):  # 如果该填数值型的地方填了空串就设置为None
        data[4] = self.set_none(data[4])  # 如果该填数值型的地方填了空串就设置为None
        data[8] = self.set_none(data[8])  # 如果该填数值型的地方填了空串就设置为None
        data[12] = self.set_none(data[12])  # 如果该填数值型的地方填了空串就设置为None
        data[13] = self.set_none(data[13])  # 如果该填数值型的地方填了空串就设置为None
        data[14] = self.set_none(data[14])  # 如果该填数值型的地方填了空串就设置为None
        return data

    def add_course(self, data):  # 添加数据
        code = data[2]  # 课程号
        exist = self.exist_course_code(code)  # 是否存在课程号
        if exist:  # 存在课程号
            success = False
            msg = '课程号已经存在'
        else:  # 不存在课程号则插入
            insert_data = dict(courseunits=data[0],
                               coursename=data[1],
                               coursecode=data[2],
                               coursenature=data[3],
                               coursecredit=data[4],
                               courseabstract=data[5],
                               courseguide=data[6],
                               appraisalcategory=data[7],
                               classhour=data[8],
                               teachtype=data[9],
                               evaluationmode=data[10],
                               englishname=data[11],
                               computerhour=data[12],
                               practicehour=data[13],
                               theoryhout=data[14])
            success, msg = mysqltool.insert(mysqltool.conn_db, 'course', insert_data)
        return success, msg

    @staticmethod
    def update_course(data):  # 修改课程
        update_data = dict(courseunits=data[0],
                           coursename=data[1],
                           coursecode=data[2],
                           coursenature=data[3],
                           coursecredit=data[4],
                           courseabstract=data[5],
                           courseguide=data[6],
                           appraisalcategory=data[7],
                           classhour=data[8],
                           teachtype=data[9],
                           evaluationmode=data[10],
                           englishname=data[11],
                           computerhour=data[12],
                           practicehour=data[13],
                           theoryhout=data[14])
        update_conditions = dict(coursecode=data[2])
        success, msg = mysqltool.update(mysqltool.conn_db, 'course', update_data, update_conditions)
        return success, msg

    def when_update(self):
        if self.update_data:
            self.win.title('课程信息修改')  # 设置为修改信息
            self.head_label.config(text='课程信息修改')  # 设置为修改信息
            self.fields[1].config(state='readonly')  # 设置只读
            self.fields[2].config(state='readonly')  # 设置只读

    def save(self, data):
        success, msg = self.check_input(data)  # 检查该输入数值的是否输入合格
        if not success:
            return success, msg
        success, msg = self.check_time(data)  # 检查总学时是否=上机学时+实践学时+理论学时
        if not success:
            return success, msg
        data = self.set_all_none(data)  # 如果该填数值型的地方填了空串就设置为None
        if self.update_data:  # 是修改
            success, msg = self.update_course(data)  # 修改
        else:
            success, msg = self.add_course(data)  # 是新增
        return success, msg

    def __init__(self, win,
                 win_width=900,  # 窗口宽度
                 win_height=500,  # 窗口高度
                 win_title='课程信息添加',  # 窗口标题
                 head='课程信息添加',  # 显示头信息
                 font_family='宋体',  # 字体
                 font_size=12,  # 字体大小
                 entry_width=20,  # 输入框宽度
                 entry_height=10,  # 下拉显示的条目数量
                 entry_space_x=5,  # label和entry在x轴的间距
                 entry_space_y=16,  # 上一行和下一行y轴的间距
                 combobox_indent=1,  # 输入框和下拉框长度之差
                 btn_space=10,  # 按钮在x轴间距
                 btn_width=10,  # 按钮的宽度
                 split_column=5,  # 1表示显示在一列,其他大于1的数字表示每列显示几个元素,即几行
                 update_data=[]  # 修改传入的数据
                 ):
        self.win = win  # 窗口
        self.head_label = None  # 设置显示的头
        self.fields = []  # 所有组件(下拉框+输入框)
        if update_data is None:
            self.update_data = []  # 模拟修改数据
        else:
            self.update_data = update_data
        win.title(win_title)  # 设置标题
        common.set_size_center(win, win_width, win_height)  # 设置位置和大小
        self.set_frame(font_family, font_size, entry_width, entry_height, entry_space_x,
                       entry_space_y, head, btn_space,
                       btn_width, split_column, combobox_indent)  # 布局
        self.clear()
        self.set_update_data()  # 设置修改的数据
        self.when_update()
        self.win.protocol("WM_DELETE_WINDOW", lambda: common.on_closing(self.win))

    def set_head(self, head, family, size):
        frame = Frame(self.win)
        self.head_label = Label(frame, text=head, font=(family, size))
        self.head_label.pack()  # 设置显示的头
        frame.pack(pady=20)

    def must(self):
        # 获取必填字段
        content = self.custom_content()
        data = []
        for index, one in enumerate(content):
            name = one.get(NAME)  # 名称
            must = one.get(MUST, False)  # 必填
            if must:  # 是必填则记录下标和名称
                data.append((index, name))
        return data

    def set_content(self, family, size, width, height, distance_x, distance_y, split_column,
                    difference):
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
                bg='#80ffff',
                width=10,
                relief='g'
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
                    label[index].grid(row=row, column=column, padx=distance_x,
                                      sticky='e')  # 布局labels
                    fields_group[i][index].grid(row=row, column=column + 1,
                                                pady=distance_y)  # 布局所有组件(下拉框+输入框)
                    row += 1
                column += 2
        self.bind_next()  # 绑定Enter聚焦事件
        self.set_course_event()  # 设置课程名称选择事件

    def auto_insert(self, event):
        name = self.fields[1].get()  # 获取课程名称
        self.fields[2].delete(0, END)  # 删除课程编号
        self.fields[2].insert(END, course.get(name))  # 补充课程编号

    def set_course_event(self):  # 设置课程名称选择事件
        self.fields[1].bind('<<ComboboxSelected>>', self.auto_insert)

    @staticmethod
    def group(list_data, number):
        # 分组列表数据
        for i in range(0, len(list_data), number):
            yield list_data[i:i + number]  # 迭代器

    def set_update_data(self):
        if self.update_data:  # 如果是修改传入的数据就填入到输入框和下拉框中
            self.clear()  # 清空输入框和下拉框
            for index, field in enumerate(self.fields):
                if isinstance(field, ttk.Combobox):  # 下拉框
                    field.set(self.update_data[index])  # 设置下拉框的值
                elif isinstance(field, Entry):  # 输入框
                    field.insert(0, self.update_data[index])  # 设置输入框的值
                else:
                    print('错误:对象不存在')

    def _button_frame(self, distance, width):
        frame = Frame(self.win)
        text = 'text'
        color = 'color'
        command = 'command'
        data = [
            {text: '清空', color: 'yellow', command: self.clear},  # 清空按钮
            {text: '返回', color: '#00ffff', command: self.select_frame},  # 返回按钮
            {text: '确认', color: 'pink', command: self.affirm},  # 确认按钮
            ]
        for i in data:
            name = i.get(text)  # 文本
            bg = i.get(color)  # 颜色
            cmd = i.get(command)
            btn = Button(frame, text=name, bg=bg, width=width, command=cmd)
            btn.pack(side=LEFT, padx=(0, distance))
        frame.pack(pady=20)

    def set_frame(self, family, size, width, height, distance_x, distance_y, head, btn_space,
                  btn_width, split_column,
                  difference):
        self.set_head(head, family, size)
        self.set_content(family, size, width, height, distance_x, distance_y, split_column,
                         difference)
        self._button_frame(btn_space, btn_width)

    def select_frame(self):
        common.clear_child(self.win)  # 清空组件
        self.clear()  # 清空数据
        course_select.SelectFrame(self.win)  # 返回查询页面

    def logout(self):
        common.clear_child(self.win)  # 清空组件
        self.clear()  # 清空数据
        login.LoginFrame(self.win)  # 返回登录页面

    def affirm(self):
        # 确认按钮
        data = list(map(lambda x: x.get(), self.fields))  # 获取填入的数据
        must = self.must()  # 必填项
        for i in must:  # 判断必填项
            if data[i[0]].strip() == '':  # 必填项为空
                messagebox.showinfo('提示信息', '"{}"是必填项'.format(i[1]))
                return

        success, msg = self.save(data)  # 保存数据
        if success:
            self.select_frame()  # 跳到查询页面
        else:
            messagebox.showerror('错误信息', '储存信息失败!\n原因:{}'.format(msg))
        pass

    def clear(self):
        # 清空所有组件(下拉框+输入框)
        for field in self.fields:
            if isinstance(field, ttk.Combobox):
                field.set('')  # 下拉框清空
            else:
                field.delete(0, END)  # entry清空输入内容

    def bind_next(self):  # 绑定Enter聚焦事件
        for index, widget in enumerate(self.fields):
            if index + 1 < len(self.fields):  # 如果不是最后一个组件,则按下回车自动聚焦下一个组件
                widget.bind(login.RETURN, lambda x, y=index + 1: self.fields[y].focus())


if __name__ == '__main__':
    w = Tk()
    MyFrame(w)
    w.mainloop()
