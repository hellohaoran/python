# 作者: 张浩然
# 2022年06月21日08时51分48秒
import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent()) #返回当前运行的greenlet，当遇到阻塞时切换到其他greenlet
        gevent.sleep(1)
g1=gevent.spawn(f,5)
g2=gevent.spawn(f,5)
g3=gevent.spawn(f,5)
g1.join()
g2.join()
g3.join()