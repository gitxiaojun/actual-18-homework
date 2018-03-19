#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!shenjie :2018/3/19 11:43
#!@Auther :shenjie
#!@file: 乘法口诀.py
# 打印乘法口诀
# 提示：尝试print(‘kk’)与print(‘kk’, end=‘’)的区别
for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print('%s*%s=%s ' %(j,i,j*i),end='') #end=''表示结果写在一行
    print() #循环完打印一个空格，换行