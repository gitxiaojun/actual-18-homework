#!/usr/bin/env python
#encoding: utf-8

Mylist = [49,38,65,97,76,13,27,49]

for i in range(len(Mylist) -1):
    for j in range(len(Mylist) -1):
        if Mylist[j] > Mylist[j+1]: #判断大小
            Mylist[j],Mylist[j+1] = Mylist[j+1],Mylist[j] #排序换位
print(Mylist)

