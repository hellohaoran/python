# 作者: 张浩然
# 2022年06月29日09时22分51秒
def add_first(func):
    print("---开始进行装饰权限1的功能---")
    def call_func(*args,**kwargs):
        print('----这时权限验证1-----')
        return func(*args,**kwargs)
    return call_func

def add_second(func):
    print("---开始进行装饰权限2的功能----")
    def call_func(*args,**kwargs):
        print("---这是权限验证2----")
        return func(*args,**kwargs)
    return call_func

@add_first
@add_second # 与装饰器离得近的先装饰，离的远的后装饰 类似于压栈 ： 离得近的先入栈 后出站
def test1():# 先装饰的后执行
    print('---test1---')

test1()