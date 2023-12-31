myNumber = dict(first=1,second=2,third=3)
print(myNumber)

sqrmyDic = {key:valu**2 for key,valu in myNumber.items()}
print(sqrmyDic)
doubleNumber = {num:num**2 for num in [1,2,3,4,5]}
doubleNumber2 = {num:num**2 for num in range(1,6)}
print(doubleNumber)
print(doubleNumber2)

simpleNumber = {num : ("even" if num % 2 == 0 else "odd") for num in range(1,6)}
print(simpleNumber)