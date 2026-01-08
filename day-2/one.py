# Strings

s1 = "Junaid"
print(s1)

# Multi level strings
s2 = """Junaid nawaz
hi 
there"""
print(s2)


s3 = '''JUnaid same thing with 
single
Quotes'''

print(s3)

# indexes 
print(s1[0]) # first index
print(s1[-1]) #last index
print(s1[-2]) #last index -2
print(s1[3]) #third index


#String slicing 
s = "GeeksforGeeks"

print(s[1:4]) #start from index 1 till 3 before 4
print(s[3:])  #start from index 3 till last

# reverse string
print(s[::-1])


# string iteration
s = "Python"
for char in s:
    print(char)

# strings are immutable 
s = 'junaid Nawaz'
s = 'J' + s[1:]
print(s)


# deleting a string
s = "Junaid"
del s
print(s)


# updating a string using Update
s = "hello Geeks"
s1 = "H" + s[1:]
s2 = s.replace("Geeks", "Junaid")
print(s1)
print(s2)


# string methods
s = 'GeeksforGeeks'
print(len(s)) # len returns len of the string

# uppercase and lowercase
print(s.upper()) 
print(s.lower()) 

s = "   GFG  "
print(s.strip()) # removes leading and trailing whitespace from the string 
s = 'Python is fun and Iam more fun'
print(s.replace('fun','awesome')) # replaces all occurrences of a specified substring with another.

# concatenate strings 
s1 = 'Hello'
s2 = 'World'
s3 = s1 + s2
print(s1+" "+s2)
print(s3)

# repeat string
s = "Hello"
print(s * 4)


# variables inside strings
# f - strings
name = 'Alice'
age = 22
sentence = f"My name is {name}. My age is {age}"
print(f"Name: {name}, Age: {age}")
print(sentence)
