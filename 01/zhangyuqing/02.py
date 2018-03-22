#coding: utf8

import random
random_num = random.randint(0,100)
count = 0

while count <= 5:
	www = int(input('输入一个数字:'))
	if www == random_num:
		print('猜对了')
		break
	if www < random_num:
		print('猜小了')
		count += 1
	if www > random_num:
		print('猜大了')
		count += 1
else:
    print('"太笨了，下次再来"')
