#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/3/19 14:03
# @Author : David Beckham
# @File   : chengfa.py
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(i,j,i*j),end='\t')
    print('')

