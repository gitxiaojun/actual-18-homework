# -*- coding: utf-8 -*-
'''
@Time    : 2018/3/19 10:49
@Author  : Xiaopf
@Email   : xiaopf@aukeys.com
@File    : 02-猜数字游戏.py
'''

'''
随机生成一个0到100的数字，提示用户在控制台上输入一个数字
当用户输入数字小于生成的随机数，则打印猜小了
当用户输入数字大于生成的随机数，则打印猜大了
当用户输入数字等于生成的随机数，则打印猜对了，结束程序
用户最多可猜测5次，如果5次都错误，则打印“太笨了，下次再来”，并结束程序
'''

import random
random_num = random.randint(0,100)

input_val = ''
while True:
    # 设置格式 1开始游戏  2退出游戏
    width = 30
    val_width = 10
    format = '%-*s%*s'
    print('=' * (width + val_width))
    print(format % (width - val_width, '猜数字(1-100)游戏说明', val_width, '选项'))
    print('-' * (width + val_width))
    print(format % (width - val_width, '开始游戏', val_width + 3, '1'))
    print(format % (width - val_width, '退出游戏', val_width + 3, '2'))
    print('=' * (width + val_width))
    input_val = input('请输入选项 >>: ').strip()

    # print(random_num)
    if input_val == '1':
        minnum = 0
        maxnum = 100
        count = 5
        # 尝试次数大于5次退出游戏
        while count != 0:
             input_num = input("猜数字 >>: ").strip()
             if input_num.isdigit():
                 input_num = int(input_num)
                 if input_num == random_num:
                     exit(print('Bingo~~ 猜对了,答案是: %d' % input_num))
                 elif input_num > random_num:
                     maxnum = input_num
                     count -= 1
                     print('猜大了,你猜的数字是: %d,剩余次数: %d, 区间：%d ~ %d' % (input_num,count,minnum,maxnum))
                     continue
                 else:
                     minnum = input_num
                     count -= 1
                     print('猜小了,你猜的数字是: %d,剩余次数: %d, 区间：%d ~ %d' % (input_num,count,minnum,maxnum))
                     continue
             else:
                 print('--- 请输入一个数字 ---')

        print('\n--- 太笨了,下次再来！答案是 >>：%d\n' % (random_num))

    elif input_val == '2':
        print('--- 游戏结束 ---')
        break
    else:
        print('\n--- 输入错误 请重新选择 ---\n')
        continue


