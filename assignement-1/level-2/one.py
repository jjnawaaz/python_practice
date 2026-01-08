# Take a number and print whether it is even or odd.
number = int(input("Enter a number: "))
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(number))


# Take marks and print:
# Fail if < 40
# Pass if 40–59
# First Class if 60–79
# Distinction if 80+
marks = int(input("Enter your marks: "))
check = lambda x : "Fail" if x < 40 else 'Pass' if x < 60 else 'First Class' if x < 80 else 'Distinction'
print(check(marks))


# Using match, take a number 1–7 and print the weekday number.
number = int(input("Enter a number: "))
match number:
    case 1: 
        print('Monday',number)
    case 2: 
        print('Tuesday',number)
    case 3: 
        print('Wednesday',number)
    case 4: 
        print('Thursday',number)
    case 5: 
        print('Friday',number)
    case 6: 
        print('Saturday',number)
    case 7: 
        print('Sunday',number)
    case _:
        print('Invalid match case')
    

# Take 3 numbers and print the largest.
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))

def largest(x,y,z):
    if x > y and x > z:
        print('Largest number is: ',x)
    elif y > x and y > z:
        print("Largest number is: ",y)
    else:
        print("Largest number is",z)
    return
largest(number1, number2, number3)  


# Check if a number is divisible by both 3 and 5.
number = int(input("Enter a number: "))
def check(num):
    if num % 3 == 0 and num % 5 == 0:
        print('Number is divisible by both 3 and 5')
        return
    else:
        print('Number is not divisible by 3 and 5')
        return  
check(number)