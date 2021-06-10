# -*- encoding=utf-8 -*-
import datetime
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename

from PIL import Image
from PIL import ImageTk

from common import *
import cut_pictures
from data.classcode import class_code
from data.culture import culture
from data.nation import nation
from data.politicsstatus import politics_status
import login
import student_select

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
        # 重构显示的字段
        content = [
            {NAME: '学号', TYPE: ENTRY, MUST: True, DATA: {}, },
            {NAME: '姓名', TYPE: ENTRY, MUST: True, DATA: {}},
            {NAME: '性别', TYPE: COMBOBOX, MUST: False, DATA: {OPTIONS: ['男', '女']}},
            {NAME: '班级代码', TYPE: COMBOBOX, MUST: True, DATA: {OPTIONS: list(class_code.keys())}},
            {NAME: '身份证号码', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '出生年月日', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '民族', TYPE: COMBOBOX, MUST: False, DATA: {OPTIONS: nation}},
            {NAME: '籍贯', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '政治面貌', TYPE: COMBOBOX, MUST: False, DATA: {OPTIONS: politics_status}},
            {NAME: '文化程度', TYPE: COMBOBOX, MUST: False, DATA: {OPTIONS: culture}},
            {NAME: '家庭地址', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '邮编', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '家庭电话', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '身高', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '体重', TYPE: ENTRY, MUST: False, DATA: {}},
            {NAME: '血型', TYPE: COMBOBOX, MUST: False, DATA: {OPTIONS: ['A', 'B', 'AB', 'O']}},
            ]
        return content

    @staticmethod
    def check_input(data):  # 判断输入是否合法
        success = True
        msg = ''
        try:
            int(data[0])
        except:
            success = False
            msg = '学号需要是整型,请检查'
        if data[5]:  # 如果输入不是空串
            try:
                datetime.datetime.strptime(data[5], '%Y-%m-%d')
            except:
                success = False
                msg = '出生年月应该是年-月-日[1997-5-16],请检查'
        return success, msg

    @staticmethod
    def exist_student_id(student_id):  # 是否存在学号
        success = True
        msg = ''
        db_data, msg = mysqltool.select(mysqltool.conn_db, 'studentrecord', ['id'],
                                        {'id': student_id})
        if db_data:
            success = False
            msg = '学号已经存在!'
        return success, msg

    def save_student_image(self, data):  # 保存学生照片
        if self.binary_image_path:
            if os.path.isfile(self.binary_image_path):
                with open(self.binary_image_path, 'rb') as f:
                    content = f.read()
                insert_data = dict(id=data[0], image=content,
                                   updatetime=mytool.now('%Y-%m-%d %H:%M:%S'))
                success, msg = mysqltool.insert(mysqltool.conn_db, 'studentphoto', insert_data)
            else:
                success = False
                msg = f'未找到二进制图片文件"添加学生照片失败":{self.binary_image_path}'
        else:
            success = False
            msg = '请选择照片"添加学生照片"'
        return success, msg

    @staticmethod
    def check_birthday(data):  # 如果输入了出生年月需要符合标准格式
        if data[5]:  # 如果输入了出生年月
            data[5] = datetime.datetime.strptime(data[5], '%Y-%m-%d')
        else:
            data[5] = None  # 如果未输入了出生年月
        return data

    def add_student_info(self, data):  # 添加信息
        success, msg = self.exist_student_id(data[0])  # 是否存在学号
        if not success:
            return success, msg
        insert_data = dict(id=data[0],
                           name=data[1],
                           sex=data[2],
                           classcode=data[3],
                           idcard=data[4],
                           birthday=data[5],
                           ethnic=data[6],
                           native=data[7],
                           politicsstatus=data[8],
                           culturelevel=data[9],
                           address=data[10],
                           postcode=data[11],
                           hometelephone=data[12],
                           height=data[13],
                           weight=data[14],
                           bloodtype=data[15],
                           )
        success, msg = self.save_student_image(data)  # 先保存图片信息
        if not success:
            return success, msg
        success, msg = mysqltool.insert(mysqltool.conn_db, 'studentrecord', insert_data)

        return success, msg

    def update_student_image(self, data):
        if self.binary_image_path:
            if os.path.isfile(self.binary_image_path):
                with open(self.binary_image_path, 'rb') as f:
                    content = f.read()
                update_data = dict(id=data[0], image=content,
                                   updatetime=mytool.now('%Y-%m-%d %H:%M:%S'))
                update_conditions = dict(id=data[0])
                success, msg = mysqltool.update(mysqltool.conn_db, 'studentphoto', update_data,
                                                update_conditions)
            else:
                success = False
                msg = f'未找到二进制图片文件"修改学生照片失败":{self.binary_image_path}'
        else:
            success = False
            msg = '请选择照片"修改学生照片"'
        return success, msg
        pass

    def update_student_info(self, data):
        update_data = dict(id=data[0],
                           name=data[1],
                           sex=data[2],
                           classcode=data[3],
                           idcard=data[4],
                           birthday=data[5],
                           ethnic=data[6],
                           native=data[7],
                           politicsstatus=data[8],
                           culturelevel=data[9],
                           address=data[10],
                           postcode=data[11],
                           hometelephone=data[12],
                           height=data[13],
                           weight=data[14],
                           bloodtype=data[15],
                           )
        success, msg = self.update_student_image(data)  # 先保存图片信息
        if not success:
            return success, msg

        update_conditions = dict(id=data[0])
        success, msg = mysqltool.update(mysqltool.conn_db, 'studentrecord', update_data,
                                        update_conditions)
        return success, msg

    def save(self, data):
        # 重构保存和修改信息
        success, msg = self.check_input(data)  # 判断输入是否合法
        if not success:
            return success, msg
        data = self.check_birthday(data)  # 如果输入了出生年月需要符合标准格式
        if self.update_data:  # 是修改
            success, msg = self.update_student_info(data)
        else:  # 是添加
            success, msg = self.add_student_info(data)
        return success, msg
        pass

    def left_mouse_down(self, event):  # 按下鼠标左键选择图片
        path = askopenfilename()
        if path:
            dst = f'tmp/image_{mytool.now()}.png'
            cut_pictures.resize_image_size(path, dst, 320, 240)  # 重置图片大小
            self.binary_image_path = f'tmp/binary_image_{mytool.now()}'
            cut_pictures.save_binary_image(dst, self.binary_image_path)  # 保存二进制图片文件
            global STUDENT_EDIT_IMG
            try:
                STUDENT_EDIT_IMG = ImageTk.PhotoImage(Image.open(dst))
                self.image_label.config(image=STUDENT_EDIT_IMG)
            except:
                messagebox.showerror('提示信息', '照片不符合标准')

    def when_update_show_image(self):
        if self.update_data:
            select_conditions = dict(id=self.update_data[0])
            db_data, msg = mysqltool.select(mysqltool.conn_db, 'studentphoto', ['image'],
                                            select_conditions)
            binary_data = db_data[0].get('image')
            if binary_data:
                self.binary_image_path = f'tmp/binary_image_{mytool.now()}'
                mytool.create_folder(os.path.dirname(self.binary_image_path))
                with open(self.binary_image_path, 'wb') as f:
                    f.write(binary_data)
                global STUDENT_EDIT_IMG
                STUDENT_EDIT_IMG = cut_pictures.read_binary_image(self.binary_image_path)
                self.image_label.config(image=STUDENT_EDIT_IMG)
            else:
                print('查询不到二进制图片信息')

    def __init__(self, win,
                 win_width=1000,  # 窗口宽度
                 win_height=600,  # 窗口高度
                 win_title='学生档案添加',  # 窗口标题
                 head='学生档案添加',  # 显示头信息
                 font_family='宋体',  # 字体
                 font_size=12,  # 字体大小
                 entry_width=20,  # 输入框宽度
                 entry_height=10,  # 下拉显示的条目数量
                 entry_space_x=5,  # label和entry在x轴的间距
                 entry_space_y=16,  # 上一行和下一行y轴的间距
                 combobox_indent=1,  # 输入框和下拉框长度之差
                 btn_space=10,  # 按钮在x轴间距
                 btn_width=10,  # 按钮的宽度
                 split_column=7,  # 1表示显示在一列,其他大于1的数字表示每列显示几个元素
                 update_data=[]  # 修改传入的数据
                 ):
        self.binary_image_path = None  # 图片路径
        self.head_label = None  # 显示头label
        self.image_label = None  # 显示图片label
        self.win = win  # 窗口
        self.fields = []  # 所有组件(下拉框+输入框)
        if update_data is None:
            self.update_data = ['盖聂', '男', '20', '计算15-9班', '学习委员']  # 模拟修改数据
        else:
            self.update_data = update_data
        self.win.title(win_title)  # 设置标题
        set_size_center(self.win, win_width, win_height)  # 设置位置和大小
        self.set_frame(font_family, font_size, entry_width, entry_height, entry_space_x,
                       entry_space_y, head, btn_space,
                       btn_width, split_column, combobox_indent)  # 布局
        self.clear()
        self.set_update_data()  # 设置修改的数据
        self.when_update()  # 当是修改数据时,设置学号只读
        self.when_update_show_image()  # 当是修改数据时,设置图片显示
        self.win.protocol("WM_DELETE_WINDOW", lambda: on_closing(self.win))

    def set_head(self, head, family, size):
        frame = Frame(self.win)
        self.head_label = Label(frame, text=head, font=(family, size))
        self.head_label.pack()  # 设置显示的头
        frame.pack(pady=20)

    def when_update(self):
        if self.update_data:
            self.win.title('学生档案修改')
            self.head_label.config(text='学生档案修改')
            self.fields[0].config(state='readonly')

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
                label.grid(row=i, column=0, padx=(distance_x, distance_x), sticky='e')  # 布局labels
            for i, field in enumerate(fields):
                field.grid(row=i, column=1, pady=distance_y)  # 布局所有组件(下拉框+输入框)
        else:  # 显示多列,每列显示split_column个元素
            column = 0
            labels_group = list(self.group(labels, split_column))  # 对labels分组
            fields_group = list(self.group(fields, split_column))  # 对所有组件(下拉框+输入框)分组
            for i, label in enumerate(labels_group):
                row = 0
                for index in range(len(label)):

                    label[index].grid(row=row, column=column, padx=(distance_x, distance_x),
                                      sticky='e')  # 布局labels
                    fields_group[i][index].grid(row=row, column=column + 1, padx=(0, distance_x),
                                                pady=distance_y)  # 布局所有组件(下拉框+输入框)
                    row += 1
                column += 2
        frame = Frame(self.win, width=320, height=240, relief='g', bd=1)
        frame.propagate(False)

        self.image_label = Label(frame, width=320, bg='#008080', height=240, text='点击选择照片')
        self.image_label.bind('<Button-1>', self.left_mouse_down)  # 鼠标左键按下
        self.image_label.pack(fill=BOTH, expand=True)
        frame.place(x=650, y=180)
        self.fields[0].focus()
        self.bind_next()

    def bind_next(self):  # 绑定Enter聚焦事件
        for index, widget in enumerate(self.fields):
            if index + 1 < len(self.fields):
                widget.bind(login.RETURN, lambda x, y=index + 1: self.fields[y].focus())

    @staticmethod
    def group(list_data, number):
        # 分组列表数据
        for i in range(0, len(list_data), number):
            yield list_data[i:i + number]  # 迭代器

    def set_update_data(self):
        if self.update_data:  # 如果是修改传入的数据就填入到输入框和下拉框中
            self.clear()  # 清除下拉框和输入框
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
            {text: '返回', color: '#00ffff', command: self.return_main_page},  # 返回按钮
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

    def return_main_page(self):  # 返回
        clear_child(self.win)  # 清空组件
        self.clear()  # 清空数据
        student_select.SelectFrame(self.win)  # 返回查询页面

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
            self.return_main_page()
        else:
            messagebox.showerror('错误信息', '储存信息失败!\n异常:{}'.format(msg))
        pass

    def clear(self):
        # 清空所有组件(下拉框+输入框)
        for field in self.fields:
            if isinstance(field, ttk.Combobox):
                field.set('')  # 下拉框清空
            else:
                field.delete(0, END)  # entry清空输入内容


STUDENT_EDIT_IMG = None
if __name__ == '__main__':
    w = Tk()
    MyFrame(w)
    w.mainloop()
