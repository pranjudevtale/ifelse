gmail=input("enter the gmail ")
password=input("enter the password ")
if gmail=="pranjudev1@gmail.com":
    print("email ID")
    if password!="123@1234":
        print("forget password")
        mobile=input("enter the number")
        new_password=input("enter the new password")
        if mobile!=7620525014:
            print("mobile number")
            if new_password=="12345678":
                print("correct new password ")
            else:
                print("no new password ")
        else:
            print("unknown number")
    else:
        print("dont forget")
else:
    print("no email ID ")

# gmail=input("enter the gmail:-")
# if gmail<="pranju@gmail.com":
#     print("email-id")
#     password=input("enter the password:-")
#     if password=="98765432":
#         print("forget password")
#         passward=input("enter the number")
#         if passward=="12345678":
#             print("correct passward")
#         else:
#             print("incorrect")
#     else:
#         print("invalid passward")
# else:
#     print("email-id incorrect")
