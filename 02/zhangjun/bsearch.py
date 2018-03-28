# encoding: utf-8
"""
@file: bsearch.py
@time: 2018-03-29 0:29
"""

data = [1, 2, 5, 13, 19, 21, 37, 56, 64, 75, 80, 88, 92, 100]

start = 0
end = len(data) - 1

while True:
    input_num = input('请输入要查找的数字：')
    if input_num and input_num.isnumeric():
        input_num = int(input_num)

        mid = (start + end) // 2

        if input_num not in data:
            print('没有你要找的东西')
            break
        else:
            if input_num < data[mid]:
                end = mid
            elif input_num > data[mid]:
                start = mid
            else:
                print("该数字的索引是:{}".format(mid))
                break
    else:
        print('你的输入有问题')
