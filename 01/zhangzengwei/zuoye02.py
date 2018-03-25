#encoding: utf-8


import random

number = random.randint(0,100)

print('随机数为:',number)
count=0

while  True:
	guess = int(input('请输入数字:'))
#while  guess != number and count <5:
	if guess > number and count <5:
		print('大了')
	elif guess < number and count <5:
		print('小了')
	
	count = count +1
	if guess == number :
		print('bingo,over!!!!!!')
		break
	if count == 5:
		print('you stuped,MDZZ')
		break






