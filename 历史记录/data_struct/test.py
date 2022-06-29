# 作者: 张浩然
# 2022年06月14日13时38分09秒
import random
import sys


class Search:
    def __init__(self,arr):
        self.arr = arr

    def bsearch( self,target):
        arr = self.arr
        high = len(arr) - 1
        low = 0
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] > target:
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1
    def bit_map(self):
        arr=self.arr
        result = []
        tem =0
        for i in arr:
            if not tem&1<<i: # 若 tem&1《《i是1说明i出现过，跳出if判断
                result.append(i)
                tem |= 1<<i# tem存的都出现过的数
        return result
    def elf_harsh(self,hash_str,Maxsize):
            h = 0
            g = 0
            for i in hash_str:
                h = (h << 4) + ord(i)
                g = h & 0xf0000000
                if g:
                    h ^= g >> 24
                h &= ~g
            return h % Maxsize

    def harsh(self):
        Maxsize = 1000
        harsh_table=[None]*Maxsize
        str_dict=['string',"eminem",'family','people']

        for i in str_dict:
            harsh_table[self.elf_harsh(i,Maxsize)]=i
        return harsh_table



class Sort:
    def __init__(self, num, value_range):
        self.num = num
        self.value_range = value_range
        self.arr = [random.randint(1, value_range) for i in range(num)]

    def partion(self, low, high):
        arr = self.arr
        part_value = arr[high]
        k = low
        i = low
        for i in range(low, high):
            if arr[i] < part_value:
                arr[k],arr[i]=arr[i],arr[k]
                k+=1
        arr[k],arr[high]=arr[high],arr[k]
        return k

    def quick_sort(self, low, high):
        arr = self.arr
        if low < high:

            pivot = self.partion(low,high)
            self.quick_sort(low, pivot - 1)
            self.quick_sort(pivot+1, high)



if __name__ == '__main__':
    s = Sort(100, 100)
    print(s.arr)
    s.quick_sort(0,99)
    print(s.arr)
    ser = Search(s.arr)
    print(ser.bsearch(16))
    print(ser.harsh())
    print(ser.harsh().index("string"))

