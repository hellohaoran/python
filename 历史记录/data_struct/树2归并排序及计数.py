# 作者: 张浩然
# 2022年06月12日08时39分35秒
import random


class node:
    def __init__(self, elem=-1, lchild=None, rchild=None):  # 节点类，对象属性的定义
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    def __init__(self):
        self.root = None
        self.queue = []

    def create_tree(self, elem):
        queue = self.queue
        new_node = node(elem)
        queue.append(new_node)  # 新结点入队
        if self.root is None:  # 根据入队结点建树
            self.root = new_node

        elif queue[0].lchild is None:
            queue[0].lchild = new_node
        elif queue[0].rchild is None:
            queue[0].rchild = new_node
            queue.pop(0)

    def preorder(self, node):
        if node:
            print(node.elem, end="")
            self.preorder(node.lchild)
            self.preorder(node.rchild)

    def midorde(self, node):
        if node:
            self.midorde(node.lchild)
            print(node.elem, end="")
            self.midorde(node.rchild)

    def postorder(self, node):
        if node:
            self.postorder(node.lchild)
            self.postorder(node.rchild)
            print(node.elem, end="")


class Sort:
    def __init__(self, num, range_value):
        self.num = num
        self.range_value = range_value
        self.arr = [random.randint(0, range_value) for i in range(num)]
        self.help_arr = [0] * num

    def merge_sort(self, left, mid, right):# 用在外面的数组进行归并，切成两半，两半分别进行比较
        for i in range(self.num):
            self.help_arr[i] = self.arr[i]
        k = left
        i = left
        j = mid + 1
        help_arr = self.help_arr
        arr = self.arr
        while i <= mid and j <= right:
            if help_arr[i] < help_arr[j]:
                arr[k] = help_arr[i]
                i += 1
            else:
                arr[k] = help_arr[j]
                j += 1
            k += 1
        while i <= mid:
            arr[k] = help_arr[i]
            k += 1
            i += 1
        while j <= right:
            arr[k] = help_arr[j]
            k += 1
            j += 1

    def merge(self, left, right):# 递归的进行归并排序，
        if left < right:
            mid = (left + right) // 2
            self.merge(left, mid)
            self.merge(mid + 1, right)
            self.merge_sort(left, mid, right)

    def count(self):# 计数把数组根据值的范围出现的个数统计在count数组中，再按照从小到达的值的范围和count数组进行排序
        arr = self.arr
        count = [0]*(self.range_value+1)
        for i in arr:
            count[i] +=1
        k=0
        for i in range(self.range_value+1):
            for j in range(count[i]):
                arr[k]=i
                k=k+1





if __name__ == '__main__':
    # tree = Tree()
    # for i in "abcdefghij":
    #     tree.create_tree(i)
    # tree.preorder(tree.root)
    # print()
    # tree.midorde(tree.root)
    # print()
    # tree.postorder(tree.root)
    arr = Sort(100000, 100)
    # arr.merge(0, 999)
    arr.count()
    print(arr.arr)
