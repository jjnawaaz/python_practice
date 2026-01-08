# Write a function that returns square of a number.
def square(num):
    return num*num
print(square(10))

# Write a function that returns True if a number is prime else False.
def prime(num):
    if num == 0:
        return "Neither prime nor composite"
    if num == 1:
        return "Prime number"
    flag = False
    for i in range(2,num):
        print(i)
        if num % i == 0 and num != i:
            flag = True
    if flag == True:
        return "Composite Number"
    else:
        return "Prime Number"

print(prime(11))

# Write a function to return factorial using loop.
number = 6
fact = 1
for i in range(number, 0, -1):
    print(i)
    fact = fact * i
print(fact)

# Write a function that takes 2 numbers and returns the greater one.
def greater(x , y):
    if x > y:
        print('Largest number is: ',x)
    else:
        print('Largest number is: ',y)
greater(60,30)