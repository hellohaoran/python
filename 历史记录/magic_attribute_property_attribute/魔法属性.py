# 作者: 张浩然
# 2022年06月25日23时18分10秒
class Foo:
    '''
    I am Foo doc
    '''
    def __call__(self, *args, **kwargs):
        print('对象加括号调用的是我')
        print(args)
        print(kwargs)
print(Foo.__doc__)
obj=Foo()
obj('王道')

class Province:
    country='中国'
    def __init__(self,name,count):
        self.name=name
        self.count=count
    def func(self,*args):
        print('func')
print(Province.__dict__)# 获取类的属性，即：类属性、方法
obj=Province('台湾',3000)
print(obj.__dict__)# 获取对象obj的属性

print('-'*50)
print('对象使用列表的操作实现,即__item__方法')
class Foo(object):
    def __getitem__(self,key):
        print('__getitem__',key)
    def __setitem__(self,key,value):
        print('__setitem__',key,value)
    def __delitem__(self, key):
        print('__delitem__',key)

obj = Foo()

result= obj['k1']
obj['k2']='laozhang'
del obj['k1']
