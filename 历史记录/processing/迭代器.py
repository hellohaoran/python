# 作者: 张浩然
# 2022年06月20日21时40分07秒
from collections.abc import Iterator,Iterable
l=[]
t=tuple()
print(t)
dic={}
s=set()
print(isinstance(l,Iterable))
print(isinstance(l,Iterator))
print(isinstance(t,Iterable))
print(isinstance(t,Iterator))
print(isinstance(dic,Iterable))
print(isinstance(dic,Iterator))
print(isinstance(s,Iterable))
print(isinstance(s,Iterator))