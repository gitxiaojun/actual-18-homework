##猜数游戏：
# -*- coding:utf-8 -*-
import random
random_num = random.randint(0,100)
count = 0
user_num = input("please input a digit:")
while True:
    count += 1
    if count >5:
        print("太笨了，下次再来")
        break
    if int(user_num) < random_num:
        print("猜小了，继续...")
        user_num = input("please input a digit:")
    elif int(user_num) > random_num:
        print("猜大了，继续...")
        user_num = input("please input a digit:")
    elif int(user_num) == random_num:
        print("恭喜你，猜对了！！！")
        break