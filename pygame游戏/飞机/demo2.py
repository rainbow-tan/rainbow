import pygame
from pygame.locals import *

pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((200, 200))  # 创建窗口
face = pygame.Surface((50, 50))  # 创建一个50x50的平面
face.fill(color='pink')  # 填充橙色
rect = face.get_rect()  # 获取面积和X,Y坐标
print(f'top:{rect.top}')
print(f'topleft:{rect.topleft}')
print(f'topright:{rect.topright}')
print(f'bottom:{rect.bottom}')
print(f'bottomleft:{rect.bottomleft}')
print(f'bottomright:{rect.bottomright}')
print(f'left:{rect.left}')
print(f'right:{rect.right}')
print(f'midtop:{rect.midtop}')
print(f'midbottom:{rect.midbottom}')
print(f'midleft:{rect.midleft}')
print(f'midright:{rect.midright}')
print(f'center:{rect.center}')
print(f'centerx:{rect.centerx}')
print(f'centery:{rect.centery}')
print(f'w:{rect.w}')
print(f'width:{rect.width}')
print(f'h:{rect.h}')
print(f'height:{rect.height}')
print(f'x:{rect.x}')
print(f'y:{rect.y}')
print(f'size:{rect.size}')

running = True
while running:
    for event in pygame.event.get():  # 获取所有事件
        if event.type == KEYDOWN:  # 获取按钮按下事件
            if event.key == K_ESCAPE:  # 如果是按下了ESC键
                running = False
        if event.type == QUIT:  # 如果是QUIT事件,如点击关闭窗口按钮
            running = False
pygame.quit()  # 退出pygame
