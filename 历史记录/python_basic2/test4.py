# 作者: 张浩然
# 2022年06月08日08时55分59秒
class A :
    def __init__(self):
        self.__name ="A"
    def a(self):
        print("this is %s" % self.__name)


class B:
    def __init__(self):
        self.__nameb ="b"
    def b(self):
        print("this is %s" % self.__nameb)
class C(B):
    def c(self):
        print("this is c")



c = C()

c.b() # 子类可以通过父类的一般方法间接调用父类的私有属性

