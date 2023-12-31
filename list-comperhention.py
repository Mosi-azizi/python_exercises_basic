myNumber = [1, 2, 3, 4, 5, 6]

double_numbers = []
for num in myNumber:
    double = num * 2
    double_numbers.append(double)
print(double_numbers)


double_numbers2  = [num * 2 for num in myNumber]
print(double_numbers2)

myName = "Mohamad"
nameChar = [char.upper() for char in myName]
print(nameChar[-5::-1])

even = [num for num in myNumber if num % 2 ==0]
print(even)
list1 = range(1,1000)
even1 = [num for num in list1 if num % 2 == 0   ]
print(even1)

newList = [num *2 if num % 2 ==0 else num * 3 for num in myNumber]
print(newList)
