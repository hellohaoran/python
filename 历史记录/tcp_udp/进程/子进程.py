# 作者: 张浩然
# 2022年06月19日12时18分46秒
from multiprocessing import Process
import time
def run_():
    while True:
        print('-'*5+'2'+'-'*5)
        time.sleep(1)
if __name__ == '__main__':
    p=Process(target=run_) #创建进程
    p.start()# 进程启动
    while True:
        print('-'*5+'1'+'-'*5)
        time.sleep(1)
