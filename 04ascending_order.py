import random


def ascanding(myList):
    #myList.sort(reverse=True)
    #sorted(myList, reverse=True)
    temp=0
    for i in range(0,len(myList)):
        for j in range(i+1,len(myList)):
            if (myList[i] < myList[j]):
                temp = myList[i]
                myList[i] = myList[j]
                myList[j] = temp
    print(myList)



myList = random.sample(range(0,200),20)
print(myList)
ascanding(myList)