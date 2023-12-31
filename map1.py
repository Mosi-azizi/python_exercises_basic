from cProfile import label


number = [1,2,3,4,6]

double = list(map(lambda num:num*2,number))
print(double)

names = ["sam","azizi"]

upperNames = map(lambda name:name.upper(),names)
print(list(upperNames))

people = [
    {'name': 'mohammad', 'family': 'ordookhani', 'age': 23},
    {'name': 'sara', 'family': 'moradi', 'age': 25},
    {'name': 'iman', 'family': 'madaeny', 'age': 30}
]
families2 = map(lambda person:person["family"],people)
print(list(families2))

families3 = []
for person in people:
    families3.append(person['family'])
print(families3)

