#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!shenjie :2018/3/27 9:34
#!@Auther :shenjie
#!@file: dichotomy.py
tmp=[5,13,19,21,37,56,64,75,80,88,92,100,101,199,1000,108,109,122]
tmp.sort()#对列表进行排序，列表是有序的，是二分法的前提
print(tmp)
#定义开始的索引
start=0
#定义结束的索引
end=int(len(tmp)-1)
find_num=input('请输入列表中要查找的数字：')
while True:
    #定义中间索引
    mid=(end+start)//2
    mid_num=tmp[mid]
    find_num=int(find_num)
    if find_num not in tmp:
        print('输入错误')
        break
    if find_num > mid_num:
        start=mid+1
    elif find_num < mid_num:
        end=mid
    else:
        print('查找的索引的值为:{0}'.format(mid))
        break
