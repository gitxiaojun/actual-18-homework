# encoding:utf-8
# author niko.zhang
'''
作业1 插入排序

思路：
假设第一个数字的位置是正确的，用后面一个数字和前面一个数字相比。
如果比第一个数字小就前移，知道大于或等于就不动。
'''
list1 = [9,3,4,2,6,7,5,1]

for i in range(1,len(list1)):
    for j in range(i,0,-1):
        if list1[j] < list1[j-1]:
            list1[j],list1[j-1]=list1[j-1],list1[j]
        else:
            continue

print(list1)
