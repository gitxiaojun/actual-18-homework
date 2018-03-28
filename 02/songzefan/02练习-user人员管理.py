#!/usr/bin/env python3
# encoding: utf-8

users=[]

text= """ ----用户管理系统 V-1.0.0----
          请按提示进行输入
          add : 添加用户
          del : 删除用户
          edit: 编辑用户信息
          list: 列出用户信息
          quit/q :退出系统
"""

print(text)

while True:
    INPUT=input("请输入要执行的操作:")

    #添加用户信息
    if INPUT == "add":
        name=input("请输入要添加的用户名：")
        while name == "":
            name=input("请输入要添加的用户名：")
        age=input("请输入要添加的年龄：")
        while age == "":
            age=input("请输入要添加的年龄：")
        phone=input("请输入要添加的联系方式：")
        while phone == "":
            phone=input("请输入要添加的联系方式：")
        users.append([name,age,phone])
        print("用户添加成功")

    #列出用户
    if INPUT == "list":
        #print('|{0:^10s}|{1:^15s}|{2:^5s}|{3:^25s}|'.format('ID','姓名','年龄','联系方式'))
        print('|{0:^10s}|{1:^13s}|{2:^5s}|{3:^15s}|'.format('ID','NAME','AGE','PHONE'))
        for i in range(len(users)):
            print("|{0:^10d}|{1:^10s}|{2:^5s}|{3:^15s}|".format(i,users[i][0],users[i][1],users[i][2]))   
   
    #删除用户
    if INPUT == "del":
        num = int(input("请输入要删除的联系人的ID号："))
        del users[num]
        print("已经成功删除....")

    #编辑用户信息
    if INPUT == "edit":
        num = int(input("请输入要修改的用户ID："))
        change = input("请输入要修改的内容(name/age/phone):")
        if change == "name":
            new = input("请输入新的名字：")
            users[num][0] = new
            print("{}修改成功".format(change))
        if change == "age":
            new = input("请输入修改后的年龄：")
            users[num][1] = new
            print("{}修改成功".format(change))
        if change == "phone":
            new = input("请输入新的电话号码：")
            users[num][2] = new
            print("{}修改成功".format(change))

    #退出系统
    if INPUT == "q" or INPUT == "quit":
        break
