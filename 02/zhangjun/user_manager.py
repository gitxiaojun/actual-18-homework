# encoding: utf-8
"""
@file: user_manager.py
@time: 2018/3/28/0028 17:42
"""

print("""
-------------------------------------
        User Manager System
指令菜单:
*\tlist\t\t查看用户列表
*\tadd\t\t\t添加用户
*\tdelete\t\t删除用户
*\tedit\t\t编辑用户
*\tfind\t\t查找用户
*\texit\t\t退出系统
-------------------------------------
""")

# init user list
users = [(1, 'lao da', 28, '13888888888'), (2, 'lao 2', 25, '13000000000'), (3, 'lao 3', 22, '13666666666')]

# title
title = ('uid', 'name', 'age', 'phone')

# row
format_row = '|{0[0]:^10d}|{0[1]:^20s}|{0[2]:^10d}|{0[3]:^24s}|'
# title
format_title = '|{0[0]:^10s}|{0[1]:^20s}|{0[2]:^10s}|{0[3]:^24s}|'

# format
title_str = format_title.format(title)

# split line
slplit_line = '-' * len(title_str)

while 1:
    ipt = input("请输入你需要的进行的操作（list/find/add/delete/edit/exit）：")
    if not ipt:
        print("你什么都没输入。。")
        continue
    if ipt == 'list':
        print(slplit_line)
        print(title_str)
        print(slplit_line)
        for user in users:
            print(format_row.format(user))
            print(slplit_line)
    elif ipt == 'add':
        _ipt = input("请输入需要录入的信息，格式为（name,age,phone）：")
        if _ipt:
            _ipt = _ipt.split(',')
            if len(_ipt) != 3:
                print("输入格式错误或信息不全")
            else:
                uid = 0
                for user in users:
                    if uid < user[0]:
                        uid = user[0]
                users.append((uid + 1, _ipt[0], int(_ipt[1]), _ipt[2]))
                print('添加成功！')
                print(slplit_line)
                print(title_str)
                print(slplit_line)
                for user in users:
                    print(format_row.format(user))
                    print(slplit_line)
        else:
            print('你什么都没输入。。')
    elif ipt == 'delete':
        uid = input('请输入需要删除的用户uid：')
        if uid and uid.isnumeric():
            for user in users:
                if int(uid) == user[0]:
                    users.remove(user)
                    print('删除成功！')
                    print(slplit_line)
                    print(title_str)
                    print(slplit_line)
                    for u in users:
                        print(format_row.format(u))
                        print(slplit_line)
        else:
            print('你的输入有问题。。')
    elif ipt == 'edit':
        uid = input('请输入要修改的用户uid：')
        if uid and uid.isnumeric():
            for user in users:
                uid = int(uid)
                if uid == user[0]:
                    users.remove(user)
                    _ipt = input("请输入需要录入的信息，格式为（name,age,phone）：")
                    if _ipt:
                        _ipt = _ipt.split(',')
                        if len(_ipt) != 3:
                            print("输入格式错误或信息不全")
                        else:
                            users.append((uid, _ipt[0], int(_ipt[1]), _ipt[2]))
                            print('修改成功！')
                            print(slplit_line)
                            print(title_str)
                            print(slplit_line)
                            for u in users:
                                print(format_row.format(u))
                                print(slplit_line)
                    break
        else:
            print('你的输入有问题。。')
    elif ipt == 'find':
        name = input('请输入需要查询的用户名：')
        if name:
            for user in users:
                if name == user[1]:
                    print(slplit_line)
                    print(title_str)
                    print(slplit_line)
                    print(format_row.format(user))
                    print(slplit_line)
        else:
            print('你的输入有问题。。')
    elif ipt == 'exit':
        print('Bye~')
        break
    else:
        print('你的输入有问题。。。')
