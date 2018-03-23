# encoding: utf-8 
import random 
random_num = random.randint(0,100)
x = input('请输入数字,还有5次机会:')
z = 5
i = 1
while i <= 4: 
    if int(x) < random_num:
        i += 1 
        z -= 1
        print('数字猜小了,你还有',z,'次机会')
        x = input('请再输入数字:')
    if int(x) > random_num:
        i +=1 
        z -= 1
        print('数字猜大了,你还有',z,'次机会')
        x = input('请再输入数字:')
    if int(x) == random_num:
        print('你太聪明了，用了',i,'次猜对了')
        break
    if  i == 5: 
        print('5次机会用完，你都没有猜对,Byebye!')
        break
