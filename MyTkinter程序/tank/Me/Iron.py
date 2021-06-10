# -*- encoding=utf-8 -*-
from tkinter import *

from Base import Base

Iron_Image = None


class Iron(Base):

    def __init__(self, canvas, x=0, y=0):
        super().__init__(canvas, x=x, y=y)
        global Iron_Image
        Iron_Image = PhotoImage(file='image/scene/iron.png')
        self.draw()

    def draw(self):
        # 找到坐标放置Iron图片
        for x in range(12, 12 + 24 * 2, 24):
            y = 624 - 48 - 7 * 24 - 48 - 24 + 12
            self.canvas.create_image(x, y, image=Iron_Image, tags='iron')
        for x in range(12 + 48 * 12, 12 + 24 * 2 + 48 * 12, 24):
            y = 624 - 48 - 7 * 24 - 48 - 24 + 12
            self.canvas.create_image(x, y, image=Iron_Image, tags='iron')
        for x in range(48 * 6 + 12, 48 * 6 + 24 * 2, 24):
            for y in range(48 * 3 + 12, 48 * 3 + 12 + 24 * 2, 24):
                self.canvas.create_image(x, y, image=Iron_Image, tags='iron')
        for x in range(48 * 5 + 36, 48 * 5 + 36 + 24, 24):
            for y in range(624 - 24 * 3 + 12, 624 - 24 * 3 + 12 + 24 * 3, 24):
                self.canvas.create_image(x, y, image=Iron_Image, tags='iron')
        for x in range(48 * 5 + 36 + 48 + 24, 48 * 5 + 36 + 24 + 48 + 24, 24):
            for y in range(624 - 24 * 3 + 12, 624 - 24 * 3 + 12 + 24 * 3, 24):
                self.canvas.create_image(x, y, image=Iron_Image, tags='iron')
        for x in range(48 * 6 + 12, 48 * 6 + 12 + 24 * 2, 24):
            y = 624 - 24 * 3 + 12
            self.canvas.create_image(x, y, image=Iron_Image, tags='iron')


if __name__ == '__main__':
    win = Tk()
    win.geometry('624x624+500+10')
    my_canvas = Canvas(win, bg='white')
    my_canvas.pack(padx=0, fill='both', expand=True)
    win.update()
    iron = Iron(my_canvas, 0, 0)
    win.mainloop()
