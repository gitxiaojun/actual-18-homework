# -*- coding:utf-8 -*-
# Author: Lizeyang
# 
import random

random_num = random.randint(0,100)
#random_num = 5

time = 0

def red(mes):
    print("\033[1;31;40m" + mes + "\033[0m")

def green(mes):
    print("\033[1;32;40m" + mes + "\033[0m")


while True:
    time += 1
    if time == 6:
        red("Game over ! Low!  ")
        break
    else:
        num = int(input('Please enter an number :  '))
        if num == random_num:
            green("Success: Your guess it .\nyou time is " + str(time))
            break 
        elif num < random_num:
            red("Error: Your guess num is "+ str(num) + " [smail]")
        elif num > random_num:
            red("Error: Your guess num is "+ str(num) + " [big]")

        

