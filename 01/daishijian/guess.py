#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/3/19 15:02
# @Author : David Beckham
# @File   : guess.py
import random
secret=random.randint(1,100)#生成随机数
#print (secret)
time=5#猜数字的次数
guess=0#输入的数字
minNum=0#最小随机数
maxNum=100#最大随机数
print("---------欢迎来到猜数字游戏，请开始---------")
while guess!=secret and time>0:#条件
    guess=int(input("*数字区间0-100，请输入你猜的数字:"))
    print("你输入数字是：",guess)
    if guess==secret:
        print("猜对了")
        break
    else:
        #当不等于的时候，还需要打印出相应的数字区间，让用户更容易猜到，增加可玩性
        if guess<secret:
            minNum=guess
            print("猜小了")
            print("现在的数字区间是：",minNum,"-",maxNum)
        else:
            maxNum=guess
            print("猜大了")
            print("数字区间是：",minNum,"-",maxNum)
        time -= 1
        print("你猜错了，你还有",time,"次机会")

print("太笨了,下次再来")
