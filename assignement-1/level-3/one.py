# Print numbers from 1 to 20.
for i in range(1,21):
    print(i)

# Print all even numbers between 1 and 50.
for i in range(1,51):
    if i % 2 == 0:
        print(i)

# Print the multiplication table of a number.
number = int(input("Enter your number: "))
for i in range(1,11):
    print(i * number)

# Find the sum of first N natural numbers using a loop.
sum=0
n = int(input("Enter the value of n: "))
for i in range(1,n+1):
    sum = sum + i
print(sum)

# Reverse a number using a loop.
num=int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev*10 + digit
    num = num // 10
print(rev)

# Count how many digits are in a number.
count = 0
number = 12345
for i in range(1,len(str(abs(number)))+1):
    count = count + 1
print(count)


# count steps 
count = 0
number = 12345
if number == 0:
    count = 1
else:
    while number > 0:
        count += 1
        number //= 10
print("Number of digits:", count)