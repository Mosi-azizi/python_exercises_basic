def anagramStrings(string1,string2):
    chars = []
    for i in string1.lower():
        if i not in string2:
            print("strings are not anagram")
            break
        else:
            chars.append(i)
    if chars == list(string1):
        print("strings are anagram")     
        

string1 = "abcde"
string2 = "bcaed"
anagramStrings(string1,string2)
#print(checkAnagram)