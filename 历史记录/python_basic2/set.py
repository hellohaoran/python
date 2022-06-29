# 作者: 张浩然
# 2022年06月06日15时45分42秒
x = {"orange","banana","oppo","apple"}
print(id(x))
y = {"google","apple","microsoft"}
print(id(y))
# x.difference_update(y)
# print(id(x))
# y.difference_update(x)
# print(id(y))
x.difference(y)# 返回一个新集合给x
print(id(x))
y.difference(x)
print(id(y))
s= "string lokd king people"
s.strip(" ")
print(s)