# -*- coding: utf-8 -*-
'''
@Time    : 2018/3/28 18:55
@Author  : Xiaopf
@Email   : xiaopf@aukeys.com
@File    : 01-插入排序.py
'''

'''
# 插入排序 1
nums = [6,11,7,9,4,2,1]
i = len(nums)

for a in range(i):
    for b in range(i-1):
        if nums[a] < nums[b]:   # 后一个值与前一个值循环比较
            nums[a],nums[b] = nums[b],nums[a] # 若后一个值大于前一个值，则调换位置
print(nums)
'''


'''
# 插入排序 2
# alist = [54,26,93,17,77,31,44,55,20]
'''
def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index] # 1 26  # 当前需要排序的元素
        position = index # 1 26  # 用来记录排序的值插入的位置

        while position>0 and alist[position-1] > currentvalue: #54 > 26  # 如果当前值比前一个值小条件成立  直到条件不成立跳出循环
            alist[position] =  alist[position-1] # 调换位置 26 54
            position = position-1 # 0 # 继续与下一个值比较 直到条件不成立

        alist[position] = currentvalue # alist[0] = 26  # 插入到指定位置

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)