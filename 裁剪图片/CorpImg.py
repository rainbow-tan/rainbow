# -*- encoding=utf-8 -*-
import os
import time
import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

from PIL import Image
from PIL import ImageTk

from Wicket import Wicket

image = None
img = None


class Crop(Wicket):
    def __init__(self):
        super().__init__()
        self.left_mouse_down_x = 0
        self.left_mouse_down_y = 0
        self.left_mouse_up_x = 0
        self.left_mouse_up_y = 0
        self.sole_rectangle = None
        self.save_folder = os.path.abspath('images')
        self.provisional_folder = os.path.abspath('provisional')

        self.img_entry = None
        self.img_path = None
        self.img_canvas = None
        self.sole_img = None

        self.create_folder(self.save_folder)
        self.create_folder(self.provisional_folder)

    @staticmethod
    def create_folder(folder):
        if not os.path.exists(folder):
            try:
                os.makedirs(folder)
                print('创建文件夹成功:{}'.format(folder))
            except Exception as e:
                print('创建文件夹失败:{}'.format(e))

    @staticmethod
    def get_now():
        return time.strftime('%Y%m%d%H%M%S', time.localtime())

    def get_img_path(self):
        print('选择图片路径')
        if self.sole_rectangle is not None:
            self.img_canvas.delete(self.sole_rectangle)  # 删除前一个矩形
        img_path = askopenfilename()
        print('图片路径:{}'.format(img_path))
        self.img_path = os.path.abspath(img_path)
        self.img_entry.delete(0, tkinter.END)
        self.img_entry.insert(tkinter.END, img_path)
        self.load_img()

    def resize_img(self, image_path, max_width, max_height):
        image_path = os.path.abspath(image_path)
        ret_path = image_path
        suffix = os.path.splitext(image_path)[1]
        now = self.get_now()
        save_name = now + suffix
        save_path = os.path.join(self.provisional_folder, save_name)
        open_image = Image.open(image_path)
        img_width, img_height = open_image.size
        if img_width > max_width or img_height > max_height:
            flag = messagebox.askyesno('缩放', '图片尺寸过大,无法完整显示,是否自动缩放')
            if flag is True:
                re_img = open_image.resize((max_width, max_height), Image.ANTIALIAS)
                re_img.save(save_path)
                ret_path = save_path
                print('自动缩放图片完成,保存于:{}'.format(ret_path))
        return ret_path

    def load_img(self, ):
        print('加载图片')
        global image
        global img
        canvas_width = self.img_canvas.winfo_width()
        canvas_height = self.img_canvas.winfo_height()
        self.img_path = self.resize_img(self.img_path, canvas_width, canvas_height)
        image = Image.open(self.img_path)
        img = ImageTk.PhotoImage(image)

        if self.sole_img is not None:
            self.img_canvas.delete(self.sole_img)  # 删除前一张图片
            print('已清除前一张图片')

        self.sole_img = self.img_canvas.create_image(0, 0, anchor='nw', image=img)

    def choose_img(self):
        # 选择图片的Frame
        img_frame = tkinter.Frame(self.win)
        img_label = tkinter.Label(img_frame, text='图片路径')
        img_label.grid(row=0, column=0)
        self.img_entry = tkinter.Entry(img_frame, width=50, )
        self.img_entry.grid(row=0, column=1)
        img_button = tkinter.Button(img_frame, text='选择', command=self.get_img_path)
        img_button.grid(row=0, column=2)
        img_frame.pack()

        # 显示图片的画布
        canvas_frame = tkinter.Frame(self.win)
        screen_width, screen_height = self.get_screen()
        zoom = 8 / 9
        canvas_width = int(screen_width * zoom)
        canvas_height = int(screen_height * zoom)
        self.img_canvas = tkinter.Canvas(canvas_frame, width=canvas_width, height=canvas_height)
        self.img_canvas.bind('<Button-1>', self.left_mouse_down)  # 鼠标左键按下
        self.img_canvas.bind('<ButtonRelease-1>', self.left_mouse_up)  # 鼠标左键释放
        self.img_canvas.bind('<Button-3>', self.right_mouse_down)  # 鼠标右键按下
        self.img_canvas.bind('<ButtonRelease-3>', self.right_mouse_up)  # 鼠标右键释放
        self.img_canvas.bind('<B1-Motion>', self.moving_mouse)  # 鼠标左键按下并移动
        self.img_canvas.pack()
        canvas_frame.pack()

    def left_mouse_down(self, event):
        # print('鼠标左键按下')
        self.left_mouse_down_x = event.x
        self.left_mouse_down_y = event.y

    def left_mouse_up(self, event):
        # print('鼠标左键释放')
        self.left_mouse_up_x = event.x
        self.left_mouse_up_y = event.y
        self.corp_img(self.img_path, self.left_mouse_down_x,
                      self.left_mouse_down_y,
                      self.left_mouse_up_x, self.left_mouse_up_y)

    def moving_mouse(self, event):
        # print('鼠标左键按下并移动')
        moving_mouse_x = event.x
        moving_mouse_y = event.y
        if self.sole_rectangle is not None:
            self.img_canvas.delete(self.sole_rectangle)  # 删除前一个矩形
        self.sole_rectangle = self.img_canvas.create_rectangle(self.left_mouse_down_x,
                                                               self.left_mouse_down_y,
                                                               moving_mouse_x,
                                                               moving_mouse_y, outline='red')

    def right_mouse_down(self, event):
        # print('鼠标右键按下')
        pass

    def right_mouse_up(self, event):
        # print('鼠标右键释放')
        pass

    def corp_img(self, source_file, x_begin, y_begin, x_end, y_end):
        if x_begin < x_end:
            min_x = x_begin
            max_x = x_end
        else:
            min_x = x_end
            max_x = x_begin
        if y_begin < y_end:
            min_y = y_begin
            max_y = y_end
        else:
            min_y = y_end
            max_y = y_begin
        suffix = os.path.splitext(source_file)[1]
        now = self.get_now()
        save_name = now + suffix
        save_path = os.path.join(self.save_folder, save_name)
        if os.path.isfile(source_file):
            corp_image = Image.open(source_file)
            region = corp_image.crop((min_x, min_y, max_x, max_y))
            region.save(save_path)
            print('裁剪完成,保存于:{}'.format(save_path))
            messagebox.showinfo('提示', '裁剪完成,保存于:{}'.format(save_path))
        else:
            print('未找到文件:{}'.format(source_file))


if __name__ == '__main__':
    corp = Crop()
    corp.create_window()
    corp.set_window_title('裁剪图片')
    corp.set_window_size('max')
    corp.choose_img()
    corp.show_window()
