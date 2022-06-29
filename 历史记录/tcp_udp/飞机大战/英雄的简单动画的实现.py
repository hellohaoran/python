# 作者: 张浩然
# 2022年06月15日15时12分18秒
import pygame

#游戏的初始化
pygame.init()

#创建游戏的窗口 480*700
screen=pygame.display.set_mode((480,700))

#绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

#在所有绘制工作完成之后，统一调用update
pygame.display.update()

clock = pygame.time.Clock()# 创建时钟对象
hero_rect=pygame.Rect(150,700,102,126)
# 英雄机的图片对象
while True:
    #可以在指定循环体内的代码执行频率
    clock.tick(60)

    #2.修改飞机位置
    hero_rect.y -= 1
    if hero_rect.y== -hero_rect.height :
        hero_rect.y=700
    #3.调用blit方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    #4.调用update方法更新显示
    pygame.display.update()
pygame.quit()

