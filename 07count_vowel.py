def countVowel(string):
    vowel = ['a', 'e', 'o', 'u', 'i']
    count = 0

    for i in string.lower():
        for j in vowel:
            if i == j:
                count +=1
    return count

string = input("please enter a string:")
countV = countVowel(string)
print(f"count vowel in {string} is: ", countV)