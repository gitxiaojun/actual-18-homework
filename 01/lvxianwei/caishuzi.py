import random
random_num=random.randint(0,100)
times=1
while times<=10:
    guess_num=int(input("请输入一个猜测数字(0-100内整数）："))
    if guess_num<random_num:
        print("猜小了，","还剩",10-times,"机会")
    elif guess_num>random_num:
        print("猜大了，","还剩",10-times,"机会")
    else:
        print("bingo！恭喜你，答对了")
        exit()
    times+=1
print("太笨了，下次再来")