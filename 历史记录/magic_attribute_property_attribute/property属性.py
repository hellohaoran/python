# 作者: 张浩然
# 2022年06月25日21时57分50秒
class Foo:
    def func(self):
        print('I am func')
    @property
    def prep(self):#property属性就是普通函数当作属性，他有set get方法， 调用时返回的是属性
        print('I am property')
f = Foo()
f.func()
f.prep
class Goods:
    def __init__(self):
        self.name ='good'
    @property
    def sayname(self):
        self.name = 'fneg'
        return self.name
g = Goods()
print(g.sayname)
