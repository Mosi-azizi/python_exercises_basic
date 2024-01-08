import re
def checkEmail(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern,email):
        print(f"{email} address is correct")
    else:
        print(f"{email} address is not correct")

email = input("please enter a email address :")
checkEmail(email)