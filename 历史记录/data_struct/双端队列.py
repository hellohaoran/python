# 作者: 张浩然
# 2022年06月10日10时39分04秒
from collections import deque
queue = deque(["God","zhanghao",'haoran','张浩然'])
queue.append("kong")
queue.pop()
queue.pop()
queue.pop()
print(len(queue))
print(queue)
queue.pop()
queue.append("张浩然")
print(queue)
