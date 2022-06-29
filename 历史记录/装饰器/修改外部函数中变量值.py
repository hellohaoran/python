# 作者: 张浩然
# 2022年06月29日08时29分16秒
x=300

def test1():
    x=200 # 这个x是nunlocal的即 局部变量
    def test2():
        nonlocal x
        print("------1------x=%d"%x)
        x=100#一旦修改就必须加修饰 不然不知道是全局变量还是局部变量
        print("--------2-------x=%d"%x)
    return test2

t= test1() # 拿到闭包的入口地址
t() #运行闭包

# 外部函数的形参也是nonlocal类型
def counter(start = 0): # 此时counter是闭包
    def incr():
        nonlocal start
        start +=1
        return start
    return incr

c1 = counter(50) # 传递部分参数 ，返回的是内部函数地址
print(c1())

c2 = counter(5) # 传递给闭包部分参数 ， 返回的是 内部函数地址

print(c2())


