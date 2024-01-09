#Use set 
def removeDuplicate(myList):
    return list(set(myList))

myList = [1,6,8,7,6]
removeDup = removeDuplicate(myList)
print(removeDup)

# use for loop
def removeDuplicate2(myList2):
    new_list = []
    for i in myList2:
        if i not in new_list:
            new_list.append(i)
    return new_list

myList2 = [2,22,2,2,2,2,5]
removeDup2 = removeDuplicate2(myList2)
print(removeDup2)