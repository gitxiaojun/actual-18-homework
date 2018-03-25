#!/usr/bin/env python
# -*- coding: utf-8 -*-

# #方法一
x = 0
y = 0
while x < 9:
    x += 1
#    y = 0
    while y < x:
        y += 1
        print(x, '*', y, '=', x * y,end=' ')
        # if x == y:
        #     break
    y = 0
    print('')

#方法二
# x = 0
# while x <9:
#     x += 1
#     # print(x)
#     y=0
#     # print(y)
#     while y < x:
#         y += 1
#         print("%d*%d=%2d" % (x,y,x*y),end=" ")
#     print('')