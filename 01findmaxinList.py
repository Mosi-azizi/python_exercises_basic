""" def maxElemntList(mylist):
    listSort = sorted(mylist)
    return listSort[-1]

mylist = [12,54,16,18]
print(maxElemntList(mylist))

 """
""" def maxElm(mylist):
    largest = mylist[0]
    for i in mylist:
        if i > largest:
            largest = i
    return largest

numbers = [10, 2, 45, 67, 23, 90, 12]
largest_element = maxElm(numbers)
print("largest element in {} is:".format(numbers), largest_element)
 """

import random


def findMaxElement(number):
    largest = number[0]
    for i in number:
        if i > largest:
         largest = i
    return largest
number = random.sample(range(1,200),20)
largest_number = findMaxElement(number)
print("large element in this list {} is : ".format(number), largest_number)

find_largest_element = lambda lst: max(lst) if lst else None
number2 = random.sample(range(1,100),10)
largest_number2 = find_largest_element(number2)
print("large element in this list {} is : ".format(number2), largest_number2)
