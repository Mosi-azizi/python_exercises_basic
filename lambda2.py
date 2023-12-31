from cProfile import label


nubmer = [1,2,3,4,5,6]

resutl = filter(lambda num:num % 2 ==0,nubmer)
print(list(resutl))