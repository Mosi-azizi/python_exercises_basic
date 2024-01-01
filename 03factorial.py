""" def factorial(number):
    lst =list(range(1,number+1))
    
    revLst = lst[::-1]
    print(revLst)
    fact = 1
    for i in revLst:
        i = i * fact
        fact = i
    return fact
   

number = 5
print(factorial(number)) """


def factorial(number):
    if number < 0 :
        return None
    elif number == 1 :
        return 1
    else:

        myList = list(range(1,number+1))
        revList = myList[::-1]
        fact = 1
        for i in revList:
            fact = fact*i
        return fact

number = 5
print(factorial(number))
