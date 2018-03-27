#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!shenjie :2018/3/26 10:26
#!@Auther :shenjie
#!@file: 6.py
users = []
users.append((1, 'kk', 29, '185xxxxxx'))
users.append((2, 'wd', 28, '186xxxxxx'))
users.append((3, 'woniu', 30, '187xxxxxx'))
app_info = '''
+-----------------------------------+
| Version: 1.0                      |
| Author:  啊jie                    |
+-----------------------------------+
'''

# 获取最后一个ID的值
tmp_tuple = tuple(users[-1:])
uid = tmp_tuple[0][0]
#定义一个临时的列表，存放名字，若输入的名字存在则需要重新输入
tmp_name=[]
for i in users:
    tmp_name.append(i[1])
# 初始化查看的循环开关
view=True

print(app_info)
while view:
    # 打印当前用户的位置
    print("home>>>")
    print(51 * '-')
    print('''
    1、查看
    2、添加
    3、删除
    4、修改
    5、退出
    ''')
    print(51 * '-')
    choose=input('请输入你的选择>>>：')
    if choose == '1':
        print(51 * '-')
        print('''|{0}| |{1}| |{2}| |{3}|'''.format('ID'.center(10,' '),'name'.center(10,' '),'age'.center(10,' '),'Telephone'.center(10,' ')))
        print(51 * '-')
        for i in users:
            print('''|{0}| |{1}| |{2}| |{3}|'''.format(str(i[0]).center(10, ' '),i[1].center(10, ' '),str(i[2]).center(10, ' '),i[3].center(10, ' ')))


    if choose == '2':
    # 初始化添加的循环开关
        adduser=True
        while adduser:
            print("home>%s>" % '添加')
            print(51 * '-')
            name=input('请输入名字：')
            test_name=True
            while test_name:
                if name in tmp_name:
                    name = input('名字已经存在，请重新输入名字：')
                else:
                    test_name=False
            #将名字添加到tmp_name中
            tmp_name.append(name)
            age=input('请输入年龄：')
            for i in age:
                if not i.isdigit():
                    age = input('输入有问题，请重新输入年龄：')
            Telephone=input('请输入号码：')
            for j in Telephone:
                if not j.isdigit():
                    Telephone = input('输入有问题，请重新输入号码：')
            print(51 * '-')

            #添加用户信息
            users.append((uid+1,name,age,Telephone))
            uid=uid+1
            adduser = False
        print('添加完成，返回上一级菜单')

    if choose == '3':
        print("home>%s>" % '删除')
        print(51 * '-')
        print('''|{0}| |{1}|'''.format('ID'.center(10, ' '), 'name'.center(10, ' ')))
        print(51 * '-')
        ID=0
        for i in tmp_name:
            print('''|{0}| |{1}|'''.format(str(ID).center(10, ' '), i.center(10, ' ')))
            ID+=1
        print(51 * '-')
        del_user=input('请输入删除的ID：')
        print(51 * '-')
        while True:
            if int(del_user) >= len(tmp_name):
                del_user = input('输入错误，请重新输入删除的ID：')
            else:
                break
        users.pop(int(del_user))
        tmp_name.pop(int(del_user))
        print('删除成功，返回上一级菜单')

    if choose == '4':
        print("home>%s>" % '修改')
        print(51 * '-')
        print('''|{0}| |{1}| |{2}| |{3}|'''.format('ID'.center(10,' '),'name'.center(10,' '),'age'.center(10,' '),'Telephone'.center(10,' ')))
        print(51 * '-')
        # 由于user中的元组不能修改，需要把它转换为list，进行修改
        list_user = list()
        #定义一个临时的列表
        list_b=list()
        for i in users:
            list_user.append(list(i))
        for i in users:
            print('''|{0}| |{1}| |{2}| |{3}|'''.format(str(i[0]).center(10, ' '),i[1].center(10, ' '),str(i[2]).center(10, ' '),i[3].center(10, ' ')))
        print(51 * '-')
        update = input('请选择修改的ID：')
        # 初始化修改的循环开关
        mod=True
        while mod:
            print(51 * '-')
            print('''
            1、name
            2、age
            3、Telephone
            4、返回上一级菜单
            ''')
            print(51 * '-')
            mes = input('请选择需改的内容为：')
            if mes == '1':
                name_up=input('修改的名字为：')
                for n in list_user:
                    if n[0] == int(update):
                        n[1] = name_up

                for i in list_user:
                    list_b.append(tuple(i))
                users=list_b
                print('名字修改成功')
                break
            elif mes == '2':
                age_up=input('修改的年龄为：')
                for n in list_user:
                    if n[0] == int(update):
                        n[2] = age_up
                for i in list_user:
                    list_b.append(tuple(i))
                users=list_b
                print('年龄修改成功')
                break
            elif mes == '3':
                Tel_up = input('修改的号码为：')
                for n in list_user:
                    if n[0] == int(update):
                        n[3] = Tel_up
                for i in list_user:
                    list_b.append(tuple(i))
                users=list_b
                print('号码修改成功')
                break
            elif mes == '4':
                mod=False
            else:
                print('输入错误，请重新输入')
    if choose == '5':
        exit()
