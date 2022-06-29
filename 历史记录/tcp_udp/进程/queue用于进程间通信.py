# 作者: 张浩然
# 2022年06月19日21时14分59秒
from multiprocessing import Process,Queue
import time
def writer(q:Queue):
    for i in ['A',"B","C"]:
        q.put(i)
        print('writer write')
        time.sleep(1)
def reader(q:Queue):
    while not q.empty():
        value = q.get()
        print("{} is dequeueing".format(value))
        time.sleep(2)

if __name__ == '__main__':
    q=Queue()
    p = Process(target=writer,args=(q,))
    pr = Process(target=reader,args=(q,))
    p.start()
    time.sleep(0.5)
    pr.start()
    p.join()
    pr.join()