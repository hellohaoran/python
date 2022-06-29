# 作者: 张浩然
# 2022年06月19日17时29分23秒
from multiprocessing import  Queue
q=Queue(3)#初始化一个三个元素的队列
q.put('1')
q.put('2')
q.put('3')
try:
    q.put('5',True)

except Exception as e :
    print('现在队列已经%d'%q.qsize())
    # print(e)
