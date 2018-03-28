num1=1
num2=1
while num1<=9:
    while num2<=num1:
        print(num1,"×",num2,"=",num1*num2,"  ",end="")
        num2+=1
    num2=1
    print("\n")
    num1+=1