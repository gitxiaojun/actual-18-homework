#coding=utf-8
#author:zhangchuan
#date:2018/03/20

import random
truenum=random.randint(0,100)
cnt=0
print ("猜数字游戏，你有五次机会")
while cnt<5:
    inputnum=int(input("请输入你猜的数字："))
    if inputnum == truenum:
        print ("恭喜你答对了，不过啥也没有")
        break
    elif inputnum > truenum:
        print ("大了")
        cnt += 1
        continue
    else:
        print ("小了")
        cnt += 1
        continue
    print ("已用完五次机会，笨蛋,正确数字是",truenum)
