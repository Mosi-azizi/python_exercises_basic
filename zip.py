numbers1 = [1,2,3,4]
numbers2 = [7,8,9,4]
result = zip(numbers1,numbers2)
# print(list(result))
# print(dict(result))

myList = [(1, 7), (2, 8), (3, 9), (4, 4)]
print(list (zip(*myList)))