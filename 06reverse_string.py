def revString(string):
    string = string[::-1]
    return string

string = input("please enter a string:")
rev = revString(string)
print(rev)

def revStr(myString):
    replceStr=myString.replace(" ",'')
    myString = replceStr[::-1]
    return myString

myString = input("please enter a string:")
revRep = revStr(myString)
print(revRep)