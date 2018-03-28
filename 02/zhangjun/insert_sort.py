# encoding: utf-8
"""
@file: insert_sort.py
@time: 2018-03-29 1:04
"""
alist = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]

# insert_sort
for i in range(1, len(alist)):
    if alist[i - 1] > alist[i]:
        # 当前需要排序的元素
        temp = alist[i]
        # 记录排序元素需要插入的位置
        index = i
        while index > 0 and alist[index - 1] > temp:
            # 把已经排序好的元素后移一位，留下需要插入的位置
            alist[index] = alist[index - 1]
            index -= 1
            # 把需要排序的元素，插入到指定位置
            alist[index] = temp
print(alist)
