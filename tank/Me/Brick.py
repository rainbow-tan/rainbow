# -*- encoding=utf-8 -*-
from tkinter import *

from Base import Base

Brick_Image = None  # 图片保持持续的全局使用


class Brick(Base):

    def __init__(self, canvas, x=0, y=0):
        super().__init__(canvas, x=x, y=y)
        global Brick_Image
        Brick_Image = PhotoImage(file='image/scene/brick.png')  # 加载图片
        self.draw()

    def draw(self):
        # 找到该放置的坐标
        for x in range(60, 564, 96):
            for y in range(60, 262, 24):
                if [x, y] in [[252, 228], [252, 252], [348, 228], [348, 252]]:
                    pass  # 去掉空的那些地方
                else:
                    self.canvas.create_image(x, y, image=Brick_Image, tags='brick')
        for x in range(60 + 24, 588, 96):
            for y in range(60, 262, 24):
                if [x, y] in [[276, 228], [372, 228], [276, 252], [372, 252]]:
                    pass  # 去掉空的那些地方
                else:
                    self.canvas.create_image(x, y, image=Brick_Image, tags='brick')
        for y in range(564, 396, -24):
            for x in range(60, 108, 24):
                self.canvas.create_image(x, y, image=Brick_Image, tags='brick')
        for y in range(564, 396, -24):
            for x in range(156, 204, 24):
                self.canvas.create_image(x, y, image=Brick_Image, tags='brick')
        for y in range(564, 396, -24):
            for x in range(444, 492, 24):
                self.canvas.create_image(x, y, image=Brick_Image, tags='brick')
        for y in range(564, 396, -24):
            for x in range(540, 588, 24):
                self.canvas.create_image(x, y, image=Brick_Image, tags='brick')
        for x in range(252, 300, 24):
            for y in range(372, 516, 24):
                self.canvas.create_image(x, y, image=Brick_Image, tags='brick')
        for x in range(348, 396, 24):
            for y in range(372, 516, 24):
                self.canvas.create_image(x, y, image=Brick_Image, tags='brick')
        for x in range(48 * 6 + 12, 48 * 6 + 12 + 24 * 2, 24):
            for y in range(624 - 48 - 7 * 24 - 12, 624 - 48 - 7 * 24 - 12 + 12 + 24, 24):
                self.canvas.create_image(x, y, image=Brick_Image, tags='brick')
        for y in range(624 - 48 - 11 * 24 + 12, 624 - 48 - 11 * 24 + 12 + 12 + 24, 24):
            for x in range(96 + 12, 96 + 12 + 4 * 24, 24):
                self.canvas.create_image(x, y, image=Brick_Image, tags='brick')
        for y in range(624 - 48 - 11 * 24 + 12, 624 - 48 - 11 * 24 + 12 + 12 + 24, 24):
            for x in range(96 + 12 + 48 * 7, 96 + 12 + 4 * 24 + 48 * 7, 24):
                self.canvas.create_image(x, y, image=Brick_Image, tags='brick')
        for y in range(264 + 12, 264 + 12 + 48, 24):
            for x in range(48 * 5 + 12, 48 * 5 + 12 + 24 * 2, 24):
                self.canvas.create_image(x, y, image=Brick_Image, tags='brick')
        for y in range(264 + 12, 264 + 12 + 48, 24):
            for x in range(48 * 5 + 12 + 48 * 2, 48 * 5 + 12 + 24 * 2 + 48 * 2, 24):
                self.canvas.create_image(x, y, image=Brick_Image, tags='brick')


if __name__ == '__main__':
    win = Tk()
    win.geometry('624x624+500+0')
    canvas = Canvas(win, bg='white')
    canvas.pack(padx=0, fill='both', expand=True)
    brick = Brick(canvas, 0, 0)
    win.mainloop()
