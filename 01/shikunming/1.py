#ecoding: utf-8

a = 1
b = 1

while a <= 9:
    while b <= a:
        print(str(b) + "*" + str(a) + "=" + str(a * b) + " ",end='')
        b += 1
    print('')
    a += 1 
    b = 1
