# 作者: 张浩然
# 2022年06月20日15时41分53秒
from greenlet import greenlet
import time
def test1():
    while True:
        print('---A---')
        gr2.switch()# 用yeild实现
        time.sleep(0.5)
def test2():
    while True:
        print('----B----')
        gr1.switch()
        time.sleep(0.5)
gr1 = greenlet(test1)#创建协程
gr2 = greenlet(test2)# 创建协程2
gr1.switch()#启动协程
