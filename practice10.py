year=int(input("enter the  year"))
if year%4==0 :
    print("leap year",year)
elif year%400==0:
    print("leap year",year)

else:
    print("not leap year",year)