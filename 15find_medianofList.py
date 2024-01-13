import random
def medianList(myList):
    sorted_list = sorted(myList)
    n = len(sorted_list)
    if n % 2 != 0:
        median = sorted_list[n // 2]
    else:
        mid1 = sorted_list[n // 2]
        mid2 = sorted_list[n // 2 -1]
        median = (mid1+mid2) / 2
    return median

myList = random.sample(range(1,100),19)
print(f"The median of this numbers of {myList} is : ",medianList(myList))