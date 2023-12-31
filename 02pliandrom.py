""" def stringPlaindrome(myString):
   mystring = myString.replace(" ","").lower()
   return  mystring== mystring[::-1]

getWord = input("please enter the string: ")
if stringPlainfrom(getWord):
    print("Yes")
else:
    print("NO") """
    
def strPlaindrome(myString):
    myString = myString.replace(" ","").lower()
    if myString == myString[::-1]:
        print("string's Plaindrome is Yes {} ".format(myString))
    else:
        print("string's Plaindrome No")

word = input("Enter the wrod or phrase: ")
strPlaindrome(word)