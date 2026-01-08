# For loop 

n = 5
for i in range(1,n):
    print(i)

# loop for arrays / lists
li = ['geeks','for','geeks']
for x in li:
    print(x)

# tuple using for 
tu = ('geeks','for','geeks')
for x in tu:
    print(x)

# string for 
s = 'abc'
for i in s:
    print(i)

# dict for 
d = dict({'x':123,'y':354})
for i in d:
    print(i,d[i])

# set for 
set = {10,20,30}
for x in set:
    print(x)

# iterating using indexes - i takes indexes
li = ["Junaid",'is','best']
for i in range(len(li)):
    print(li[i])

# while loop 
cnt = 0

while(cnt < 3):
    cnt = cnt + 1
    print("Hello")

# while loop 
flag = False 
n = 0
while flag == False:
    n = n+1
    if n == 10:
        flag = True
    print('Hello')

# Nested Loop 
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()


# break and continue 

for letter in 'geeksforgeeks':
    if letter == 's' or letter == 'e':
        continue
    print('Current letter: ',letter)


for letter in 'geeksforgeeks':
    if letter == 's' or letter == 'e':
        break
    print('Current letter: ',letter)
    