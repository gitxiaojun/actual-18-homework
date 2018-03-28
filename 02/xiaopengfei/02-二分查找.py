# -*- coding: utf-8 -*-
'''
@Time    : 2018/3/28 18:57
@Author  : Xiaopf
@Email   : xiaopf@aukeys.com
@File    : 02-二分查找.py
'''


# 二分查找

nums_1 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
find = int(input('number >>:'))

low = 0
high = len(nums_1)-1  # 高位
flag = False

while low <= high and not flag:
    mid = (high+low)//2  # 取中间值的索引

    if find == nums_1[mid]:
        flag = True
        print('You got it {0}'.format(nums_1[mid]))
    else:
        if find < nums_1[mid]:
            high = mid-1  # 重新定义高值
        else:
            low = mid+1  # 重新定义低至

if not flag:
    print('not found')

