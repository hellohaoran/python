# 作者: 张浩然
# 2022年06月29日08时40分19秒
def set_func(func):
    def call_func():
        print('----权限验证————-')
        func()
    return call_func

@set_func# 只要开始 运行就会test1 = set_func(test1)
def test1():
    print("-----test1------")
test1()