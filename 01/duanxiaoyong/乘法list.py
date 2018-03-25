# /usr/bin/env python
# -*- coding: utf-8 -*-
# auth: duanxiaoyong

#方法1
x = 0
while x <9:
    x += 1
    # print(x)
    y=0
    # print(y)
    while y < x:
        y += 1
        print("%d*%d=%2d" % (x,y,x*y),end=" ")
    print('\n')

# 方法2
for i in range(1,10):
    #print(i)
    for j in range(1,i+1):
        #print(j)
        print("%d*%d=%2d" % (i, j, i * j), end=" ")
    print(" ")

