# encoding:utf-8
# author niko.zhang
'''
作业2 二分查找

思路：
low = 0
high = (len(list2)-1)
mid = (low + high)/2

'''

list2 = [1,2,5,13,19,21,37,56,64,75,80,88,92,100]
key_value = 21



high = len(list2)-1
low = 0
while low < high:
    mid = (low + high)//2
    if list2[mid] == key_value:
        print('u find it,is:',end='\t')
        print(mid)
        break
    #判断为左边
    elif list2[mid] > key_value:
        high = mid
    #判断为右边
    else:
        list2[mid] < key_value
        low = mid

