number  = [1,2,3,4,5,6]
newNubmer = [[1,2,3],[4,5,6]]

# print(newNubmer[1][1])

for li in newNubmer:
    for li2 in li:
        print(li2)


newNumbers =[[print(l) for l in li] for li in newNubmer]

genlist = [['X' if n % 2 == 0 else 'O' for n in range(1,4)] for num in range(1,4)]
print(genlist)