def checkPrime(number):
    if number <= 1:
        return None
    else:
        for i in range(2, int(number/2)+1):
            if number%i==0:
                print(f"{number} is not Prime")
                break
        else:
            print(f"{number} is Prime ")



number = int(input("Enter a number : "))
checkPrime(number)

