# encoding: utf-8
# author: niko.zhang

import random
count = 1
random_num = random.randint(0,100)
while True:
    input_num = int(input('请输入一个范围在 0-100 的数字： '))
    while count < 5:
        if random_num == input_num:
            print('太棒了，你猜对了！')
            break
        if random_num > input_num:
            print('猜小了')
            input_num = int(input('请输入一个范围在 0-100 的数字： '))
            count += 1
            continue
        else:
            print('猜大了')
            input_num = int(input('请输入一个范围在 0-100 的数字： '))
            count += 1
            continue
    print('你太笨了，下次再来！')
    break