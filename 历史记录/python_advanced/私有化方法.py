# 作者: 张浩然
# 2022年06月22日19时06分00秒
class _Bug():
    @staticmethod
    def showbug():
        print('showbug')
class Person(object):
    def __init__(self,name,age,taste):
        self.name=name
        self._age=age
        self.__taste=taste
    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)
    def dowork(self):
        self._work()
        self.__away()
    def _work(self):
        print('my _work')
    def __away(self):
        print('my __away')
class Student(Person):
    def __init__(self,name,age,taste):
        self.name=name
        self._age=age
        self.__taste=taste# 重写父类属性
    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)
    @staticmethod
    def testbug():
        _Bug.showbug()
s=Student('浩然',18,'好')
# 另个函数也可以起init的作用
s.showstudent() #没有初始
s.testbug()

s.showstudent()
