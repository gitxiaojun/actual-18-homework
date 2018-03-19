#coding: utf8

for i in range(1,10):
	for j in range(1,i+1):
		print(str(j)+'*'+str(i)+'=',i*j,end=' ')
	print('')
