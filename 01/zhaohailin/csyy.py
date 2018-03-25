# /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018/3/22 16:19
# @Software: PyCharm
# @Version : V1.0.0
# @File    : csyy.py

# 1、输入数字，并判断是否为数字
# 2、输入数字 < 随机数 打印 小
# 3、输入数字 > 随机数 打印 大
# 4、输入数字 = 随机数 打印 猜对，exti
# 5、最多猜5次，如5次失败 打印 太笨了，下次再来，exit

import random
random_num = int(random.randint(0, 100))

n = 1

while n <= 5:
	num = int(input('Plaease input number: '))
	if num < random_num:
		print('猜小了', random_num)
	elif num > random_num:
		print('猜大了', random_num)
	elif num == random_num:
		print('猜对了', random_num)
		break
	n += 1
else:
	print ( '太笨了，下次再来' )


