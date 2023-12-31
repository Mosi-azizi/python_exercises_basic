# def sum_all_number(name,*args):
#     print(name)
#     total = 0
#     for num in args:
#         total +=num
#     return total

# print(sum_all_number("first",1,2,3,4,5,6))
# print(sum_all_number("second",1,6,6,4,))

# def showUserInfo(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
#         # print(f"{key}  {value}")


# showUserInfo(name="sam",family="azizi",age=40)



def sum_all_numbers(*args):
    total = 0
    for num in args:
        total +=num
    return total

myNumbers = list(range(1,100))
# print(sum_all_numbers(myNumbers)) #get error
print(sum_all_numbers(*myNumbers))

def display_name(name,family):
    print(f"name is {name} and family is {family}")

person = {"name":"sam","family":"azizi"}
# display_name(person["name"],person["family"])
display_name(**person)
