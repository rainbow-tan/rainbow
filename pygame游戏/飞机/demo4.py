import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):  # 继承pygame.sprite.Sprite精灵对象
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))  # 创建Surface平面对象
        self.surf.fill('orange')  # 填充橙色
        self.rect = self.surf.get_rect()  # 获取X,Y坐标和大小
        print(f'rect:{self.rect}')  # 不设置默认是0,0
        self.rect.x = 100  # 重新设置X轴坐标
        self.rect.y = 100  # 重新设置Y轴坐标


pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((300, 300))  # 创建窗口
screen.fill(color='white')  # 填充颜色
player = Player()  # 创建Player对象
running = True
while running:
    for event in pygame.event.get():  # 获取所有事件
        if event.type == KEYDOWN:  # 获取按钮按下事件
            if event.key == K_ESCAPE:  # 如果是按下了ESC键
                running = False
        if event.type == QUIT:  # 如果是QUIT事件,如点击关闭窗口按钮
            running = False
    screen.blit(player.surf, player.rect)  # 放置player对象
    pygame.display.update()  # 刷新整个平面 或者 pygame.display.flip()
pygame.quit()  # 退出pygame
