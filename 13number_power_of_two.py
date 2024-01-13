def numberPowerofTwo(n):
    if n <= 0:
        return False
    return n & (n-1) == 0
n = int(input("please enter a number  :"))

if numberPowerofTwo(n):
    print("number is power of two")
else:
    print("number is not power of two")