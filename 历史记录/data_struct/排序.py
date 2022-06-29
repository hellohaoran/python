# 作者: 张浩然
# 2022年06月10日21时29分58秒



class Sort:
    def __init__(self, num, range_value):
        self.arr = [0] * num
        self.num = num
        self.help_arr = [0] * num
        self.range_value = range_value

    def create_arr(self):
        for i in range(self.num):
            self.arr[i] = random.randint(0, self.range_value)

    def Bubble(self):
        arr = self.arr
        i = self.num - 1
        while i > 0:
            j = 0
            while j < i:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j += 1
            i -= 1

    def Select(self):
        arr = self.arr
        i = 0
        while i < self.num - 1:
            min_ = i
            j = i + 1
            while j < self.num:
                if arr[min_] > arr[j]:
                    min_ = j
                j += 1
            arr[i], arr[min_] = arr[min_], arr[i]
            i += 1

    def insert(self):
        arr = self.arr
        i = 1
        while i < self.num:
            j = i - 1
            temp = arr[i]
            while j >= 0:
                if temp < arr[j]:  # 传递到temp>=arr[j]时就退出
                    arr[j + 1] = arr[j]
                    j -= 1
                else:
                    break
            arr[j + 1] = temp
            i += 1

    def hash_(self):
        arr = self.arr
        gap = self.num >> 1
        while gap > 0:
            i = gap
            while i < self.num:
                j = i - gap
                temp = arr[i]
                while j >= 0:
                    if temp < arr[j]:  # 传递到temp>=arr[j]时就退出
                        arr[j + gap] = arr[j]
                        j -= gap
                    else:
                        break
                arr[j + gap] = temp
                i += gap
            gap = gap >> 1

    def partition(self, left, right):  # 确定分界基准的
        arr = self.arr
        k = left
        pivot = right
        for i in range(left, right):
            if arr[i] < arr[pivot]:
                arr[k], arr[i] = arr[i], arr[k]
                k += 1
        arr[k], arr[pivot] = arr[pivot], arr[k]
        return k

    def quick_sort(self, left, right):  # 递归进行快排，

        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def adjust_heap(self, head, len):  # 因为除了创造大根堆还要进行排序所以要传递len
        arr = self.arr
        dad = head
        son = dad * 2 + 1  # 左叶子节点
        while son < len:
            if son + 1 <= len - 1 and arr[son] < arr[son + 1]:
                son = son + 1
            if arr[son] > arr[dad]:
                arr[son], arr[dad] = arr[dad], arr[son]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap(self):
        arr = self.arr
        for i in range(self.num // 2 - 1, -1, -1):
            self.adjust_heap(i, self.num)  # 建堆
        arr[0], arr[self.num - 1] = arr[self.num - 1], arr[0]
        for i in range(self.num - 2, 0, -1):  # 利用大根堆排序
            self.adjust_heap(0, i + 1)
            arr[0], arr[i] = arr[i], arr[0]

    def merge_sort(self, left, mid, right):
        arr = self.arr
        help_arr = self.help_arr
        for i in range(self.num):
            help_arr[i] = arr[i]
        i = left
        j = mid + 1
        k = left
        while i <= mid and j <= right:
            if help_arr[i] < help_arr[j]:
                arr[k] = help_arr[i]
                k += 1
                i += 1
            else:
                arr[k] = help_arr[j]
                k += 1
                j += 1
        while i <= mid:
            arr[k] = help_arr[i]
            k += 1
            i += 1
        while j <= right:
            arr[k] = help_arr[j]
            k += 1
            j += 1

    def merge(self, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge(left, mid)
            self.merge(mid + 1, right)
            self.merge_sort(left, mid, right)

    def count(self):
        count_arr = [0] * (self.range_value+1)
        arr = self.arr
        for i in arr:
            count_arr[i] += 1  # 统计数组中各值的个数
        k = 0
        for i in range(0, self.range_value + 1):
            for j in range(0, count_arr[i]):
                arr[k] = i
                k += 1


















if __name__ == '__main__':
    s = Sort(10000,100)
    s.create_arr()
    print(s.arr)
    # s.Bubble()
    # s.Select()
    # s.insert()
    # s.hash_()
    # s.quick_sort(0, 10 - 1)
    # s.merge(0,s.num-1)
    # s.heap()
    s.count()
    print(s.arr)
