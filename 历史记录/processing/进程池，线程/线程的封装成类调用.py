# 作者: 张浩然
# 2022年06月20日20时22分57秒
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(0.5)
            msg = 'I‘m'+self.name+'@'+str(i)
            print(msg)
def test():
    for i in range(5):
        t=MyThread()#线程创建完成
        t.start()#线程开始执行
if __name__ == '__main__':
    test()
