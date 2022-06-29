# 作者: 张浩然
# 2022年06月25日22时46分44秒
class Goods:
    def __init__(self):
        self.orginal_price=100
        self.discount=0.8
    @property
    def price(self):
        return  self.orginal_price * self.discount
    @price.setter
    def price_setter(self,value):
        self.orginal_price=value
    @price.deleter
    def price_delete(self):
        del self.orginal_price
g= Goods()
g.price_setter=100 #在装饰器外调用
print(g.price)
del g.price_delete # 在装饰器外调用del
print(g.price)