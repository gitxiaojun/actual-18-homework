# encoding: utf-8
"""
@file: game.py
@time: 2018/3/19/0019 12:44
"""

left = 1
while left < 10:
    right = 1
    while right < 10:
        print(right, '*', left, '=', left * right, '\t', end='')
        right += 1
        if right > left:
            print()
            break
    left += 1

