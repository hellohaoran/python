# 作者: 张浩然
# 2022年06月06日17时29分03秒
class Person:
    def __init__(self,name,height,weight,age = 7):

        self.name =name
        self.height = height
        self.weight = weight
        self.age = age
        print("%s 来了" % self.name)
    def eat(self):
        print( self.name + "can eat!")
    def run(self):
        print(self.name+"can run!")
        self.eat()
        print(self.age)
    def __str__(self):
        return self.name+str(self.height)+self.weight
    def __del__(self):
        print("%s 我去了" % self.name)
man =Person("浩然",1.65,"62kg")
man.eat()
man.run()
hero = Person("zhang",1.65,"62kg",75)
hero.run()
hero.age = 95
hero.run()
print(man)
del hero
