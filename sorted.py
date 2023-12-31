number = [1,2,56,4,3]
print(number)
nubmerSorted=sorted(number)
print(nubmerSorted)
revSorted = sorted(number,reverse=True)
print(revSorted)

users = [
    {'name': 'mohammad', 'family': 'ordookhani', 'age': 23},
    {'name': 'taha', 'family': 'ordookhani', 'age': 40},
    {'name': 'ali', 'family': 'ordookhani', 'age': 30},
    {'name': 'sara', 'family': 'ordookhani', 'age': 80}
]

print(sorted(users, key=lambda user:user['age'],reverse=True))
names = ['mohammad', 'milad', 'akbar', 'sara', 'iman','ali']

print(max (names, key=lambda n:len(n)))