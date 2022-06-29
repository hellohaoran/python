# 作者: 张浩然
# 2022年06月20日17时55分26秒
from multiprocessing import Pool

import os,time,random
#具体任务是模拟睡觉一段时间
def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d"% (msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop=time.time()
    print(msg,"执行完毕，耗时%0.2f"%(t_stop-t_start))
if __name__ == '__main__':
    po=Pool(3)
    for i in range(10):
        po.apply_async(worker,(i,))# worker是功能，i是参数 创建进程
    print('------start-----')
    po.close()
    print('close之后') # 父进程由子进程创建，
    po.join()#将进程池中的所有资源回收

    print('-----end------')