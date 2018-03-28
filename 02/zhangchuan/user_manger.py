#coding:utf-8
#author:zc
#time:2017-03-27

#定义列表(list):users
users=[]
users.append((1,'zc',24,'133xxxxxxxx'))
users.append((2,'kk',23,'177xxxxxxxx'))
users.append((3,'woniu',30,'137xxxxxxxx'))
#定义表头
title=('ID','NAME','AGE','TEL')
#定义字符串格式化
tpl_title_format='|{0:^5s}|{1:^10s}|{2:^5s}|{3:^15s}|'
tpl_title = tpl_title_format.format(title[0],title[1],title[2],title[3])
splitline='-' * len(tpl_title)
tpl_body_format='|{0:^5}|{1:^10s}|{2:^5}|{3:^15s}|'
while True:
    op = input("请输入你需要的进行的操作（list/find/add/delete/edit/exit）：")
    if op == 'list':
        print(splitline)
        print(tpl_title)
        print(splitline)
        for user in users:
            print(tpl_body_format.format(user[0], user[1], user[2], user[3]))
        print(splitline)
    elif op == 'find':
        name = input("请输入你需要查找的用户名：")
        exits_user=None
        for user in users:
            if name == user[1]:
                exits_user=user
        if exits_user:
            print(splitline)
            print(tpl_title)
            print(splitline)
            for user in users:
                if name == user[1]:
                    print (tpl_body_format.format(user[0],user[1],user[2],user[3]))
            print (splitline)
        else:
            print ('用户不存在')

    elif op == 'add':
        txt = input("请输入需要录入的信息，格式为（name,age,tel）：")
        nodes = txt.split(',')
        uid = 0
        if len(nodes) != 3:
            print ("信息不全，请重新输入")
        else:
            for user in users:
                if uid < user[0]:
                    uid=user[0]
            users.append((uid+1,)+tuple(nodes))
            print ("信息录入成功")
    elif op == 'delete':
        uid = int(input("请输入需要删除的用户ID："))
        exits_user=None
        for user in users:
            if uid == user[0]:
                exits_user=user
        if exits_user:
            users.remove(exits_user)
            print ('已删除用户')
        else:
            print  ('用户不存在')
    elif op == 'edit':
        uid = int(input('请输入需要修改的用户ID：'))
        exits_user=None
        for user in users:
            if uid == user[0]:
                exits_user=user
                break
        if exits_user:
            txt = input("请输入需要录入的信息，格式为（name,age,tel）：")
            nodes = txt.split(',')
            if len(nodes) != 3:
                print ("信息不全，请重新输入")
            else:
                users.remove(exits_user)
                nodes[1]=int(nodes[1])
                users.append((uid,)+tuple(nodes))
    else:
        print ('退出程序')
        exit()

