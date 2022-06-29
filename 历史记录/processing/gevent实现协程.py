# 作者: 张浩然
# 2022年06月20日15时47分49秒
import gevent
def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)#getcurrent接口表示现在有多少协程
        #用来模拟一个耗时操作，
        gevent.sleep(1)#该协程睡眠改用另一个协程进行
g1 = gevent.spawn(f,5)#创建协程1
g2= gevent.spawn(f,5)#创建协程2
g3 = gevent.spawn(f,5)#创建协程3
g1.join()
g2.join()
g3.join()
