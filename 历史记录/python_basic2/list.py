# 作者: 张浩然
# 2022年06月06日10时33分18秒

l = [7,89,"jind",8596,89,"jind",62]

l.insert(2,"king")# 在第二个索引位置增加数据，其后的数据往后退
print(l)
l.append("kon")#  在列表最后增加数据
print(l)
print(l[2])
del l[2]# 删除指定位置的数据
print(l)
l.remove("jind")# 删除第一个出现的数据
print(l)
l.pop(5)#删除某个索引的元素
print(l)
print(len(l))
print(l.count("jind"))
print(l.index("jind"))# 搜某个值的索引
'''
数字和字母杂糅可以先排序后反转的接口

'''
l.sort
print(l)
l.reverse()
print(l)
# l.sort(reverse = True) # 不能用数字和字母进行排序后翻转的接口
print(l)

print("*"*50)
k = [7,8,9,63,1,25,34,1]
print(id(l))
l += k
print(id(l)) #列表重载