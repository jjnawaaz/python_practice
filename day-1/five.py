
# conditional statements in python 

age = 100
if age <= 12:
    print('Travel for free')
else:
    print("Pay for ticket")


# Short hand for if else 
marks = 35 
res = "Pass" if marks >= 40 else "Fail"
print("Result: "+res)


# elif statements 
age = 25
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <=35:
    print("Adult")
else:
    print("Old")

# match similar to switch 
number = 2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or three")
    case _:
        print("Other number")


# nested if else 
age = 70 
is_member = True

if age >= 60:
    if is_member:
        print("Is a member")
    else:
        print("Not a member")
else:
    print('Not eligible for being a member')