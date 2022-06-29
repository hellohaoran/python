# 作者: 张浩然
# 2022年06月20日21时15分02秒
import threading
import time
class MyThread1(threading.Thread):
    def run(self):
        #对mutexA上锁,延时1秒等待另一个进程把mutexB锁上
        mutexA.acquire()
        print('Thread1 A ')
        time.sleep(2)
        #对mutexA上锁
        mutexB.acquire()
        print('Thread1 B ')

        mutexB.release()
        mutexA.release()

class MyThread2(threading.Thread):
    def run(self):
        #对mutexB上锁,后延时两秒等待另一个进程把mutexA锁上
        mutexB.acquire()
        print('Thread2 B')
        time.sleep(2)

        mutexA.acquire()
        print('Thread2 A  ')

        mutexB.release()
        mutexA.release()
if __name__ == '__main__':
    mutexA=threading.Lock()
    mutexB=threading.Lock()
    t1=MyThread1()
    t2=MyThread2()
    t1.start()
    t2.start()