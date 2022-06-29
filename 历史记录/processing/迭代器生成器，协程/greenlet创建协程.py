# 作者: 张浩然
# 2022年06月21日08时45分00秒
from greenlet import greenlet
import time
def test1():
    while True:
        print('-----A-------')
        gr2.switch()# 遇到卡顿到另一个协程中去
        time.sleep(0.5)

def test2():
    while True:
        print('----B-----')
        gr1.switch()# 遇到卡顿到另一个协程中去
        time.sleep(0.5)
gr1 = greenlet(test1)#创建协程
gr2 = greenlet(test2)#创建协程
#切换到gr1中运行
gr1.switch()
