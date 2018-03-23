#!/bin/bin/env python3
# -*- coding: utf-8 -*-
# __auhtor__: will_xue
# Date: 2018-03-20
# Email: xuegqcto@aliyun.com

'''
猜数游戏
随机生成一个0到100的数字，提示用户在控制台上输入一个数字
当用户输入数字小于生成的随机数，则打印猜小了
当用户输入数字大于生成的随机数，则打印猜大了
当用户输入数字等于生成的随机数，则打印猜对了，结束程序
用户最可猜测5次，如果5次都错误，则打印“太笨了，下次再来”，并结束程序
'''

# 生成一个随机数
import random
random_num = random.randint(0, 100)

n = 1

print('本次获取的随机数是:', random_num)
while n <= 5:
    num = int(input('请输入一个数字:'))
    if num < random_num:
        print('抱歉，猜小了'+ '还有%s 次机会，加油!' % ( 5 - n))
    elif num > random_num:
        print('抱歉，猜大了' + '还有%s 次机会，加油!' % (5 - n))
    elif num == random_num:
        print('恭喜您，猜对了，谢谢!')
        break
    n = n + 1
else:
    print('太笨了，下次再来')
