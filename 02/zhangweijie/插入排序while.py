# encoding:utf-8
'''

插入排序使用while的方法

'''

list1 = [9,3,4,2,6,7,5,1]

n = len(list1)

for i in range(1,n):
    temp = list1[i]
    j = i - 1
    while j >= 0 and list1[j] > temp:
        list1[j+1] = list1[j]
        j = j - 1
    list1[j + 1] = temp
print(list1)
