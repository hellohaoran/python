# 作者: 张浩然
# 2022年06月08日09时19分29秒
class animal:
    def __init__(self,name):
        self.name = name
    def move(self):
        print("i can move...")
    def sleep(self):
        print("i can sleep...")
class Dog(animal):
    def bark(self):
        print("汪汪。。")
    def run(self):
        print("我会跑")
class Bird(animal):
    def fly(self):
        print("我会飞。。")
class SunWuKong(Dog,Bird):
    def __init__(self):
        super().fly()
        super().run()
    def __str__(self):
        return "我有七十二般变化！"


sunwukong = SunWuKong()
sunwukong.sleep()
sunwukong.bark()
