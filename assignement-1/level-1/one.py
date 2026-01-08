# Take a number from the user and print its square.
number = int(input("ENTER A NUMBER: "))
print(number*number)

# Take two numbers and print their sum, difference, product and quotient.
x = int(input("Enter number 1: "))
y = int(input("Enter number 1: "))
sum = x + y
diff = x - y
product = x * y
quotient = x / y

print('Sum: ',sum)
print('Difference: ',diff)
print('Product: ',product)
print('Quotient: ',quotient)

# Take a number and print whether it is positive, negative or zero.
number = int(input('Enter your number: '))
func = lambda x : 'Positive' if x > 0  else 'Negative' if x < 0  else "Zero"
print(func(number))

# Take your birth year and print your age.
birthYear = int(input('Enter your birthYear: '))
age = 2025 - birthYear
print(age)


# Swap two variables without using a third variable.
a = 10
b = 20
print(a,b)
[a,b]=[b,a]
print(a, b)