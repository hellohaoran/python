# 作者: 张浩然
# 2022年06月20日20时32分44秒
from threading import Thread,Lock
import time
num = 0
def worker1(mutex:Lock):
    global num

    for i in range(100):
        mutex.acquire()
        num += 1
        mutex.release()
def worker2(mutex):
    global num

    for i in range(1000000):
        mutex.acquire()
        num +=1
        mutex.release()
if __name__ == '__main__':
    mutex =Lock()
    t1 = Thread(target=worker1,args=(mutex,))
    start=time.time()
    t1.start()
    # time.sleep(1)
    t2 = Thread(target=worker2, args=(mutex,))
    t2.start()
    # time.sleep(1)
    t1.join()
    t2.join()
    end=time.time()
    print(num)
    print(end-start)