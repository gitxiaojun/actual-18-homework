arr = [1,2,3,4,5,6,7,8,9]
for i in arr:
        for j in range(1,i+1):
                if i==j:
                    print(str(j)+'*'+str(i)+'='+str(i*j))
                else:
                    print(str(j)+'*'+str(i)+'='+str(i*j),end=',')
