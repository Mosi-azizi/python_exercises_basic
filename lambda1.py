def squer(num): return num * num

myFunction = lambda num: num * num

print(squer(6))
print(myFunction(6))

def sum(first,second): return first + second

sum2 = lambda first,second:first + second

print(myFunction.__name__)

sum3= lambda a,b,c:a+b+c
print(sum3(2,568,4))