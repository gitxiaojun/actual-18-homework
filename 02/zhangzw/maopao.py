#encoding: utf-8

num = [6, 11, 7, 9, 4, 2, 1]

n = len(num)

#索引值从0-6
for x in range(n):
	#索引值从1-6,2-6,3-6,4-6,5-6,6
	for y in range(x+1,n):
		if num[x] > num[y]:
			num[x],num[y] = num[y],num[x]
print(num)
