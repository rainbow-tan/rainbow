# -*- encoding=utf-8 -*-
from tkinter import Canvas
from tkinter import N
from tkinter import Tk
from tkinter import W

from PIL import ImageTk

from Base import Base

image = None


class Tree(Base):

    def __init__(self, canvas, x=100, y=250, color='blue', path=None):
        super().__init__(canvas, x=x, y=y)
        self.path = path
        self.draw()

    def draw(self):
        global image
        image = ImageTk.PhotoImage(file=self.path)
        for x in range(0, self.canvas_width, image.width()):
            for y in range(0, self.canvas_height, image.height()):
                self.canvas.create_image(x, y, image=image, anchor=N + W, tags='tree')


if __name__ == '__main__':

    win = Tk()
    win.geometry('624x624+500+10')
    canvas = Canvas(win, width=48 * 13, height=48 * 13, bg='white')
    canvas.pack(padx=0, fill='both', expand=True)
    win.update()
    tree = Tree(canvas, 0, 0, path='image/scene/tree.png')
    win.mainloop()
