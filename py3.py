grade=int(input("enter the grade "))
if grade>=65:
    print("passing grade ")
    if grade<=90 or grade>=80:
        print("A")
    elif grade<=80 or grade>=70:
        print("B")
    elif grade<=70 or grade>=65:
        print("C")
    elif grade>=65:
        print("D")
else:
    print("failing grade ")


        