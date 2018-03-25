#!/usr/bin/env python3
# coding: utf-8

import random

max_times = 5
guess_times = 1
random_num = random.randint(0, 100)

while guess_times <= max_times:
    guess_num = int(input('Your guess number: '))
    if guess_num > random_num:
        print('猜大了')
        guess_times += 1
    elif guess_num < random_num:
        print('猜小了')
        guess_times += 1
    else:
        print('猜对了, 共猜了%s次' % guess_times)
        break
else:
    print('你太笨了，随机数是: %s' % random_num)
