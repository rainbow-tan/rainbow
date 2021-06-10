import random
import time
from tkinter import *

from Base import Base
from Bullet import Bullet

Green_left_0 = None  # 图片保持持续的全局使用
Green_left_1 = None  # 图片保持持续的全局使用
Green_right_0 = None  # 图片保持持续的全局使用
Green_right_1 = None  # 图片保持持续的全局使用
Green_up_0 = None  # 图片保持持续的全局使用
Green_up_1 = None  # 图片保持持续的全局使用
Green_down_0 = None  # 图片保持持续的全局使用
Green_down_1 = None  # 图片保持持续的全局使用
Brick_Image = None  # 图片保持持续的全局使用
BOOM_IMAGE = None  # 图片保持持续的全局使用
enemys = []  # 图片保持持续的全局使用


class Enemy(Base):
    """
    定义坦克
    """

    def __init__(self, canvas, x=24, y=24, step=24, direction='right'):
        super().__init__(canvas, x, y)
        self.direction = direction  # 方向
        global Green_left_0  # 图片保持持续的全局使用
        global Green_left_1  # 图片保持持续的全局使用
        global Green_right_0  # 图片保持持续的全局使用
        global Green_right_1  # 图片保持持续的全局使用
        global Green_up_0  # 图片保持持续的全局使用
        global Green_up_1  # 图片保持持续的全局使用
        global Green_down_0  # 图片保持持续的全局使用
        global Green_down_1  # 图片保持持续的全局使用
        global Brick_Image  # 图片保持持续的全局使用
        global BOOM_IMAGE  # 图片保持持续的全局使用
        Green_left_0 = PhotoImage(file='image/enemy/Green_left_0.png')  # 图片保持持续的全局使用
        Green_left_1 = PhotoImage(file='image/enemy/Green_left_1.png')  # 图片保持持续的全局使用
        Green_right_0 = PhotoImage(file='image/enemy/Green_right_0.png')  # 图片保持持续的全局使用
        Green_right_1 = PhotoImage(file='image/enemy/Green_right_1.png')  # 图片保持持续的全局使用
        Green_up_0 = PhotoImage(file='image/enemy/Green_up_0.png')  # 图片保持持续的全局使用
        Green_up_1 = PhotoImage(file='image/enemy/Green_up_1.png')  # 图片保持持续的全局使用
        Green_down_0 = PhotoImage(file='image/enemy/Green_down_0.png')  # 图片保持持续的全局使用
        Green_down_1 = PhotoImage(file='image/enemy/Green_down_1.png')  # 图片保持持续的全局使用
        Brick_Image = PhotoImage(file='image/scene/brick.png')  # 图片保持持续的全局使用
        BOOM_IMAGE = PhotoImage(file='image/others/boom_static.png')  # 图片保持持续的全局使用

        self.canvas = canvas
        self.x = x
        self.y = y
        self.R = 48
        self.r = self.R / 2

        self.step = step
        self.dx = 0
        self.dy = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.step_count = 0
        self.draw()
        self.test_hit()

    def hit(self, tags, r=12):
        # 碰撞检查
        all_tags = list(self.canvas.find_withtag(tags))
        if tags == 'enemy':  # 如果是自己人，不检测自己，只检测队友
            all_tags.remove(self.id)  # 移除自己
        for i in all_tags:
            ret = self.canvas.coords(i)
            x = ret[0]  # x轴的坐标
            y = ret[1]  # y轴的坐标
            safe_distance = self.r + r  # 安全距离
            x_distance = abs(x - self.x)  # x直接的距离
            y_distance = abs(y - self.y)  # y直接的距离
            if x_distance < safe_distance and y_distance < safe_distance:
                # 碰撞了
                if self.direction == 'up' or self.direction == 'down':
                    self.y = self.y - self.dy  # x回退到之前的坐标点
                if self.direction == 'left' or self.direction == 'right':
                    self.x = self.x - self.dx  # y回退到之前的坐标点
                self.dx = 0  # x不移动
                self.dy = 0  # y不移动
                return i
        return False

    def send_bullet(self):
        # 发射子弹
        bullet_r = 6
        x = -48
        y = -48
        if self.direction == 'up':  # 根据坦克的坐标和方向确定子弹的坐标和方向
            x = self.x  # 根据坦克的坐标和方向确定子弹的坐标和方向
            y = self.y - self.r - bullet_r  # 根据坦克的坐标和方向确定子弹的坐标和方向
        if self.direction == 'down':  # 根据坦克的坐标和方向确定子弹的坐标和方向
            x = self.x  # 根据坦克的坐标和方向确定子弹的坐标和方向
            y = self.y + self.r + bullet_r  # 根据坦克的坐标和方向确定子弹的坐标和方向
        if self.direction == 'left':  # 根据坦克的坐标和方向确定子弹的坐标和方向
            x = self.x - self.r - bullet_r  # 根据坦克的坐标和方向确定子弹的坐标和方向
            y = self.y  # 根据坦克的坐标和方向确定子弹的坐标和方向
        if self.direction == 'right':  # 根据坦克的坐标和方向确定子弹的坐标和方向
            x = self.x + self.r + bullet_r  # 根据坦克的坐标和方向确定子弹的坐标和方向
            y = self.y  # 根据坦克的坐标和方向确定子弹的坐标和方向

        bullet = Bullet(self.canvas, x, y, 12, self.direction, 'enemy_bullet')
        bullet.start()  # 发射子弹

    def draw(self):
        global enemys
        image = eval('Green_' + self.direction + '_{}'.format(self.step_count))
        enemys.append(image)
        self.id = self.canvas.create_image(self.x, self.y, image=image, tags='enemy')

    def move(self):
        self.canvas.coords(self.id, self.x, self.y)

    def test_hit(self):
        # 测试碰撞
        for x in range(60, 564, 96):
            for y in range(60, 262, 24):
                "252和348" "228和252"
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

    def next(self):
        turn_direction = None
        if random.randint(0, 10) == 0:  # 随机转向
            turn_direction = random.choice(['up', 'down', 'left', 'right'])
        if random.randint(0, 20) == 0:  # 随机发射子弹
            self.send_bullet()

        if self.direction == 'right':  # 方向是右的处理逻辑
            self.dx = self.step
            right_x = self.x + self.dx + self.r
            if right_x >= self.canvas_width:
                self.x = self.canvas_width - self.r
                turn_direction = random.choice(['up', 'down', 'left'])  # 随机其他几个方向

            else:
                self.x += self.dx
        if self.direction == 'left':  # 方向是左的处理逻辑
            self.dx = -self.step
            left_x = self.x + self.dx - self.r
            if left_x <= 0:
                self.x = self.r
                turn_direction = random.choice(['up', 'down', 'left'])  # 随机其他几个方向
            else:
                self.x += self.dx
        if self.direction == 'up':  # 方向是上的处理逻辑
            self.dy = -self.step
            up_y = self.y + self.dy - self.r
            if up_y <= 0:
                self.y = self.r
                turn_direction = random.choice(['right', 'down', 'left'])  # 随机其他几个方向
            else:
                self.y += self.dy
        if self.direction == 'down':  # 方向是下的处理逻辑
            self.dy = self.step
            down_y = self.y + self.dy + self.r
            if down_y >= self.canvas_height:
                self.y = self.canvas_height - self.r
                turn_direction = random.choice(['right', 'up', 'left'])  # 随机其他几个方向
            else:
                self.y += self.dy
        if self.hit('brick', 12):  # 检测是否碰撞了其他  brick
            turn_direction = random.choice(['up', 'down', 'left', 'right'])  # 碰撞了就随机转向
        if self.hit('iron', 12):  # 检测是否碰撞了其他     iron
            turn_direction = random.choice(['up', 'down', 'left', 'right'])  # 碰撞了就随机转向
        if self.hit('hero', 12):  # 检测是否碰撞了其他  hero
            turn_direction = random.choice(['up', 'down', 'left', 'right'])  # 碰撞了就随机转向
        if self.hit('enemy', 12):  # 检测是否碰撞了其他    enemy
            turn_direction = random.choice(['up', 'down', 'left', 'right'])  # 碰撞了就随机转向
        hero_bullet = self.hit('hero_bullet', 12)  # 检测是否碰撞了其他 hero_bullet
        if hero_bullet:
            # 被英雄攻击了
            self.canvas.delete(hero_bullet)  # 立即销毁英雄的子弹
            self.canvas.itemconfig(self.id, image=BOOM_IMAGE)  # 爆炸图片
            self.stop = True  # 停止自己
            time.sleep(1)  # 等待一秒
            self.canvas.delete(self.id)  # 销毁自己

        if turn_direction:
            # 转向了就切换图片   和设置新的方向
            self.canvas.itemconfig(self.id, image=eval('Green_' + turn_direction + '_{}'.format(
                    self.step_count)))
            self.direction = turn_direction
        self.move()

    def run(self):
        pass
        while not self.stop:
            time.sleep(0.5)
            self.next()


if __name__ == '__main__':
    win = Tk()
    win.geometry('624x624+500+0')
    canvas = Canvas(win)
    canvas.pack(fill='both', expand=True)
    win.update()
    enemy = Enemy(canvas, x=24, y=24, step=24, direction='right')
    enemy.start()
    enemy = Enemy(canvas, x=24+48*3, y=24, step=24, direction='down')
    enemy.start()
    enemy = Enemy(canvas, x=24+48*5, y=24, step=24, direction='left')
    enemy.start()
    enemy = Enemy(canvas, x=24+48*9, y=24, step=24, direction='up')
    enemy.start()

    win.mainloop()
