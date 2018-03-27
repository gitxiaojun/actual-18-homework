#!/usr/bin/env python3

# -*- coding: utf-8 -*-


nums = [1, 2, 4, 7, 10, 12, 15,20]

print(nums)

num = int(input("Please input a num:"))

for i in range(len(nums)-1):
    if num < nums[i]:
        nums.insert(i, num)
        break
    elif num > nums[-1]:
        nums.append( num)
        break
    elif num > nums[i] and num <= nums[i+1]:
        nums.insert(i+1, num)
        break

print(nums)
