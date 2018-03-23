#!/bin/bin/env python3
# -*- coding: utf-8 -*-
# __auhtor__: will_xue
# Date: 2018-03-18
# Email: xuegqcto@aliyun.com

'''
打印乘法口诀
提示：尝试print('kk’)与print('kk’, end=‘’)的区别

print('kk')  # 打印结果，并换行
print('kk', end=' ')  # 打印结果，不换行
'''

# 定义外循环值
i = 1
while i <= 9:
    #定义内循环，保持每次 j 初值为1
    j = 1
    while j <= i:
        print(str(j) + '*' + str(i) + '=' + str(j * i), end=' ')
        j = j + 1
    print( )
    i = i + 1
