num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
if num1>num3>num2:
    print(num1, "max")
elif num2>num1>num3:
    print(num2, "max")
elif num3>num2>num1:         
    print(num3, "max")
else:
    print(num1,"max")
    

