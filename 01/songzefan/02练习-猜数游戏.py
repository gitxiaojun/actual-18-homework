#/usr/bin/env python
# -*- coding: utf-8 -*-
# auth: songzefan
# time: 2018-03-18

import random
random_num = random.randint(0,10) 

input_times = 5

while True:
    input_num = int(input("请输入您猜的数字："))
    input_times -= 1
    if input_num < random_num:
        print("猜小了！")
    if input_num > random_num:
        print("猜大了！")
    if input_num == random_num:
        print("猜对了！")
        break
    if input_times == 0: 
        print("太笨了，下次再来")
        break
