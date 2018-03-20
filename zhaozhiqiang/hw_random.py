#Don't know how to tell characters
import random
random_num = random.randint(0,100)
v_time = 0
while True:
        usernum = input('Please input a 0-100 number:')
        while True:
                if usernum == '':
                        print('Invalid input,must input!')
                        usernum = input('Please input a 0-100 number:')
                elif int(usernum)<0 or int(usernum)>100:
                        print('Invalid input,out of range!')
                        usernum = input('Please input a 0-100 number:')
                else:
                        user_num = int(usernum)
                        break
        if user_num < random_num:
                print('What you guessed is less.')
        elif user_num > random_num:
                print('What you guessed is more.')
        else:
                print('Bingo!')
                break
        v_time += 1
        if v_time == 5:
                print('You idiot! Again!')
                break
		

