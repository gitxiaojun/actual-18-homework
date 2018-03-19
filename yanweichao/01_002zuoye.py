#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:YGxchao

# 随机数字游戏
import random

count = 1
random_nums= random.randint(0,100)
you_input = int(input('请输入0-100的数字\n看看是否能猜中电脑随机输出的数字：'))
while you_input != random_nums and count <=4:
        if you_input > random_nums:
            print('你第%d次输入的数字大于电脑随机数！！'%count)
            you_input = int(input('您可以在再次尝试：'))
        else:
            print('你第%d次输入的数字小于电脑随机数！！'%count)
            you_input = int(input('您可以在再次尝试：'))
        count += 1
        if count == 5 and you_input != random_nums :
            print('你太笨了，这都猜不出来！！！')
if you_input == random_nums:
    print('恭喜您，您的输入与电脑随机数相符')


