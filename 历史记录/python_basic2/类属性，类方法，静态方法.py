# 作者: 张浩然
# 2022年06月08日16时22分01秒
class Ufo:
    '''
    我是帮助！
    '''
    count = 0
    ufo_num = 101
    def __init__(self,name,location):
        self.name = name
        self.location = location
        Ufo.count += 1
    def __str__(self):
        return "这是%sUfo，来自%s"%(self.name,self.location)
    @classmethod
    def show_count(cls):
        print(cls.count)
    @classmethod
    def show_num(cls):
        cls.ufo_num += cls.count
        cls.show_count()
        print("飞船编号为%d"%cls.ufo_num)
    @staticmethod
    def help():
        print("这是一个找Ufo的说明文档")

ufo1 = Ufo("飞抵你","爱尔兰")
ufo2 = Ufo("近视眼","北京")
print(ufo1.__str__())
print(ufo2.__str__())
print(Ufo.show_num())
ufo2.help()



