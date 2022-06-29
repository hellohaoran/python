# 作者: 张浩然
# 2022年06月15日16时08分14秒

class A:
    def __init__(self):
        self.name='xiongda'
        self.addr='hainan'
    def sleep(self):
        print('sleep')
class B(A):
    def __init__(self):
        super().__init__()
        self.age=10
    def ok(self):

b=B()
b.sleep()
print(b.addr)