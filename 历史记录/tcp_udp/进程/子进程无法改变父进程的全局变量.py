# 作者: 张浩然
# 2022年06月19日17时02分48秒
from multiprocessing import Process
import os
import time
nums=[11,22]
def work1(nums):#
    '''子进程要执行的代码'''
    print('in process1 pid=%d,nums=%s'%(os.getpid(),nums))
    for i in range(3):
        nums.append(i)
        time.sleep(1)
    print(nums)
def work2():
    print(nums)
if __name__ == '__main__':

    #子进程相当于父进程的复制，在另外的空间
    p=Process(target=work1,args=(nums,))
    print(id(p))
    p.start()
    time.sleep(10)# 以免进程一启动就结束
    f= Process(target=work2)
    print(id(f))
    f.start()
    time.sleep(3)# 以免进程一启动就结束
    p.terminate()
    f.terminate()
    p.join()
    f.join()


