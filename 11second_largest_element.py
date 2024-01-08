


import random
#check with sort
def secondLargest(myList):
    print(myList)
    myList = sorted(myList, reverse=True)
    print("Second largest in this list is : ",myList[1])

myList = random.sample(range(1,101),25)
secondLargest(myList)

#check witout sort

def secondLargEl(mylist2):
    print(myList2)
    largest =max(myList2[0], myList2[1])
    second_largest = min(myList2[0],myList2[1])

    for i in mylist2[2::]:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i< largest:
            second_largest = i
    return second_largest
    # largestIDx=myList2.index(largest)

    # return myList2.pop(largestIDx)
    

myList2 = random.sample(range(1,101),25)
print("Second larget in this list is: ",secondLargEl(myList2))