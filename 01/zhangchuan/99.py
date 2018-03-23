#coding=utf-8
#author: zhangchuan
#date: 2018/3/20

# print ('str',end=" ")
# print 默认在结尾添加换行，加上end关键字并给空格，相当于在结尾的时候
# 将换行替换成空格，从而在内层循环不会以列输出，而已以行输出
# print ("") 换行
for i in range(1,10):
    for j in range(1,i+1):
       print (str(i)+"*"+str(j)+"=",i*j,end=" ")
    print ("")

