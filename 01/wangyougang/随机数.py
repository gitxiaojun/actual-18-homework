import random
random_num = random.randint(0,100)
j = 5
while True:
    i = int(input('输入一个数字: '))
    j -= 1
    if i < random_num:
        print('猜小了')
    if i > random_num:
        print('猜大了')
    if i == random_num:
        print('猜对了')
        break
    if j == 0:
        print('你太笨了，下次再来')
        break
