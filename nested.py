# ***time table**
time=float(input("enter the time "))
if time>6.00 and time<=7.00:
    print("morning exercise time")
    time=float(input("enter the time "))
    if time>7.00 and time<=9.00:
        print("breakfast time")
        time=float(input("enter the time "))
        if time>9.00 and time<=10.00:
            print("english activity")
            time=float(input ("enter the time "))
            if time>10.00 and time<=13.00:
                print("coding time")
                time=float(input("enter the time "))
                if time>13.00 and time<=14.30:
                    print("lunch time")
                    time=float(input("enter the time "))
                    if time>14.30 and time<=17.00:
                        print("self study time")
                        time=float(input("enter the time "))
                        if time>17.00 and time<=17.30:
                            print("break time")
                            time=float(input("enter the time "))
                            if time>17.30 and time<=19.00:
                                print("cultural activity")
                                time=float(input("enter the time "))
                                if time>19.00 and time<=21.00:
                                    print("learning study")
                                    time=float(input("enter the time "))
                                    if time>21.00 and time<=22.00:
                                        print("dinner")
                                        time=float(input("enter the time "))
                                        if time>22.00 and time<=23.00:
                                            print("our study")
                                            time=float(input("enter the time"))
                                        else:
                                            print("not allowed our study ")
                                    else:
                                        print("not allowed dinner")
                                else:
                                    print("not allowed learning activity")
                            else:
                                print("not allowed cultural activity")
                        else:
                            print("not allowed break")
                    else:
                        print("not allowed self study")
                else:
                    print("not allowed lunch")
            else:
                print("not allowed coding")
        else:
            print("not allowed english activity")
    else:
        print("not allowed breakfast")
else:
    print("not allowed morning exercise")
                                        