import random
import datetime
numbers=[]
for i in range(50000000):
    j=random.randint(1,1000000)
    numbers.append(j)
start1=datetime.datetime.now()
sav=numbers
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)
res1=quicksort(numbers)
end1=datetime.datetime.now()
diff1=end1-start1
print("Скорость сортировки по-спидранерски:")
print(diff1)
numbers=sav
start2=datetime.datetime.now()
def fusionsort(nums): 
    if len(nums) > 1: 
        mid = len(nums)//2
        left = nums[:mid] 
        right = nums[mid:]
        fusionsort(left) 
        fusionsort(right) 
        i = j = k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                nums[k] = left[i] 
                i+=1
            else: 
                nums[k] = right[j] 
                j+=1
            k+=1
        while i < len(left): 
            nums[k] = left[i] 
            i+=1
            k+=1
        while j < len(right): 
            nums[k] = right[j] 
            j+=1
            k+=1
s2=fusionsort(numbers)
end2=datetime.datetime.now()
diff2=end2-start2
print("Скорость сортировки Фьюжоном:")
print(diff2)
numbers=sav
start3=datetime.datetime.now()
def heapsort(alist):
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)
 
def parent(i):
    return (i - 1)//2
 
def left(i):
    return 2*i + 1
 
def right(i):
    return 2*i + 2
 
def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1
 
def max_heapify(alist, index, size):
    l = left(index)
    r = right(index)
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)
 
 
alist = numbers
res3=heapsort(alist)
end3=datetime.datetime.now()
diff3=end3-start3
print("Скорость Египетской силы:")
print(diff3)
