# -*- encoding=utf-8 -*-
import threading
import time
from tkinter import *


class Base(threading.Thread):
    """
    定义所有的基类
    """

    def __init__(self, canvas, x=100, y=250):
        """
        参数说明:
        画布  canvas
        坐标 [x,y]
        """
        # 把类 的对象转换为类 threading.Thread 的对象
        super().__init__()  # 重构run函数必须写 super().__init__()

        # 保存画板
        self.canvas = canvas

        # 保存中心点坐标
        self.x = x
        self.y = y

        # 获取画布的宽高
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

        self.dx = 0
        self.dy = 0
        self.id = None

        # 停止条件
        self.stop = False

    def draw(self):
        # 绘制自己
        pass

    def move(self):
        # 移动自己
        self.canvas.move(self.id, self.dx, self.dy)

    def next(self):
        # 重新定位 自己的XY 坐标
        pass

    def run(self):
        # 重构线程函数
        while not self.stop:
            self.next()
            time.sleep(0.05)


if __name__ == '__main__':
    win = Tk()
    win.geometry('600x400+100+100')

    my_canvas = Canvas(win, width=300, height=200, bg='white')
    my_canvas.pack(padx=0, fill='both', expand=True)
    win.update()
    base = Base(my_canvas)
    base.start()

    win.mainloop()
