import random

import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):  # 继承pygame.sprite.Sprite精灵对象
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # 创建Surface平面对象
        self.image.fill('orange')  # 填充颜色
        self.rect = self.image.get_rect()  # 获取X,Y坐标和大小
        print(f'rect:{self.rect}')  # 不设置默认是0,0
        self.rect.x = 20  # 重新设置X轴坐标
        self.rect.y = 100  # 重新设置Y轴坐标

    def update(self, pressed_keys, *args, **kwargs):
        if pressed_keys[K_UP]:  # 如果按下的是方向上键
            self.rect.move_ip(0, -5)  # 更新rect的X,Y
        if pressed_keys[K_DOWN]:  # 如果按下的是方向下键
            self.rect.move_ip(0, 5)  # 更新rect的X,Y
        if pressed_keys[K_LEFT]:  # 如果按下的是方向左键
            self.rect.move_ip(-5, 0)  # 更新rect的X,Y
        if pressed_keys[K_RIGHT]:  # 如果按下的是方向右键
            self.rect.move_ip(5, 0)  # 更新rect的X,Y
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


class Enemy(pygame.sprite.Sprite):  # 继承pygame.sprite.Sprite精灵对象
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # 创建Surface平面对象
        self.image.fill('blue')  # 填充颜色
        self.rect = self.image.get_rect()  # 获取X,Y坐标和大小
        self.rect.centerx = screen.get_width() + 20  # 设置中心X轴坐标,设置在窗口最右边距离20
        self.rect.centery = random.randint(0, screen.get_height())  # 设置中心Y轴坐标,随机坐标
        self.speed = random.randint(1, 5)  # 设置速度随机

    def update(self, *args, **kwargs):
        self.rect.move_ip(-self.speed, 0)  # 一直向左跑,速度随机
        if self.rect.right < 0:  # 如果跑到头
            self.kill()  # 从精灵组移除自己


ADDENEMY = USEREVENT + 1  # 自定义事件的值,必须大于USEREVENT,因为在USEREVENT之下的数值都被pygame用完了
pygame.time.set_timer(ADDENEMY, 500)  # 定时器,用于生成敌人,负责把事件传入PyGame的事件队列中
pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((300, 300))  # 创建窗口
player = Player()  # 创建Player对象
running = True
clock = pygame.time.Clock()  # 创建Clock用于跟踪时间
enemies = pygame.sprite.Group()  # 定义精灵组,用于存放enemy
all_sprite = pygame.sprite.Group()  # 定义精灵组,用于存放所有精灵
all_sprite.add(player)  # 添加player到精灵组

while running:
    for event in pygame.event.get():  # 获取所有事件
        if event.type == KEYDOWN:  # 获取按钮按下事件
            if event.key == K_ESCAPE:  # 如果是按下了ESC键
                running = False
        if event.type == QUIT:  # 如果是QUIT事件,如点击关闭窗口按钮
            running = False
        if event.type == ADDENEMY:  # 监控自定义事件
            enemy = Enemy()  # 创建敌人
            enemies.add(enemy)  # 添加到enemies精灵组
            all_sprite.add(enemy)  # 添加到all_sprite精灵组
    clock.tick(100)  # 每秒刷新多少帧,不设置按键后移动的飞快
    pressed_key = pygame.key.get_pressed()  # 获取按键
    screen.fill(color='white')  # 为窗口填充白色
    all_sprite.update(pressed_key)  # 更新组中的精灵位置
    all_sprite.draw(screen)  # 显示整个精灵组中的精灵

    # 碰撞检测,检测player和enemies精灵组中精灵是否碰撞
    collide_sprite = pygame.sprite.spritecollideany(player, enemies)
    if collide_sprite:  # 如果碰撞,返回精灵组中的碰撞精灵
        collide_sprite.kill()  # 从精灵组移除自己
    pygame.display.update()  # 刷新整个平面 或者 pygame.display.flip()
pygame.quit()  # 退出pygame
