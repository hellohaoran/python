# 作者: 张浩然
# 2022年06月05日16时27分34秒
s = 7
print(id(s))
s = 5
print(id(s))
s = []
print("%d"%id(s))
def ko(s):
    for i in range(100):
        s.append(75+i)

    print(id(s))
ko(s)
num = 2
print("num的id=%d"%id(num))
def b(n):
    print(id(n))
    n = n + 2
    print(id(n))
    return n
n = b(num)
print(id(n))
def k():
    global num
    num = 10
    print(num)

k()