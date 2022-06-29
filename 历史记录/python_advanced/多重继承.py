# 作者: 张浩然
# 2022年06月22日21时29分45秒
print('******多继承使用super().__init__ 发生的状态')
class Parent:
    def __init__(self,name,*args,**kwargs):
        print('parent的init开始被调用')
        self.name=name
        print('parent的init结束被调用')
class Son1(Parent):
    def __init__(self,name,age,*args,**kwargs):
        print('son1的init开始被调用')
        self.age=age
        super().__init__(name,*args,**kwargs)
        print('son1的init结束被调用')
class Son2(Parent):
    def __init__(self,name,gender,*args,**kwargs):
        print('son2的init开始被调用')
        self.gender=gender
        super().__init__(name,*args,**kwargs)
        print('son2的init结束被调用')
class Grandson(Son1,Son2):
    def __init__(self,name,age,gender):
        print('grandson的init开始被调用')
        super().__init__(name,age,gender)
        print('grandson的init结束被调用')
gs=Grandson('浩然',18,'男')
print(gs.name)
print(gs.age)
print(gs.gender)
print(Grandson.__mro__)
