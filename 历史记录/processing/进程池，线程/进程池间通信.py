# 作者: 张浩然
# 2022年06月20日18时06分38秒
from multiprocessing import Manager,Pool# 进程池间通信要用Manager包
import os,time,random

def reader(q):
    print("reader启动（%s）,父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取消息：%s"% q.get())
def writer(q):
    print("writer启动(%s),父进程为(%s)"% (os.getpid(),os.getppid()))
    for i in "wangdao":
        q.put(i)
    time.sleep(3)
if __name__ == '__main__':
    print("(%s) start "%os.getpid())
    q=Manager().Queue()#使用Manager中的Queue进行通信
    po=Pool()# 初始化进程池
    po.apply_async(writer,(q,))#用进程池创建进程，用q传参
    time.sleep(1)# 先让上面的任务向Queue存入数据，然后再让下面的任务开始从中提取数据
    po.apply_async(reader,(q,))
    po.close()
    po.join()
    print("(%s) End"% os.getpid())
