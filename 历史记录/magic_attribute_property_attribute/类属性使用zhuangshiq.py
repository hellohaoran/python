# 作者: 张浩然
# 2022年06月25日23时07分02秒
class Foo:
    '''
    I am Foo
    '''
    def get_bar(self):
        """
        I am a functin

        """
        return  'laowang'
    Bar = property(get_bar) # property 函数
obj=Foo()
print(obj.Bar)
print(Foo.__doc__) # 类的文档说明
print(obj.get_bar.__doc__)
print(object.__dict__)