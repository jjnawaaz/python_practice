# Take a number and check if it is palindrome (no strings allowed).
number = int(input("Enter a number: "))
def isPalindrome(num):
    rev = int(str(num)[::-1])
    if num == rev:
        print("It is Palindrome")
        return
    else:
        print("It is not Palindrome")
        return

isPalindrome(number)

# Print first N Fibonacci numbers using loop.
n = 10
sum = 0
firstNumber = 0
lastNumber = 1
print(firstNumber, lastNumber, end=" ")
for i in range(0,n - 2):
    sum = firstNumber + lastNumber
    firstNumber = lastNumber
    lastNumber = sum
    print(sum,end =" ")

# fibonacci using recursion
def fibonacci(num):
    if num == 0:
        return
    print(num)
    return fibonacci(num - 2) + fibonacci(num - 1)
fibonacci(10)