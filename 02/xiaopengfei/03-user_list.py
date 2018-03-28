# -*- coding: utf-8 -*-
'''
@Time    : 2018/3/28 19:38
@Author  : Xiaopf
@Email   : xiaopf@aukeys.com
@File    : 03-user_list.py
'''

'''
练习3:
    让用户在控制台上输入”find/list/add/delete/update/exit”格式字符串
    如果输入add，则让用户继续输入用户名、年龄、联系方式等数据， 将用户数据(用户名, 年龄，联系方式)，放入list中存储，在放入list之前检查用户名不重复，如果重复，则提示用户已存在
    如果输入delete，则让用户输入”用户名”字符串，根据用户名查找list中数据，若存在数据则将该数据移除，若用户数据不存在，则提示不存在
    如果输入update，则让用户分别输入用户名、年龄、联系方式等数据，根据用户名查找list中数据，若存在数据则将改数据更新为新的(用户名, 年龄，联系方式)，若用户数据不存在，则提示不存在
    如果用户输入find，则让用户输入”用户名” ，根据用户名查找list中数据用户名等于字符串的用户信息，并打印
    如果用户输入list，则打印所有用户信息
    打印用户第一个行数据为用户信息描述，从第二行开始为用户数据
    如果用户输入exit，则打印退出程序，并退出
'''

userlist = []
actionlist = ['find','list','add','delete','update','exit']

# 格式化
tpl = '|{:^10}|{:^5}|{:^15}|'
header = tpl.format('name','age','phone')
splitline = '-' * len(header)
while True:
    action = input("输入\"find/list/add/del/update/exit\" >>: ").strip()
    if action not in actionlist:
        print('输入错误，请重新输入!')
    elif action == 'add':
        txt = input('请输入用户名,年龄,联系方式 >>: ')
        exsit_val = tuple(txt.split(','))
        flag = False
        if len(exsit_val) != 3:
            print('输入错误，请重新输入！')
        else:
            for user in userlist:
                if user[0] == exsit_val[0]:
                    flag = True
                    print('用户已存在，请重新输入！')
                    break
            if not flag:
                userlist.append(exsit_val)
                print('添加成功！%s' % userlist)
    elif action == 'del':
        name = input('请输入要删除的用户名 >>:').strip()
        flag = False
        for user in userlist:
            if name == user[0]:
                flag = True
                userlist.remove(user)
                print('已删除！%s' % userlist)
                break
        if not flag:
            print('用户不存在')
    elif action == 'update':
        name = input('请输入用户名 >>: ').strip()
        flag = False
        for user in userlist:
            if user[0] == name:
                flag = True
                txt = input('请输入新用户名,年龄,联系方式 >>: ')
                exsit_val = tuple(txt.split(','))
                userlist.remove(user)
                userlist.append(exsit_val)
                print('用户已更新')
                break
        if not flag:
            print('用户不存在')
    elif action == 'find':
        name = input('请输入用户名 >>: ').strip()
        flag = False
        print(splitline)
        print(header)
        print(splitline)
        for user in userlist:
            if user[0] == name:
                flag = True
                print(tpl.format(user[0],user[1],user[2]))
        print(splitline)
        if not flag:
            print('用户不存在')
    elif action =='list':
        if len(userlist) == 0:
            print('nothing')
        else:
            print(splitline)
            print(header)
            print(splitline)
            for user in userlist:
                print(tpl.format(user[0], user[1], user[2]))

            print(splitline)
    elif action == 'exit':
        print(header)
        for user in userlist:
            print(tpl.format(user[0], user[1], user[2]))

        break