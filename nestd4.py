# ***disco permission***
day=input("enter the day- ")
if day=="tuesday":
    print("ja skte hai")
    permission=input("enter the disco permissionyes/no- ")
    if permission=='yes':
        print("market ja skte hai")
        work=input("enter the work- ")
        if work=="hospital":
            print("hospital mai ja sakte ho ")
            rule=input("enter the rules ")
            if rule=="follow":
                print("sanitizer or mask lgana padega")
                time=input("enter the time- ")
                if time<="6":
                    print(time," tb tak entry milegi")
                    print("quarentine rhna padega 7 days")
                else:
                    print(" entry nahi milegi")
            else:
                print("sanitizer or mask lagake nahi jana")
        else:
            print("hospital mai nahi ja sakte")
    else:
        print("market nahi ja sakte ho")
else:
    print("nahi ja sakte ho")                                                     