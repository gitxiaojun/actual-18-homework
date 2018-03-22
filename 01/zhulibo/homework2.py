#encoding: utf-8
#猜字游戏

import random

print('游戏开始！')

count = 5

while True:

    random_num = random.randint(1, 100)
    prompt = input('猜数字，请输入0~100间数字，或exit，退出游戏！ : ')

    if prompt == 'exit':
        print ('欢迎下次再来！')
        break

    count -= 1

    if count == 0:
        print ('你太笨了，下次再来吧！')
        break


    if(int(prompt) < random_num):
        print('你输入的数字太小了！')
        print('请重新输入，你还有'+ str(count) + '次机会!')
    elif (int(prompt) > random_num):
        print('你输入的数字太大了！')
        print('请重新输入，你还有'+ str(count) + '次机会!')
    else:
         print('恭喜您猜对了！')



