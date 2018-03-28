v_list = []
for k in range(10000,0,-1):
        v_list.append(k)
v_value = 0
listlen = len(v_list)
for tar in range(1,listlen):
	v_value = v_list.pop(tar)
	for j in range(1,listlen):	
		if v_value >= v_list[tar-j]:
			v_list.insert(tar-j+1,v_value)
			break
		elif tar-j == 0:
			v_list.insert(0,v_value)
			break
print(v_list)
