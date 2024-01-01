def dascending_order1(myList):
    myList.sort(reverse=True)
    return myList

def dascending_order2(myList):
    sorted(myList, reverse=True)
    return myList

def dascending_order3(myList):

    temp = 0
    for i in range(0,len(myList)):
        for j in range(i+1,len(myList)):
            if(myList[i] < myList[j]):
                temp = myList[i]
                myList[i] = myList[j]
                myList[j] = temp
    return myList
            

myList = [15.65,89,42,1]
#print("Sort List by sort funct",dascending_order1(myList))
#print("Sort list by sorted funct",dascending_order2(myList))
print("Sort list by ... ",dascending_order3(myList))


