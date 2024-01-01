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


""" def factorial(number):
    if number < 0 :
        return None
    elif number == 0 :
        return 1
    else:

        myList = list(range(1,number+1))
        revList = myList[::-1]
        fact = 1
        for i in revList:
            fact = fact*i
        return fact

number = 5
print(factorial(number)) """





def factByRevese(number2):
    if number2 < 0 :
        return None
    elif number2 == 0 :
        return 1
    else:
        myList = list(range(1,number2+1))
        myList.reverse()
        result = 1
        for i in myList:
            result *=i
        return result

number2 = int(input("Enter a number: "))
factorial = factByRevese(number2)
print("Factorial {} is : ".format(number2), factorial)