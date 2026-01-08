# # create dictionary
# d1 = {1: 'Junaid', 2: 'Harsh', 3: 'Aamir'}
# print(d1)

# # create using dictionary constructor
# d2 = dict(a = "Junaid", b = 'Harsh')
# print(d2)

# # Accessing dictionary Items
# d = {"name":"Junaid",1:'Python',(1,2):[1,2,3,4]}
# print(d['name'])
# print(d.get('name')) # does the same thing 

# # Adding and deleting in dictionary
# d = {1:"Junaid", 2:"Basith"}
# print(d)
# # add a new key-value
# d[3] = 'Harsh'
# d['don'] = 'Gafoor'
# # update
# d[2] = 'Aamir'
# print(d)

# # Removing from dictionary items
# d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}
# del d['age']
# print(d)

# # pop method pop(key)
# d['name']='Junaid'
# print(d)
# val = d.pop('name')
# print(val)
# print(d)

# # popitem()
# d.popitem()
# print(d)

# # clears all dictionary
# d.clear()
# print(d)

# iterating dictionary
d = {1: 'Geeks', 2: 'For', 'age':22}
for key in d:
    print(key)

# Iterate over values 
for value in d.values():
    print(value)

# Iterate Key value
for key,value in d.items():
    print(key, value)

