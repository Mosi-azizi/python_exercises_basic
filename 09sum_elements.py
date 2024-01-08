
def sumElm(numbers):
    sum = 0
    for i in numbers:
        sum +=i
    return sum
numbers = list(range(1,11))
sum = sumElm(numbers)
print("Elements Sum : ",sum)

