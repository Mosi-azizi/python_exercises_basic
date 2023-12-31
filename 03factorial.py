def factorial(number):
    lst =list(range(1,number+1))
    
    revLst = lst[::-1]
    print(revLst)
    fact = 1
    for i in revLst:
        i = i * fact
        fact = i
    return fact
   

number = 5
print(factorial(number))