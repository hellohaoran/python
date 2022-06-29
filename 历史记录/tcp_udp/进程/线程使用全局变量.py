# 作者: 张浩然
# 2022年06月20日10时34分16秒
import threading
import time
num=0
def work1():
    global num
    for i in range(1000000):
        num +=1
def work2():
    global num
    for i in range(1000000):
        num +=1
if __name__ == '__main__':
    w1 = threading.Thread(target=work1)
    w2= threading.Thread(target=work2)
    w1.start()
    time.sleep(0.005)
    w2.start()
    w1.join()
    w2.join()
    print(num)