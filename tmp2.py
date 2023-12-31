from ast import alias
from traceback import print_tb


myNumber = [1,2,3,5,6,7,9,10]
selectNum = myNumber[5]
print(selectNum)
slicemyNum = myNumber[1:6:2]
print(slicemyNum)
# for num in myNumber:
#     print(num)
# sliceNum= myNumber[-3::]
# print(sliceNum)
# copyofMyNumber = myNumber[::2]
# print(copyofMyNumber)

# print(myNumber  == copyofMyNumber)
# print(myNumber is copyofMyNumber)
colors = ["red", "green", "blue", "yellow", "orange"]
copyofcolors = colors[::-1]

colors.reverse()

print(colors)
print(copyofcolors)
print(copyofcolors[::-1])
myName = "SAM Azizi"
# print(myName[::-1])
print(myName.split(' '))
# for word in myName:
#     print(word)
yourWord = input('please enter your full name: ')
print(yourWord[::-1])
print(yourWord[0:4])

