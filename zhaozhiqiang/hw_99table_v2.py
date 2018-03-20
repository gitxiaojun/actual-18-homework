arr = [1,2,3,4,5,6,7,8,9]
arr2 = [1,2,3,4,5,6,7,8,9]
for i in arr:
	for j in arr2:
		if j>i:
		    break
		elif i==j:
		    print(str(i)+'*'+str(j)+'='+str(i*j))
		elif i*j>=10:
		    print(str(i)+'*'+str(j)+'='+str(i*j),end=',')
		else:
		    print(str(i)+'*'+str(j)+'='+str(i*j),end=' ,')
			
		
