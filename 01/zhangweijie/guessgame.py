# encoding: utf-8
# author: niko.zhang

import random
count = 1
random_num = random.randint(0,100)
guess_num = int(input('Please in put a number between 0-100: '))

while True:
    if guess_num < 0 or guess_num > 100:
        guess_num = int(input('Warning!!Please in put a number between 0-100: '))
        continue
    else:
        while count < 5:
            if guess_num == random_num:
                print('猜对了')
                break
            if guess_num != random_num:
                if guess_num > random_num:
                    print('猜大了')
                    guess_num = int(input('Please in put a number between 0-100: '))
                else:
                    print('猜小了')
                    guess_num = int(input('Please in put a number between 0-100: '))
            count += 1
    print('太笨了，下次再来')
    break
