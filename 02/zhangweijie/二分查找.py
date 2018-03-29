# encoding:utf-8
# author niko.zhang
'''
作业2 二分查找

思路：
low = 0
high = (len(list2)-1)
mid = (low + high)/2

'''

list2 = list(range(1,101))
key_value = int(input('输入一个1-100的数字：'))



high = len(list2)-1
low = 0
while low < high:
    mid = (low + high)//2
    if list2[mid] == key_value:
        print('{0}在列表的第{1}位'.format(key_value,mid))
        #print(mid)
        break
    #判断为左边
    elif list2[mid] > key_value:
        high = mid
    #判断为右边
    else:
        list2[mid] < key_value
        low = mid

