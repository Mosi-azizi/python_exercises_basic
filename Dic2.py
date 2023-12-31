from traceback import print_tb


myDic = {"name": "Sam", "family": "Azizi", "age": 40,"email":"kassit.azizi@gmail.com"}

if "email" in myDic:
    print(myDic["email"])
else:
    print("there is not email in myDis")

isExist = "Sam" in myDic.values()
print(isExist)

print(myDic)
print("-----------------")
# myDic.clear()
# copymyDic = myDic.copy()
# print(copymyDic)
# print(myDic == copymyDic)
# print(myDic is copymyDic)
# myDic2 = {"name":"unKnown", "Family":"unKnown"}
# myDic2_copy = dict.fromkeys(["name","family"],"unKnown")
# print(myDic2)
# print('--------------------')
# print(myDic2_copy)

print(myDic["family"])
print(myDic.get("family"))

isExist = myDic.get("phone")
print(isExist is None)
