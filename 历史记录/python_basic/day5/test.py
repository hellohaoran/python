# 作者: 张浩然
# 2022年06月05日18时10分31秒
# 下列代码证明，不可变类型，内存中的数据不可更改，即变量存的是数字、字母的地址
num = 25
print(id(num))
num = 15
print(id(num))
num = 25
print(id(num))
s = "hello"
print(id(s))
s = "hellol"
print(id(s))
t = (1,)
print(id(t))
t = (1,2)
print(id(t))
'''下列代码证明
可变数据类型，内存中的数据可以被修改,即修改数据变量存储的地址不会改变

'''
l = [7,89,5]
print("改变数据前的l的id为%d"%id(l))
l.append(6)
print(l)
print("改变数据后的l的id为%d"%id(l))
d = {"kin":75,"lo":85}
print("改变数据前的d的id为%d"%id(d))
d["jn"] = 85
print("改变数据后的d的id为%d"%id(d))
se = set()
print("改变数据前的se的id为%d"%id(se))
se.add(75)
print("改变数据后的se的id为%d"%id(se))
print(se)


