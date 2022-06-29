# 作者: 张浩然
# 2022年06月25日22时15分27秒
class Price:
    def __init__(self):
        self.__price=10
    @property # property装饰器 ，自动添加一个money属性，当调用获取money值时调用装饰方法
    def price(self):
        return self.__price
    @price.setter # 当对money设置值时，调用装饰器方法
    def setter(self,value):
        self.__price = value

p = Price()
p.setter=30

print(p.price)
