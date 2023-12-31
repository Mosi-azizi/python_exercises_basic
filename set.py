number = {1,2,3,4,8,7,"ali"}
print("ali" in number)

listnumber = [1,2,3,4,5,6]

for num in number:
    print(num)

print(list(number))
print(set(listnumber))
number.add(562)
print(number)
number.remove(562)
print(number)
number.discard(562)

copyNumber = number.copy()
print(copyNumber)
copyNumber.clear()
print(copyNumber)