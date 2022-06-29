# 作者: 张浩然
# 2022年06月15日14时55分22秒
import pygame
import time
pygame.init()
# ch创建游戏窗口
screen = pygame.display.set_mode((480,700))
# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("./images/background.png")
#2.blit 绘制图像
screen.blit(bg,(0,0))
#3.update更新屏幕显示
pygame.display.update()
while True:
    time.sleep(1)
pygame.quit()