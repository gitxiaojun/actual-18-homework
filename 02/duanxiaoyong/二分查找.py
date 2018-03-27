# /usr/bin/env python3
# -*- coding: utf-8 -*-
# auth: duanxiaoyong

#原始list数据
number_list = [5,13,19,21,37,56,64,75,80,88,92]
#通过插入排序number_list
for i in range(len(number_list)-1):
    for j in range(len(number_list)-i -1):
        if number_list[j]>number_list[j+1]:
            number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
#练习冒泡排序
print('原始数据排序后:',number_list)
#定义开始
start = 0
#定义结束
end = int(len(number_list) -1)
count =0
find_num = int(input('请输入需要find的数字：'))
while True:
    count +=1
    mid = int(start+end)//2
    mid_number = number_list[mid]
    if find_num > mid_number:
        start = mid + 1
    elif find_num < mid_number:
        end = mid
    else:
        print('查找的索引的值为:{0},查找的次数是：{1}'.format(mid,count))
        break
    if find_num not in number_list:
        break
