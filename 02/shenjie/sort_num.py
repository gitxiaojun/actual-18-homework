#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!shenjie :2018/3/28 10:16
#!@Auther :shenjie
#!@file: sort_num.py


num=[1,23,234,12,3,4,576]

for i in range(len(num)):
    for j in range(len(num)-1):
        if num[j] > num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
print(num)