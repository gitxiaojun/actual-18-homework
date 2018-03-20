#encoding: utf-8

import random
result = random.randint(0,100)
count = 0

while True:
    prompt = int(input("enter a number:"))
    if prompt > result:
        print("bigger than result")
    elif prompt < result:
        print("smaller than result")
    else:
        print("you are right")
        break
    count += 1
    if count == 5:
        print("stupid")
        break
