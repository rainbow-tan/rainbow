import random

import pygame
from pygame.locals import *


class Airplane(pygame.sprite.Sprite):  # 继承pygame.sprite.Sprite精灵对象
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.image.load('resource/jet.png').convert()  # 加载图片
        self.rect = self.image.get_rect()  # 获取X,Y坐标和大小
        self.image.set_colorkey('white', RLEACCEL)  # 显示时设置白色为透明
        print(f'rect:{self.rect}')  # 不设置默认是0,0
        self.rect.x = 20  # 重新设置X轴坐标
        self.rect.y = 100  # 重新设置Y轴坐标
        self.speed = speed

    def update(self, pressed_keys, *args, **kwargs):
        if pressed_keys[K_UP]:  # 如果按下的是方向上键
            self.rect.move_ip(0, -self.speed)  # 更新rect的X,Y
        if pressed_keys[K_DOWN]:  # 如果按下的是方向下键
            self.rect.move_ip(0, self.speed)  # 更新rect的X,Y
        if pressed_keys[K_LEFT]:  # 如果按下的是方向左键
            self.rect.move_ip(-self.speed, 0)  # 更新rect的X,Y
        if pressed_keys[K_RIGHT]:  # 如果按下的是方向右键
            self.rect.move_ip(self.speed, 0)  # 更新rect的X,Y
        self.stay_inside()  # 保证一直在窗口里面

    def stay_inside(self):  # 保证一直在窗口里面
        if self.rect.top < 0:  # 如果上边界小于0
            self.rect.top = 0  # 设置上边界为0
        if self.rect.bottom > screen.get_height():  # 如果下边界超过窗口高度
            self.rect.bottom = screen.get_height()  # 设置下边界为窗口高度
        if self.rect.left < 0:  # 如果左边界小于0
            self.rect.left = 0  # 设置左边界为0
        if self.rect.right > screen.get_width():  # 如果右边界超过窗口宽度
            self.rect.right = screen.get_width()  # 设置右边界为窗口宽度


class Bullet(pygame.sprite.Sprite):  # 继承pygame.sprite.Sprite精灵对象
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resource/missile.png').convert()  # 加载图片
        self.image.set_colorkey('white', RLEACCEL)  # 显示时设置白色为透明
        self.rect = self.image.get_rect()  # 获取X,Y坐标和大小
        self.rect.centerx = screen.get_width() + 20  # 设置中心X轴坐标,设置在窗口最右边距离20
        self.rect.centery = random.randint(0, screen.get_height())  # 设置中心Y轴坐标,随机坐标
        self.speed = random.randint(4, 8)  # 设置速度随机
        self.stay_inside()  # 保证一直在窗口里面

    def update(self, *args, **kwargs):
        self.rect.move_ip(-self.speed, 0)  # 一直向左跑,速度随机
        if self.rect.right < 0:  # 如果跑到头
            self.kill()  # 从精灵组移除自己

    def stay_inside(self):  # 保证一直在窗口里面
        if self.rect.top < 0:  # 如果上边界小于0
            self.rect.top = 0  # 设置上边界为0
        if self.rect.bottom > screen.get_height():  # 如果下边界超过窗口高度
            self.rect.bottom = screen.get_height()  # 设置下边界为窗口高度
        if self.rect.left < 0:  # 如果左边界小于0
            self.rect.left = 0  # 设置左边界为0
        if self.rect.right > screen.get_width():  # 如果右边界超过窗口宽度
            self.rect.right = screen.get_width()  # 设置右边界为窗口宽度


class Cloud(pygame.sprite.Sprite):  # 继承pygame.sprite.Sprite精灵对象
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resource/cloud.png').convert()  # 加载图片
        self.image.set_colorkey('black', RLEACCEL)  # 显示时设置黑色为透明
        self.rect = self.image.get_rect()  # 获取X,Y坐标和大小
        self.rect.x = random.randint(screen.get_width() + 20, screen.get_width() + 100)  # 设置X轴坐标
        self.rect.y = random.randint(0, screen.get_height())  # 设置Y轴坐标,随机坐标
        self.speed = 3  # 设置速度
        # self.stay_inside()  # 保证一直在窗口里面

    def update(self, *args, **kwargs):
        self.rect.move_ip(-self.speed, 0)  # 一直向左跑,速度随机
        if self.rect.right < 0:  # 如果跑到头
            self.kill()  # 从精灵组移除自己

    def stay_inside(self):  # 保证一直在窗口里面
        if self.rect.top < 0:  # 如果上边界小于0
            self.rect.top = 0  # 设置上边界为0
        if self.rect.bottom > screen.get_height():  # 如果下边界超过窗口高度
            self.rect.bottom = screen.get_height()  # 设置下边界为窗口高度
        if self.rect.left < 0:  # 如果左边界小于0
            self.rect.left = 0  # 设置左边界为0
        if self.rect.right > screen.get_width():  # 如果右边界超过窗口宽度
            self.rect.right = screen.get_width()  # 设置右边界为窗口宽度


ADDENEMY = USEREVENT + 1  # 自定义事件的值,必须大于USEREVENT,因为在USEREVENT之下的数值都被pygame用完了
ADDCLOUD = USEREVENT + 2  # 自定义事件的值,必须大于USEREVENT,因为在USEREVENT之下的数值都被pygame用完了
pygame.time.set_timer(ADDENEMY, 500)  # 定时器,用于生成子弹,负责把事件传入PyGame的事件队列中
pygame.time.set_timer(ADDCLOUD, 1000)  # 定时器,用于生成云彩,负责把事件传入PyGame的事件队列中
pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((800, 600))  # 创建窗口
airplane = Airplane(5)  # 创建Player对象
running = True
clock = pygame.time.Clock()  # 创建Clock用于跟踪时间
bullets = pygame.sprite.Group()  # 定义精灵组
all_sprite = pygame.sprite.Group()  # 定义精灵组,用于存放所有精灵
all_sprite.add(airplane)  # 添加player到精灵组

while running:
    for event in pygame.event.get():  # 获取所有事件
        if event.type == KEYDOWN:  # 获取按钮按下事件
            if event.key == K_ESCAPE:  # 如果是按下了ESC键
                running = False
        if event.type == QUIT:  # 如果是QUIT事件,如点击关闭窗口按钮
            running = False
        if event.type == ADDENEMY:  # 监控自定义事件
            bullet = Bullet()  # 创建敌人
            bullets.add(bullet)  # 添加到精灵组
            all_sprite.add(bullet)  # 添加到all_sprite精灵组
        if event.type == ADDCLOUD:  # 监控自定义事件
            cloud = Cloud()  # 创建云彩
            all_sprite.add(cloud)  # 添加到all_sprite精灵组
    clock.tick(60)  # 每秒刷新多少帧,不设置按键后移动的飞快
    pressed_key = pygame.key.get_pressed()  # 获取按键
    screen.fill((135, 206, 250))  # 为窗口填充颜色
    all_sprite.update(pressed_key)  # 更新组中的精灵位置
    all_sprite.draw(screen)  # 显示整个精灵组中的精灵

    # 碰撞检测,检测player和enemies精灵组中精灵是否碰撞
    collide_sprite = pygame.sprite.spritecollideany(airplane, bullets)
    if collide_sprite:  # 如果碰撞,返回精灵组中的碰撞精灵
        collide_sprite.kill()  # 从精灵组移除自己
    pygame.display.update()  # 刷新整个平面 或者 pygame.display.flip()
pygame.quit()  # 退出pygame
