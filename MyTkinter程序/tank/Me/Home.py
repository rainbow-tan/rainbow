# -*- encoding=utf-8 -*-
from tkinter import *

from Base import Base

Home_Image = None


class Home(Base):

    def __init__(self, canvas, x=0, y=0):
        super().__init__(canvas, x=x, y=y)
        global Home_Image
        Home_Image = PhotoImage(file='image/home/home1.png')
        self.draw()

    def draw(self):
        x = 48 * 6 + 24
        y = 600
        self.canvas.create_image(x, y, image=Home_Image, tags='home')


if __name__ == '__main__':
    win = Tk()
    canvas = Canvas(win, width=48 * 13, height=48 * 13, bg='white')
    canvas.pack(padx=0, fill='both', expand=True)
    win.update()
    home = Home(canvas, 0, 0, )
    win.mainloop()
