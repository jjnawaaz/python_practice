# Lists

# create list
a = [1,2,3,4,5,6]
print(a)

# create using list constructor
a = list((1,2,3,4,5))
print(a)

# create multiple items
a = [10] * 5
print(a)

# accesing list elements 
a = [1,2,3,4,5]
print(a[0])
print(a[-1])
print(a[1:4]) # first index and second index - 1 place


# adding elements in the list 
a = []
a.append(10)
print('After appending list: ', a)
a.append(20)
print('After appending list: ', a)
a.append(30)
print('After appending list: ', a)
a.append(40)
print('After appending list: ', a)
a.append(50)
print('After appending list: ', a)

# insert 
a.insert(1,5)
print('After using insert list: ', a)

# extend 
a.extend([60,70,80])
print("After extend: ",a)

# clear
a.clear()
print("After clearing: ",a)

# updating elements in the list 
a = [10, 20, 30, 40, 50]
a[1] = 5                    # lists are mutable 
print(a)

# removing from list 
a = [10,20,30,40,20]
a.remove(20)            # deletes that element from the list only the first occurence
print('After removal: ',a)

# popping from the list
pop_val = a.pop(1)
print(pop_val)
print(a)

# deletes 1st 
del a[0]
print(a)


# iterating over lists
a = ['apple','cherry','blueberry']
for item in a:
    print(item)