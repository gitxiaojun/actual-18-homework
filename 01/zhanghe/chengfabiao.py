#!/usr/bin/env python3
# coding: utf-8

# 方法1
i = 1

while i <= 9:
    j = 1
    while j <= i:
        print('%s x %s = %s' % (j, i, j * i), end='\t')
        j += 1
    i += 1
    print()


'''
# 方法2
for i in range(1, 10):
    for j in range(1, i+1):
        print('%s x %s = %s' % (j, i, j * i), end='\t')

    print()
'''
