#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!shenjie :2018/3/19 11:47
#!@Auther :shenjie
#!@file: 猜数游戏.py
# 随机生成一个0到100的数字，提示用户在控制台上输入一个数字
# 当用户输入数字小于生成的随机数，则打印猜小了
# 当用户输入数字大于生成的随机数，则打印猜大了
# 当用户输入数字等于生成的随机数，则打印猜对了，结束程序
# 用户最可猜测5次，如果5次都错误，则打印“太笨了，下次再来”，并结束程序
# 提示：生成随机数的方法
import random
random_num=random.randint(0,100)
guess_count=0
while True:
    num=input('请猜数字：')
    guess_count+=1
    for i in num:
        if not i.isdigit():
            print('请重新执行，必须是数字')
            exit()
    if int(num) < random_num:
        print('%s < %s ,猜小了' %(int(num),random_num))
    elif int(num) > random_num:
        print('%s > %s ,猜大了' % (int(num), random_num))
    else:
        print('%s = %s, 猜对了，结束程序' %(int(num), random_num))
        break
    if guess_count >= 5:
        print("太笨了，下次再来")
        break
