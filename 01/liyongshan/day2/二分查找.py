#!/usr/bin/env python3

# -*- coding: utf-8 -*-


nums = [3, 5, 6, 7, 9, 10, 11, 12, 13, 17, 20, 26, 37, 49, 56, 66, 74, 88, 99, 100]
num = int(input("请输入查找的数字:"))

low = 0
high = len(nums)-1
while low <= high:
    mid = (low+high)//2
    if nums[mid] == num:
        print("您要找的数字下标为%s" % mid)
        break
    elif nums[mid] > num:
        high = mid - 1
    elif nums[mid] < num:
        low = mid + 1
    else:
        print("找不到这个数字")
        break
