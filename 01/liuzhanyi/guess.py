#!/usr/bin/env python
# -*- coding: utf-8 -*-
#随机生成一个0到100的数字，提示用户在控制台上输入一个数字
#当用户输入数字小于生成的随机数，则打印猜小了
#当用户输入数字大于生成的随机数，则打印猜大了
#当用户输入数字等于生成的随机数，则打印猜对了，结束程序
#用户最可猜测5次，如果5次都错误，则打印“太笨了，下次再来”，并结束程序
import random
random_num = random.randint(0,100)

conut = 0

while True:
    conut_num = 5
    conut_num -= conut
    guess_num = input('你有5次猜的机会，剩余次数为' + str(conut_num) + '请输入你要猜的数字:')
    guess_num = int(guess_num)
    if guess_num == random_num:
        print('你真的太厉害了，猜对了')
        break
    elif guess_num < random_num:
        print('你猜的小了可以再大点')
    elif guess_num > random_num:
        print('你猜的大了，可以小一点')
    conut += 1
    if conut == 5:
        print('太笨了下次再来')
        break