# encoding: utf-8
"""
@file: game.py
@time: 2018/3/19/0019 12:44
"""
import random

random_num = random.randint(0, 100)
input_text = int(input('来猜个数吧，5次机会，在控制台输入个0-100之间的整数：'))
count = 1
while True:
    if input_text == random_num:
        print('猜对了')
        break
    elif input_text > random_num:
        print('猜大了,你已经猜了' + str(count) + '次，再猜：')
    else:
        print('猜小了,你已经猜了' + str(count) + '次，再猜：')
    input_text = int(input())
    count += 1
    if count == 5:
        print('太笨了，下次再来')
        break
