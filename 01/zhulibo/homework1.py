#encoding: utf-8
# 输出9*9乘法表

print('----------------- 9*9乘法表 --------------------')

i = 1
j = 1

while i<=9:

    while j <= i:

        print(str(j) + ' * ' + str(i) + ' = ' + str(j*i), end='  ')

        if i == j:
            print('\r\n')

        j += 1

    j = 1
    i += 1





