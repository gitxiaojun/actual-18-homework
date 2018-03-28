#!/usr/bin/env python
#encoding: utf-8

num = [5 , 13 , 19, 21, 37, 56, 64, 75, 80, 88, 92]

#设置开始数索引
low=0
#最大数索引
high=(len(num) -1)
#需要查找的值
val = 21

while True:
    min = (low+high) // 2
    if num[min] == val:
        print('索引为{0}'.format(min))
        break
    elif num[min] > val:
        high = min -1
    elif num[min] < val:
        low = min +1
