# getNumber = input("please enter a number: ")

# while getNumber != "100":
#     print("your number is {0} please try again".format(getNumber))
#     getNumber = input("please enter a number: ")

# for num in range(1,11):
#     print("*" * num)

# num = 1
# while num <=10:
    
#     print("*" * num)
#     num +=1
#     if num == 6 :
#         break
    
# for num in range(1,10):
#     stars = ""
#     for star in range(1,num+1):
#         stars +="*"
#     print(stars)

# for num in range(1,10):
#     print("*"* num)
# myRange = range(1,100)
# myList= list(myRange)
# # print(myList[3])
# isExist = 10 in myList
# print(isExist)



# myColors = ["red", "blue", "green", "gray", "yellow", "orange", 3.6]
# # for color in myColors:
# #    print(color)
# print(myColors)
# print(myColors[1])
# print(myColors[3])
# print(myColors[-1])
# print(myColors[-3])
# print(myColors[0].title())
# print(myColors[3].title())
# myColors[2] = 'GREEN'
# print(myColors)
# myColors.append('black')
# print(myColors)

# motorcycle = []
# motorcycle.append('honda')
# motorcycle.append('yamaha')
# print(motorcycle)
# motorcycle.insert(0, 'ducati')
# print(motorcycle)
# # del motorcycle[0]
# # print(motorcycle)
# # pope_motorcycle = motorcycle.pop()
# # print(motorcycle)
# # print(pope_motorcycle)
# # popsecond_motorcycle = motorcycle.pop(1)
# # print(popsecond_motorcycle.title())
# motorcycle.remove('ducati')
# print(motorcycle)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# # cars.sort()
# # cars.sort(reverse=True)
# print(cars)
# print(sorted(cars))
# print(cars)
# cars.reverse()
# print(cars)

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()} that was a greate trick!")
#     print(f"I can't wait to see your next trick,{magician.title()} \n")
# print("Thank you every one, that was a grete magic show! ")

squers = []
# for value in range(1,11):
#     squers.append(value ** 2)
squers = [value ** 2 for value in range(1,11)]
print(squers)
print(min(squers))
print(max(squers))
print(sum((squers)))

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:3])
print(players[4:])