# 作者: 张浩然
# 2022年06月15日15时03分02秒
import pygame
pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((480,700))
#绘制背景图
#1.加载背景图
bg =pygame.image.load("./images/background.png")
#2.blit绘制图像
screen.blit(bg,(0,0))
#3.加载英雄图像
hero = pygame.image.load("./images/me1.png")
#4.绘制在屏幕上
screen.blit(hero,(200,500))
pygame.display.update()
while True:
    pass
pygame.quit()