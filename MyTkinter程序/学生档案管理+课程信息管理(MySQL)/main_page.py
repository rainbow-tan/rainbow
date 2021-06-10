from tkinter import *

from PIL import Image
from PIL import ImageTk

from common import *
import course_edit
import course_select
import login
import student_edit
import student_select


class MainPage:
    def view_students(self):  # 查看学生档案
        self.menu.destroy()  # 销毁菜单栏
        clear_child(self.win)  # 清空组件
        student_select.SelectFrame(self.win)

    def add_students(self):  # 添加学生档案
        self.menu.destroy()  # 销毁菜单栏
        clear_child(self.win)  # 清空组件
        student_edit.MyFrame(self.win)

    def view_course(self):  # 查看课程信息
        self.menu.destroy()  # 销毁菜单栏
        clear_child(self.win)  # 清空组件
        course_select.SelectFrame(self.win)

    def add_course(self):  # 添加课程信息
        self.menu.destroy()  # 销毁菜单栏
        clear_child(self.win)  # 清空组件
        course_edit.MyFrame(self.win)

    def exit_system(self):  # 退出系统
        on_closing(self.win)  # 关闭窗口

    def return_login_page(self):  # 返回登录
        set_exit_date()  # 设置退出时间
        self.menu.destroy()  # 销毁菜单栏
        clear_child(self.win)  # 清空组件
        login.LoginFrame(self.win)  # 返回登录页面

    def __init__(self, win):
        self.win = win
        set_size_center(self.win, 400, 500)
        font = ('', 16)
        self.menu = Menu(self.win, tearoff=0)  # 创建主菜单
        menu_main = Menu(self.menu, font=font, tearoff=0)  # 创建主菜单1
        menu_main.add_command(label='查看学生档案', command=self.view_students)  # 子菜单
        menu_main.add_command(label='添加学生档案', command=self.add_students)  # 子菜单

        menu_main2 = Menu(self.menu, font=font, tearoff=0)  # 创建主菜单2
        menu_main2.add_command(label='查看课程信息', command=self.view_course)  # 子菜单
        menu_main2.add_command(label='添加课程信息', command=self.add_course)  # 子菜单

        menu_main3 = Menu(self.menu, font=font, tearoff=0)  # 创建主菜单
        menu_main3.add_command(label='退出系统', command=self.exit_system)  # 子菜单
        menu_main3.add_command(label='返回登录', command=self.return_login_page)  # 子菜单

        self.menu.add_cascade(label='学生档案管理', menu=menu_main)  # 添加主菜单1到主菜单上
        self.menu.add_cascade(label='课程信息管理', menu=menu_main2)  # 添加主菜单2到主菜单上
        self.menu.add_cascade(label='离开', menu=menu_main3)  # 添加到主菜单上
        self.win.config(menu=self.menu)  # 设置主菜单到界面
        self.win.protocol("WM_DELETE_WINDOW", lambda: on_closing(self.win))
        global MAIN_PAGE_IMG
        MAIN_PAGE_IMG = ImageTk.PhotoImage(Image.open('data/bg.jpg'))
        Label(self.win, image=MAIN_PAGE_IMG).pack(fill=BOTH, expand=True)


MAIN_PAGE_IMG = None
if __name__ == '__main__':

    w = Tk()  # 窗口
    MainPage(w)
    w.mainloop()
