# 作者: 张浩然
# 2022年06月20日19时30分23秒
import time
from threading import Thread
def while1():
    while True:
        print('while1')
def while2():
    while True:
        print('while2')
if __name__ == '__main__':
    w1 = Thread(target=while1)
    w2 = Thread(target=while2)
    w1.start()
    w2.start()

    while True:
        print('this is real while!') # cpu占有率是1/3说明时间片轮流分配
