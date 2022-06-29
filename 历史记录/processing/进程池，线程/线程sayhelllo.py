# 作者: 张浩然
# 2022年06月20日19时24分54秒
from threading import  Thread
import time
def say():
    print('sayhello!')

if __name__ == '__main__':
    for i in range(5):
        th = Thread(target=say)
        th.start()


        th.join()