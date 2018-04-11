number = 50
count = 0
while count <3:
    aaa = int(input("请输入你要猜的数字："))
    if number == aaa:
        print("恭喜你，猜对啦！！！")
        break
    elif number > aaa:
            print("猜的有点小了，你再猜大点。。。。")
    else:
            print("猜的有点大了，你再猜小点。。。")
    count += 1
    if count ==3:
        print('你猜错了！！！')
        break
        if continue_or_no != 'n':
            count = 0