#coding:utf-8
#定义一个列表,冒泡排序将按照从小到大的顺序排列，因为二分查找数组是有序的
num_list=[11,12,34,12,3,5,123,5,15,6,45,65]
length=len(num_list)
for i in range(0,length):
    for j in range(i+1,length):
        if num_list[i] > num_list[j]: #顺序排列，倒序排列就是小于
            temp=num_list[i]
            num_list[i]=num_list[j]
            num_list[j] = temp



#定义索引初始位置
low=0
high=length-1


num=int(input('请输入你要查找的整数：'))
if num not in num_list:
    print ('你查找的整数不存在')
    exit()

while low<=high:
    mid=(low+high)// 2
    if num_list[mid] > num:
        high = mid-1
    elif num_list[mid] < num:
        low = mid+1
    else:
        print ('你查找的整数索引为:%s' % mid)
        break


