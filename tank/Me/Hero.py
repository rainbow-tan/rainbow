from tkinter import *

from Bullet import Bullet

Tank_Left_0 = None  # 图片保持持续的全局使用
Tank_Left_1 = None  # 图片保持持续的全局使用
Tank_Right_0 = None  # 图片保持持续的全局使用
Tank_Right_1 = None  # 图片保持持续的全局使用
Tank_Up_0 = None  # 图片保持持续的全局使用
Tank_Up_1 = None  # 图片保持持续的全局使用
Tank_Down_0 = None  # 图片保持持续的全局使用
Tank_Down_1 = None  # 图片保持持续的全局使用
Brick_Image = None  # 图片保持持续的全局使用
BOOM_IMAGE = None  # 图片保持持续的全局使用


class Hero():
    """
    定义英雄
    """

    def __init__(self, canvas, x=240 - 24, y=600, step=24, direction='up'):
        self.direction = direction  # 方向
        global Tank_Left_0  # 图片保持持续的全局使用
        global Tank_Left_1  # 图片保持持续的全局使用
        global Tank_Right_0  # 图片保持持续的全局使用
        global Tank_Right_1  # 图片保持持续的全局使用
        global Tank_Up_0  # 图片保持持续的全局使用
        global Tank_Up_1  # 图片保持持续的全局使用
        global Tank_Down_0  # 图片保持持续的全局使用
        global Tank_Down_1  # 图片保持持续的全局使用
        global Brick_Image  # 图片保持持续的全局使用
        global BOOM_IMAGE  # 图片保持持续的全局使用
        Tank_Left_0 = PhotoImage(file='Image\\Yellow_Left_0.png')  # 图片保持持续的全局使用
        Tank_Left_1 = PhotoImage(file='Image\\Yellow_Left_1.png')  # 图片保持持续的全局使用
        Tank_Right_0 = PhotoImage(file='Image\\Yellow_Right_0.png')  # 图片保持持续的全局使用
        Tank_Right_1 = PhotoImage(file='Image\\Yellow_Right_1.png')  # 图片保持持续的全局使用
        Tank_Up_0 = PhotoImage(file='Image\\Yellow_Up_0.png')  # 图片保持持续的全局使用
        Tank_Up_1 = PhotoImage(file='Image\\Yellow_Up_1.png')  # 图片保持持续的全局使用
        Tank_Down_0 = PhotoImage(file='Image\\Yellow_Down_0.png')  # 图片保持持续的全局使用
        Tank_Down_1 = PhotoImage(file='Image\\Yellow_Down_1.png')  # 图片保持持续的全局使用
        Brick_Image = PhotoImage(file='image/scene/brick.png')  # 图片保持持续的全局使用
        BOOM_IMAGE = PhotoImage(file='image/others/boom_static.png')  # 图片保持持续的全局使用

        self.canvas = canvas
        self.x = x
        self.y = y
        self.R = 48
        self.r = self.R / 2

        self.step = step
        self.dx = self.step
        self.dy = self.step
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.draw()

        self.canvas.bind_all('<Key>', self.AnyKey)  # 绑定键盘

        self.step_count = 0
        self.test_hit()

    def hit(self, tags, r=12):
        for i in self.canvas.find_withtag(tags):
            ret = self.canvas.coords(i)
            x = ret[0]  # 障碍物的横坐标
            y = ret[1]  # 障碍物的纵坐标
            safe_distance = self.r + r
            x_distance = abs(x - self.x)  # x轴距离
            y_distance = abs(y - self.y)  # y轴距离
            if x_distance < safe_distance and y_distance < safe_distance:
                # 小于安全距离就会碰撞
                if self.direction == 'up' or self.direction == 'down':
                    self.y = self.y - self.dy
                    # 恢复到之前的y坐标，不让移动，否则就碰撞
                if self.direction == 'left' or self.direction == 'right':
                    self.x = self.x - self.dx
                    # 恢复到之前的x坐标，不让移动，否则就碰撞

                self.dx = 0  # 不移动
                self.dy = 0  # 不移动
                return True

    def send_bullet(self):
        # 发射子弹
        bullet_r = 6
        x = -48
        y = -48
        if self.direction == 'up':  # 根据英雄的方向决定子弹的方向，坐标同理
            x = self.x  # 根据英雄的方向决定子弹的方向，坐标同理
            y = self.y - self.r - bullet_r  # 根据英雄的方向决定子弹的方向，坐标同理
        if self.direction == 'down':  # 根据英雄的方向决定子弹的方向，坐标同理
            x = self.x  # 根据英雄的方向决定子弹的方向，坐标同理
            y = self.y + self.r + bullet_r  # 根据英雄的方向决定子弹的方向，坐标同理
        if self.direction == 'left':  # 根据英雄的方向决定子弹的方向，坐标同理
            x = self.x - self.r - bullet_r  # 根据英雄的方向决定子弹的方向，坐标同理
            y = self.y  # 根据英雄的方向决定子弹的方向，坐标同理
        if self.direction == 'right':  # 根据英雄的方向决定子弹的方向，坐标同理
            x = self.x + self.r + bullet_r  # 根据英雄的方向决定子弹的方向，坐标同理
            y = self.y  # 根据英雄的方向决定子弹的方向，坐标同理

        bullet = Bullet(self.canvas, x, y, 12, self.direction, 'hero_bullet')
        bullet.start()  # 发射子弹

    def AnyKey(self, event):
        if event.keysym not in ['Left', 'Right', 'Up', 'Down', 'space']:
            return
        self.step_count = 1 if self.step_count == 0 else 0
        if event.keysym != 'space':
            # 切换图片
            self.canvas.itemconfig(self.id,
                                   image=eval('Tank_' + event.keysym + '_' + str(self.step_count)))
        if event.keysym == 'Left':  # 左
            self.dx = -self.step
            left_x = self.x + self.dx - self.r
            if self.direction == 'left':  # 方向是左 直接移动
                if left_x <= 0:
                    self.x = self.r
                    self.is_left = True
                else:
                    self.x += self.dx
            else:
                self.direction = 'left'  # 方向不是左的转为左
        if event.keysym == 'Right':
            self.dx = self.step
            right_x = self.x + self.dx + self.r
            if self.direction == 'right':  # 方向是右 直接移动
                if right_x >= self.canvas_width:
                    self.x = self.canvas_width - self.r
                    self.is_right = True
                else:
                    self.x += self.dx
            else:
                self.direction = 'right'  # 方向不是右的转为右

            pass

        if event.keysym == 'Up':
            self.dy = -self.step
            up_y = self.y + self.dy - self.r
            if self.direction == 'up':
                if up_y <= 0:
                    self.y = self.r
                    self.is_up = True
                else:
                    self.y += self.dy
            else:
                self.direction = 'up'
        if event.keysym == 'Down':
            self.dy = self.step
            down_y = self.y + self.dy + self.r
            if self.direction == 'down':
                if down_y >= self.canvas_height:
                    self.y = self.canvas_height - self.r
                    self.is_down = True
                else:
                    self.y += self.dy
            else:
                self.direction = 'down'
        if event.keysym == 'space':
            # 空格发射子弹
            self.send_bullet()
            pass
        self.hit('brick')  # 是否碰撞 brick
        self.hit('iron')  # 是否碰撞 iron
        self.hit('enemy')  # 是否碰撞 enemy

        self.move()

    def draw(self):
        self.id = self.canvas.create_image(self.x, self.y, image=Tank_Up_0, tags='hero')

    def move(self):
        self.canvas.coords(self.id, self.x, self.y)

    def test_hit(self):  # 测试碰撞
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
    my_canvas = Canvas(win)
    my_canvas.pack(fill='both', expand=True)
    win.update()

    Hero(my_canvas)

    win.mainloop()
