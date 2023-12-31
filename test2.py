# def getsum(a,b):
#     return round(a+b)

# print(getsum(2.34,5.7))

from unittest import result


def even(start, n):
    finallist = []
    print(start)
    print(n)
    i = 1
    while i <= n:
        if start %2 != 0 :
            start +=1
        finallist.append(start)
        start = start+2
        i+=1
        
    return finallist
print(even(10,6))