#coding: utf8
import random

count = 1

while count <= 5:
	count += 1
	random_int = random.randint(0,100)
	num = input('输入数字猜大小:')
	if int(num) < random_int:
		print('猜小了')
	elif int(num) > random_int:
		print('猜大了')
	elif int(num) == random_int:
		print('猜对了')
		break
else:
	print('太笨了,下次再来!')
