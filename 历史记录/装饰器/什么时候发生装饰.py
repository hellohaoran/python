# 作者: 张浩然
# 2022年06月29日09时18分03秒
def set_func(func):
    print('---开始装饰---')
    def call_func(*args,**kwargs):
        print('---权限验证---')
        func(*args,**kwargs)
    return call_func

@set_func# 运行 test1= set_func(test1)
def test1(num):
    print('-----test1------{}'.format(num))
test1(3)