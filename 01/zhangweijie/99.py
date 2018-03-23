# encoding: utf-8
# author: niko.zhang

a = 1
b = 1
while a < 10:
    while b < 10:
        print('%sX%s=%s'%(a,b,a*b),end='\t')
        b += 1
    print('')
    b = a + 1
    a += 1