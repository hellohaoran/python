# 作者: 张浩然
# 2022年06月20日20时32分44秒
from threading import Thread
import time
num = 0
def worker1():
    global num
    for i in range(1000000):
        num += 1
def worker2():
    global num
    for i in range(1000000):
        num +=1
if __name__ == '__main__':
    t1 = Thread(target=worker1)
    t2 = Thread(target=worker2)
    t1.start()
    # time.sleep(1)
    t2.start()
    # time.sleep(1)
    t1.join()
    t2.join()
    print(num)