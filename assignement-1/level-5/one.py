# Factorial using recursion.
def fact(num):
    if num == 1:
        return 1
    return num * fact(num - 1)
print(fact(5))

# Sum of digits
def SumOfDigits(x):
    if len(str(abs(x))) == 1:
        return x
    lastDigit = x % 10
    digit = x // 10
    return lastDigit + SumOfDigits(digit)
print(SumOfDigits(321))


def SumOfDigits2(x):
    if x < 10:
        return x
    lastDigit = x % 10
    digit = x // 10
    return lastDigit + SumOfDigits(digit)
   
print(SumOfDigits2(321567))


# power using recursion
def power(a, b):
    if b == 1:
        return a * b
    return a * power(a,b-1)
print(power(4,2))