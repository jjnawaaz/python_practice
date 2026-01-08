# Use map() to print squares of numbers 1–10.
squares = map(lambda x : x * x, range(1,11))
print(list(squares))

# Use filter() to print only even numbers from 1–50.
even = filter(lambda x: x % 2 == 0, range(1,51))
print(list(even))

# Use reduce() to find product of numbers 1–5.
from functools import reduce
reduced = reduce(lambda x,y: x + y,range(1,6))
print(reduced)

# Use lambda to check if a number is divisible by 7.
check = lambda x: True if x % 7 == 0 else False 
print(check(14))