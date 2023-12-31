from traceback import print_tb


dictionary = [{"name": "Sam", "family": "Azizi", "age": 45},
              {"name": "Vahid", "family": "mohamdi","age":35}]

myShopping = dict(name="Sam",family="Azizi")
myDic = {"name": "Sam", "family": "Azizi", "age": 45}
# print(dictionary)
# print("----------------------")
# print(myShopping)

# print(myShopping["name","family"])
# print(myDic.values())
# print(myDic.keys())
# for valu in myDic.values():
#     print(valu)

# for key in myDic.keys():
#     print(key)

# for item in myDic.items():
#     print(item)

print(myDic.values())
print(myDic.keys())
print(myDic.items())

for valu in myDic.values():
    print(valu)

for key in myDic.keys():
    print(key)

for key,valu in myDic.items():
    print(key,valu)


# print((key,valu) for key,valu in myDic.items())
