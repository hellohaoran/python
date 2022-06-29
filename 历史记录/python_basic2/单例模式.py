# 作者: 张浩然
# 2022年06月08日17时54分02秒
class Video:
    instance = None
    init_flag = False
    def __new__(cls, *args, **kwargs): # 重写new方法
        if cls.instance == None:
            cls.instance = super().__new__(cls)# 将类分配给对象的地址传递给instance
            return cls.instance
        else:
            return cls.instance
    def __init__(self,name):
        if Video.init_flag == False:
            print("初始化播放器")
            Video.init_flag = True
    def __str__(self):
        return
s1 = Video("青花瓷")
s2 = Video("da")
print(s1 is s2)
del s1
del s2
print(Video)



