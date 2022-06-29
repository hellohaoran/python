# 作者: 张浩然
# 2022年06月10日10时43分59秒
class circle_queue:
    def __init__(self):
        self.max_size = 10
        self.arr = [0] * self.max_size
        self.front = 0
        self.rear = 0

    def enqueue(self, num):
        arr = self.arr

        if (self.rear + 1) == self.front:
            print("队列已满！")
        arr[self.rear] = num
        self.rear = (self.rear + 1) % self.max_size

    def dequeue(self):
        arr = self.arr
        if self.rear == self.front:
            print("队列已空！")
        re = arr[self.front]
        arr[self.front] = 0
        self.front = (self.front + 1) % self.max_size
        return re


if __name__ == '__main__':
    s = circle_queue()
    s.enqueue(7)
    s.enqueue(8)
    s.enqueue(9)
    s.enqueue(10)
    print( s.dequeue())
    s.dequeue()
    s.dequeue()
    s.dequeue()
    print(s.arr)
