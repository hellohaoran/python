# 作者: 张浩然
# 2022年06月22日20时59分22秒
class Animal:
    def eat(self):
        pass
    def action(self):
        pass
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
    def action(self):
        print('猫叫喵喵')
class Dog(Animal):
    def eat(self):
        print('狗吃肉')
    def action(self):
        print('狗叫旺旺')
class factory_mode:
    dict1={'dog':Dog,'cat':Cat}
    def creat_animal(self,name):
        return factory_mode.dict1[name]()
f= factory_mode()
cat = f.creat_animal('cat')
cat.eat()
