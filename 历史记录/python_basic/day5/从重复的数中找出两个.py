# 作者: 张浩然
# 2022年06月05日19时04分10秒
l = [3,4,5,9,12,3,4,5]
a = []
b = []
cat = 0
for i in l:
    cat ^= i
print(cat)
t = cat & (-cat)
print(t)
for k in l:
    f = t & k

    if f == 1:
        a.append(k)
    if f == 0:
        b.append(k)
print(a)
print(b)
cat1 = 0
cat2 = 0
for i in a:
    cat1 ^= i
for j in b:
    cat2 ^= j
print("两个数分别为：%d,%d"%(cat1,cat2))

