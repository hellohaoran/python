# 作者: 张浩然
# 2022年06月19日15时58分17秒
import  os
import time
from multiprocessing import Process
def _getpd():
    print("子进程的pid为%s"%os.getpid())
    print('子进程将要结束！')
    while True:
        time.sleep(1)
if __name__ == '__main__':
    f = Process(target=_getpd)
    f.start()
    print('父进程的pid为%s'%os.getpid())
    print('父进程结束！')
