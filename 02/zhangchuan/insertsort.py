#coding:utf-8

#插入排序：一组有序的数据列表，要求插入一个任意整数字的之后，还是有序
#思路：将输入的数据插入到第一个位置，然后依次与后面的数字进行比对，并将插入的数放到合适的位置
#定义一组有序列表
num_list=[12,14,15,21,23,26,40,42,54,72]

num=int(input('请输入需要插入的整数：'))
#定义一个临时变量
temp=None
#将数字插入列表,将数据插入到第一位
#insert(),插入时候指定索引位置
num_list.insert(0,num) #将插入的数字放在首位
length=len(num_list)
#将插入数据与原列表对比
for i in range(1,length):
    j = i - 1  #获得插入元素索引位置
    #如果后一个元素小于插入元素，则将两个元素互换位置
    if num_list[i] < num_list[j]:
        temp=num_list[i]
        num_list[i]=num_list[j]
        num_list[j] = temp

print (num_list)
