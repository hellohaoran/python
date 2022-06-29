# 作者: 张浩然
# 2022年06月16日12时10分14秒
from plane_sprites import *
import time
# pygame专门提供一个模块pygame.display用于创建管理游戏窗口

class PlaneGame:
    '''飞机大战主游戏'''
    def __init__(self):
        print('游戏初始化')
        #1.创建游戏的窗口
        self.screen=pygame.display.set_mode(SCREEN_RECT.size)
