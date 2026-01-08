# functions 
def fun():
    print("Welcome to GFG")

fun()


def evenOdd(x):
    if x % 2 == 0:
        print("Is Even")
    else:
        print('Is Odd')
    return

evenOdd(12)
evenOdd(11)

# default parameter 
def default(x,y=50):
    print(x,y)
    return

default(10,20)
default(10)        # Takes default value y = 50 here 

# Keyword Arguments
def student(fname, lname):
    print(fname,lname)
    return
# Takes arguments with values assigned to parameters/arguments
student(fname='Junaid',lname='Nawaz')
student(lname='Nawaz',fname='Junaid')


# Positional Arguments 
def employee(name, age):
    print('Hi Iam',name)
    print('My age is',age)

print("Case-1:")
employee('Junaid',27)

print('\nCase-2:')
employee(29,'Suraj')


# Arbitrary Arguments 
def myFun(*args, **kwargs):

    print(args,kwargs)
    # creates tuples if *
    print(type(args))
    # creates a dictionary if **
    print(type(kwargs))

myFun('Hey','Welcome',first='Junaid',last='Nawaz')


# functions within functions 
def f1():
    s = 'Junaid Nawaz' 
    # f2 can access the variable of the outer function like a closure in javascript
    def f2():
        print(s)
    f2()
f1()

#lambda functions 
# normal function
def cube(x):
    return x * x * x
print(cube(3))

#lambda function
volume = lambda x : x * x * x
print(volume(3))


#pass by reference
def modify(arr):
    arr[0] = 20

lst = [10,11,12,13]
modify(lst)
print(lst)

def modify2(x):
    x = 20
a = 10
modify2(a)
print(a)



#recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))

# fibonacci 
def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)
print(fibonacci(10))



# lambda functions 
s1 = 'geeksforgeeks'
s2 = lambda x: x.upper()
print(s2(s1))


n = lambda x: "Positive" if x > 0 else "Negetive" if x < 0 else 'Zero'
print(n(3))
print(n(-2))
print(n(0))



# lambda with list 
li = [lambda arg = x: arg * 10 for x in range(1,5)]
# these are like 5 functions in list which can be executed if function is called 
for i in li:
    print(i())


calc = lambda x, y: (x+y, x*y)
print(calc(5,10))

# using filter with lambda function
n = [1,2,3,4,5,6]
even = filter(lambda x : x%2 == 0,n)
print(list(even))


# using map with lambda function
n = [1,2,3,4,5]
b = map(lambda x : x * 20,n)
print(list(b))


from functools import reduce
# using reduce 
a = [1,2,3,4,5]
b = reduce(lambda x, y: x * y,a)
print(b)
