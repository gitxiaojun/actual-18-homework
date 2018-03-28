users = []
users.append(('1','zhao',29,'13999990090'))
users.append(('2','zhi',29,'13999990091'))
users.append(('3','qiang',29,'13999990092'))
users.append(('4','zzq',29,'13999990093'))
users_add = []
users_del = []
del_flag = 0
fetch_flag = 0
head_format = '|{0:<10}|{1:<10}|{2:<5}|{3:<15}|'
title = ('ID','NAME','AGE','PHONE')
body_format = '|{0:<10}|{1:<10}|{2:<5}|{3:<15}|'
title_real = head_format.format(title[0],title[1],title[2],title[3])
usersid_list = []

while True:
	v_input=input('please input add/delete/update/fetch/list/quit:')
	if v_input == 'add':
		v_input=input('please input name,age,phone separated by comma:')
		for j in users:
			users_add.append(j[0])
		if len(users) == 0:
			users.append((1,)+tuple(v_input.split(',')))
		else:
			users.append((str(int(max(users_add))+1),)+tuple(v_input.split(',')))
		print('1 record is inserted.')
	elif v_input == 'delete':
		v_input = input('please input info that you wanna delete(id=/name=/age=/phone=):')
		for i in users:
			if v_input.split('=')[0] == 'id' and v_input.split('=')[1] == i[0]:
				users_del.append(i)
			elif v_input.split('=')[0] == 'name' and v_input.split('=')[1] == i[1]:
				users_del.append(i)
			elif v_input.split('=')[0] == 'age' and int(v_input.split('=')[1]) == int(i[2]):
				users_del.append(i)
			elif v_input.split('=')[0] == 'phone' and v_input.split('=')[1] == i[3]:
				users_del.append(i)
		for j in users_del:
			users.remove(j)
			del_flag += 1
		print('{0} record is deleted.'.format(del_flag))
	elif v_input == 'update':
		v_input = input('please input id,name,age,phone that you wanna update separated by comma:')
		for i in users:
			usersid_list.append(i[0])
		if v_input.split(',')[0] in usersid_list:
			users.remove(i)
			users.append((i[0],v_input.split(',')[1],v_input.split(',')[2],v_input.split(',')[3]))
			print('1 record is updated.')
		else:
			print('The id is not in the list!')
	elif v_input == 'fetch':
		v_input = input('please input info that you wanna fetch(id=/name=/age=/phone=):') 
		print(head_format.format(title[0],title[1],title[2],title[3]))
		print('-'*len(title_real))
		fetch_flag = 0
		for i in users:
			if v_input.split('=')[0] == 'id' and v_input.split('=')[1] == i[0]:
				print(body_format.format(i[0],i[1],i[2],i[3]))
				fetch_flag += 1
			elif v_input.split('=')[0] == 'name' and v_input.split('=')[1] == i[1]:
				print(body_format.format(i[0],i[1],i[2],i[3]))
				fetch_flag += 1
			elif v_input.split('=')[0] == 'age' and int(v_input.split('=')[1]) == i[2]:
				print(body_format.format(i[0],i[1],i[2],i[3]))
				fetch_flag += 1
			elif v_input.split('=')[0] == 'phone' and v_input.split('=')[1] == i[3]:
				print(body_format.format(i[0],i[1],i[2],i[3]))
				fetch_flag += 1
		print('{0} record is fetched.'.format(fetch_flag))
	elif v_input == 'list':
		print(head_format.format(title[0],title[1],title[2],title[3]))
		print('-'*len(title_real))
		for i in users:
        		print(body_format.format(i[0],i[1],i[2],i[3]))

	elif v_input == 'quit':
		print('bye bye!')
		break
	else:
		print('Invalid input!')
