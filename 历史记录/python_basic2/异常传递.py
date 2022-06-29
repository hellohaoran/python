# 作者: 张浩然
# 2022年06月08日19时50分24秒
def demo1():
    s = int(input("请输入整数"))
    print("this is demo1")
    return s

def demo2():
    num =  demo1()
    print("this is demo2")
    return num


try:
    print("数字为：{}".format(demo2()))
except Exception as res:
    print("未知错误:{}".format(res))