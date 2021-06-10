import pygame
from pygame.locals import *

pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((200, 200))  # 创建窗口
pygame.display.set_caption('Title')  # 设置标题
running = True
while running:
    for event in pygame.event.get():  # 获取所有事件
        if event.type == KEYDOWN:  # 获取按钮按下事件
            if event.key == K_ESCAPE:  # 如果是按下了ESC键
                running = False
        if event.type == QUIT:  # 如果是QUIT事件,如点击关闭窗口按钮
            running = False
pygame.quit()  # 退出pygame
