# fibonacci using recursion

def recursion(num):
    if num == 0:
        print(num)
        return 0
    print(num)
    return recursion(num - 1)
recursion(10)

# Print numbers from N to 1 using recursion.
def printNumber(num):
    if num == 1:
        print(num)
        return
    print(num)
    return printNumber(num - 1)
printNumber(10)


# Print numbers from N to 0 but only even numbers.
def printNumber(num):
    if num == 0:
        print(num)
        return
    if num % 2 == 0:
        print(num)
    return printNumber(num - 1)
printNumber(10)


# Print N stars 
def printStars(num):
    if num == 1:
        print('*')
        return
    print('*')
    return printStars(num - 1)
printStars(5)



def printNums(num, n):
    if num == n:
        print(num)
        return
    print(num)
    return printNums(num + 1,n)
printNums(1, 10)

def printNums(num):
    if num == 1:
        print(num)
        return
    printNums(num - 1)
    print(num)
printNums(10)


def printEven(num):
    if num == 0:
        print(num)
        return
    printEven(num - 1)
    if num % 2 == 0:
        print(num)
printEven(10)


def printLine(k):
    if k == 0:
        return
    printLine(k - 1)
    print(k, end="")

def printPattern(n):
    if n == 0:
        return
    printPattern(n - 1)
    printLine(n)
    print()   # move to next line

printPattern(4)
