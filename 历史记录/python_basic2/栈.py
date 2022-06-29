# 作者: 张浩然
# 2022年06月09日09时06分27秒
class Stack:
    def __init__(self):
        self.tack = []
    def push(self,ele):
        self.stack.append(ele)
    def pop(self):
        return self.stack.pop()
    def top(self):
        if self.empty():
            return "stack is empty"
        return self.stack[-1]
    def empty(self):
        return self.stack == []
    def size(self):
        return len(self.)