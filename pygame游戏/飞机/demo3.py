import pygame
from pygame.locals import *

pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((300, 300))  # 创建窗口
screen.fill(color='white')  # 填充颜色
face = pygame.Surface((50, 50))  # 创建一个50x50的平面
face.fill(color='orange')  # 填充颜色

running = True
while running:
    for event in pygame.event.get():  # 获取所有事件
        if event.type == KEYDOWN:  # 获取按钮按下事件
            if event.key == K_ESCAPE:  # 如果是按下了ESC键
                running = False
        if event.type == QUIT:  # 如果是QUIT事件,如点击关闭窗口按钮
            running = False
    screen.blit(face, (100, 100))  # 放置平面face
    pygame.display.flip()  # 刷新整个平面 或者 pygame.display.update()
pygame.quit()  # 退出pygame
