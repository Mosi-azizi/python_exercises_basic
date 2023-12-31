# def sayhello():
#     print("sayhello")

# sayhello()

# def sqre():
#     a = 6
#     b = 7
#     return b**a


# resutl = sqre()
# print(resutl)
# print(sqre())
# def sum (firstNumber,secondNumber):
#     return secondNumber + firstNumber

# print(sum(5,10))


def showfullname(firstName, lastName):
    return f"{firstName} {lastName}"
    
name = "sam" #Argoman
family = "azizi"

print(showfullname(firstName=name,lastName=family))

# person = {
#     "name":"sam",
#     "family":"azizi"
# }

# print(showfullname(person["name"],person["family"]))




mylist = range(1,100)
mynubmers = list(mylist)
# print(mynubmers)
def sum_odd_number(numbers):
    total = 0
    for num in numbers:
        
        if num % 2 !=0:
            total +=num
    return total

# print(sum_odd_number(mynubmers))

def is_even_number(number):
    if number % 2 == 0:
        return f"number is even"
    return f"nubmer is odd"

print(is_even_number(15364))

