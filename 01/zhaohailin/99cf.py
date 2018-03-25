# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Version : V1.0.0
# @File    : 99cf.py

# 思路：

# 设置为0
# z = 0
# for x in range(1,10):
# 	z += 1
# 	for y in range(1,z+1):
# 		if y != x:
# 			print('%s×%s=%s'%(y,x,x*y),end=' ')
# 		else:
# 			print('%s×%s=%s'%(y,x,x*y))


# 来源：
# https://www.cnblogs.com/xuyuanyuan123/p/6684814.html
# i=0
# j=0
# while i<9:
#     i+=1
#     while j<9:
#         j+=1
#         print(j,"x",i,"=",i*j,"\t",end="")
#         if i==j:
#             j=0
#             print("")
#             break

# 通过pycharm格式化后的，标准化的格式是不是都是这样写的？？
# z = 0
# for x in range ( 1 , 10 ):  # range从1-10范围取数
# 	z += 1  #
# 	for y in range ( 1 , z + 1 ):
# 		if y != x:
# 			print ( '%s×%s=%s' % (y , x , x * y) , end=' ' )
# 		else:
# 			print ( '%s×%s=%s' % (y , x , x * y) )