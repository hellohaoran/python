# 作者: 张浩然
# 2022年06月19日16时34分51秒
from multiprocessing import Process
import os
import time
def run_proc(name,age,**kwargs):
    for i in range(10):
        print('姓名：{}，年纪：{},pid={}'.format(name,age,os.getpid()))
        print(kwargs)

if __name__ == '__main__':
    p=Process(target=run_proc,args=('test',18),kwargs={'one':45}) #Process给函数传递参数需要args=,kwargs=
    p.start()
    time.sleep(10)
    p.terminate()
    p.join(1)

