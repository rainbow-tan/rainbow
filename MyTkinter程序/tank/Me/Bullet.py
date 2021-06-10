# -*- encoding=utf-8 -*-
import time
from tkinter import *
from tkinter import messagebox

from Base import Base

bullet_up = None  # 图片保持持续的全局使用
bullet_down = None  # 图片保持持续的全局使用
bullet_left = None  # 图片保持持续的全局使用
bullet_right = None  # 图片保持持续的全局使用
bullets = []


class Bullet(Base):

    def __init__(self, canvas, x=6, y=6, step=12, direction='right', tags='bullet'):
        super().__init__(canvas, x, y)
        self.tags = tags
        self.direction = direction  # 方向
        global bullet_up  # 图片保持持续的全局使用
        global bullet_down  # 图片保持持续的全局使用
        global bullet_left  # 图片保持持续的全局使用
        global bullet_right  # 图片保持持续的全局使用
        bullet_up = PhotoImage(file='image/bullet/bullet_up.png')  # 加载图
        bullet_down = PhotoImage(file='image/bullet/bullet_down.png')  # 加载图
        bullet_left = PhotoImage(file='image/bullet/bullet_left.png')  # 加载图
        bullet_right = PhotoImage(file='image/bullet/bullet_right.png')  # 加载图

        self.canvas = canvas
        self.x = x
        self.y = y
        self.R = 12
        self.r = self.R / 2

        self.step = step
        self.dx = self.step
        self.dy = self.step
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.draw()

    def hit(self, tags, r=12):
        all_tags = list(self.canvas.find_withtag(tags))
        for i in all_tags:
            ret = self.canvas.coords(i)
            x = ret[0]  # 障碍物的横坐标
            y = ret[1]  # 障碍物的纵坐标
            safe_distance = self.r + r
            x_distance = abs(x - self.x)  # x轴距离
            y_distance = abs(y - self.y)  # y轴距离
            if x_distance < safe_distance and y_distance < safe_distance:
                # 小于安全距离就撞在一起
                self.stop = True  # 停止
                self.canvas.delete(self.id)  # 删除自己
                return i  # 返回被撞的id

    def draw(self):
        global bullets
        image = eval('bullet_' + self.direction)
        bullets.append(image)  # 保持持续的全局使用
        self.id = self.canvas.create_image(self.x, self.y, image=image, tags=self.tags)
        self.canvas.addtag_withtag('bullet', self.tags)

    def move(self):
        self.canvas.coords(self.id, self.x, self.y)

    def next(self):
        pass
        if self.direction == 'up':  # 上
            self.dx = 0
            self.dy = -self.step
            self.y += self.dy

        if self.direction == 'down':  # 下
            self.dx = 0
            self.dy = self.step
            self.y += self.dy
        if self.direction == 'left':  # 左
            self.dx = -self.step
            self.dy = 0
            self.x += self.dx
        if self.direction == 'right':  # 右
            self.dx = self.step
            self.dy = 0
            self.x += self.dx
        if self.y > self.canvas_height or self.y < 0 or self.x < 0 or self.x > self.canvas_width:
            # 碰到边界该销毁自己
            self.canvas.delete(self.id)
            self.stop = True
        self.hit('brick')  # 碰撞brick监测
        self.hit('iron')  # 碰撞 iron 监测
        self.hit('enemy')  # 碰撞 enemy 监测
        hit_hero = self.hit('hero')  # 碰撞 hero 监测
        if hit_hero:
            if self.tags == 'enemy_bullet':  # 被敌人的子弹撞了英雄
                messagebox.showinfo('你已经', '你已经阵亡了，是否重来一次？')
                self.reset()  # 重置画布
        self.move()

    def reset(self):
        # 重置画布
        all = list(self.canvas.find_withtag('hero')) + list(
                self.canvas.find_withtag('enemy')) + list(
                self.canvas.find_withtag('bullet')) + list(
                self.canvas.find_withtag('hero_bullet')) + list(
                self.canvas.find_withtag('enemy_bullet'))
        for i in all:
            self.canvas.delete(i)  # 删除所有的东西，只保存背景

    def run(self):
        while not self.stop:
            self.next()
            time.sleep(0.5)


if __name__ == '__main__':
    win = Tk()
    win.geometry('624x624+500+0')

    my_canvas = Canvas(win, )
    my_canvas.pack(fill='both', expand=True)
    win.update()

    bullet = Bullet(my_canvas, 48, 48, 12, 'down')
    bullet.start()

    Brick_Image = PhotoImage(file='image/scene/brick.png')
    my_canvas.create_image(48 + 12, 84 + 48 * 5, image=Brick_Image, tags='brick')

    win.mainloop()
