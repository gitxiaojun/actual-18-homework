v_list = []
for k in range(10000,0,-1):
	v_list.append(k)
for i in range(1,len(v_list)):
	for j in range(i,0,-1):
		if v_list[j] < v_list[j-1]:
			v_list[j],v_list[j-1] = v_list[j-1],v_list[j]
#print(v_list)
