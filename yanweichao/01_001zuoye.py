#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:YGxchao

x = 1

while x <= 9:
    y = 1
    while y <= x:
        print(str(y), '*', str(x), '=', str(x * y), end='\t')
        y += 1
    print()
    x += 1
