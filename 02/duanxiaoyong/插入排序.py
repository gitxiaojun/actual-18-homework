# /usr/bin/env python3
# -*- coding: utf-8 -*-
# auth: duanxiaoyong

Number_list = [1,3,11,22,14,33,54]
#遍历的次数
for i in range(len(Number_list)-1):
    #这个循环负责设置冒泡排序进行的次数
    for j in range(len(Number_list) - i - 1):
        if Number_list[j] > Number_list[j + 1]:
            Number_list[j], Number_list[j + 1] = Number_list[j + 1], Number_list[j]

print(Number_list)

