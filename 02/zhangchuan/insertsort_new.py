#coding:utf-8

#插入排序：一组有序的数据列表，要求插入一个任意整数字的之后，还是有序
#思路：将输入的数据插入到第一个位置，然后依次与后面的数字进行比对，并将插入的数放到合适的位置
#定义一个列表
num_list=[]
while True:
    num=input('请输入需要插入的整数or done：')
    if num != 'done':
        num_list.append(int(num))
    else:
        break

#定义一个临时变量
temp=None

length=len(num_list)

for i in range(0,length):
    for j in range(i+1,length):
        if num_list[i] > num_list[j]: #顺序排列，倒序使用小于号
            temp=num_list[i]
            num_list[i]=num_list[j]
            num_list[j] = temp

print (num_list)
