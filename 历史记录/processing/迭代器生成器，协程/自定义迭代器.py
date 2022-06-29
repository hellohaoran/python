# 作者: 张浩然
# 2022年06月20日22时53分42秒
class MyIterator:
    def __init__(self,mylist):
        self.current=0
        self.mylist=mylist
        self.n= len(mylist.content)
    def __next__(self):# next指向下个元素，返回当前元素
        if self.current<self.n:
            item = self.mylist.content[self.current]
            self.current +=1
            return item

        else:
            raise StopIteration
    def __iter__(self):
        return self



class MyList:
    def __init__(self):
        self.content=[]
    def add(self,value):
        self.content.append(value)
    def __iter__(self): # 迭代器方法返回迭代器
        iterator=MyIterator(self)
        return iterator


if __name__ == '__main__':
    li=MyList()
    li.add(5)
    li.add(7)
    li.add(12)
    li.add(8)
    p=iter(li)
    print(next(p))
    for i in p:
        print(i)