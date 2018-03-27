# encoding: utf-8
#初始数据
users = []
users.append((1, 'kk', 29, '185xxxxxx'))
users.append((2, 'wd', 28, '186xxxxxx'))
users.append((3, 'woniu', 30, '187xxxxxx'))

'''
---------------------
|id|name|age|contact|
---------------------
|01| kk | 28|138xx00|
---------------------
'''
#定义头部
_per_Title = '|{0:^3s}|{1:^10s}|{2:^5s}|{3:^13s}|'
_title = _per_Title.format('id','name','age','contact')
_line = '-' * len(_title)
_per_body = '|{0:^3d}|{1:^10s}|{2:^5d}|{3:^13s}|'

def _banner():
    _welcome ='|welcome to using usmgr system|'
    print('-'*len(_welcome))
    print('|'+' '*(len(_welcome)-2)+'|')
    print(_welcome)
    print('|'+' '*(len(_welcome)-2)+'|')
    print('-'*len(_welcome))
_banner()

while True:
    _fun = input('请输入以下指令 find/list/add/delete/update/exit:')
    #listuser
    if _fun == 'list':
        print(_line)
        print(_title)
        print(_line)
        for user in users:
            print(_per_body.format(user[0],user[1],user[2],user[3]))
        print(_line)

    #adduser
    elif _fun == 'add':
        add_user = input('请输入相关信息 name,age,contact:')
        nodes = add_user.split(',')
        if len(nodes) != 3:
            print('你输入的信息有误，请重新输入。')
        else:
            uid = 0
            for user in users:
                if uid < user[0]:
                    uid = user[0]
            nodes[1] = int(nodes[1])
            users.append((uid+1,)+tuple(nodes))
    #delete
    elif _fun == 'delete':
        uid_user = int(input('请输入你要删除的用户ID: '))
        for user in users:
            if uid_user == user[0]:
                users.remove(user)
                break
    #find
    elif _fun == 'find':
        exist_user = None
        find_uid = int(input('请输入你要查询的用户ID: '))
        for user in users:
            if find_uid == user[0]:
                exist_user = user
                print(user)
                break
        if exist_user == None:
            print('用户信息不存在')
    #update
    elif _fun == 'update':
        update_uid = int(input('请输入你要修改的用户ID: '))
        exist_user = None
        for user in users:
            if update_uid == user[0]:
                exist_user = user
            if exist_user:
                print('你要修改的用户是',end='\t')
                print(exist_user)
                update_user = input('请重新输入该用户信息 name,age,contact: ')
                nodes = update_user.split(',')
                if len(nodes) != 3:
                    print('你输入的信息有误。')
                else:
                    nodes[1] = int(nodes[1])
                    users.remove(user)
                    users.append((update_uid,)+tuple(nodes))
                    print('修改成功')
                    break
        if exist_user == None:
            print('用户信息不存在')
    #exit
    elif _fun == 'exit':
        _exit = input('是否如确认退出程序 yes/no？')
        if _exit == 'yes':
            break
        else:
            continue
