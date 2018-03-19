#!/bin/bin/env python3
# -*- coding: utf-8 -*-
# __auhtor__: will_xue
# Date: 2018-03-20
# Email: xuegqcto@aliyun.com

# 猜数比对随机数

import random
random_num = random.randint(0, 100)
print(random_num)

n = 1
while n <= 5:
    print('本次获取的随机数是:', random_num)
    num = int(input('请输入一个数字:'))
    if num < random_num:
        print('抱歉，猜小了')
    elif num > random_num:
        print('抱歉，猜大')
    elif num == random_num:
        print('恭喜您，猜对了，谢谢')
        break
    n = n + 1
else:
    print('太笨了，下次再来')
