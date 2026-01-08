# tuples 
tup = ('Junaid', "Nawaz")
# tup[0] = 'Basith' cant do this because tuples are immutable
print(tup)

# tup
tup = ("Geeks", "For", "Geeks", "Geeks", "Geeks", "Geeks")
print(tup[1:])
print(tup[1:4])

# concatenation
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')

tup3 = tup1 + tup2
print(tup3)

# reversing a tuple 
print(tup1[::-1])

# deleting a tuple 
# IMPORTANT WE CANNOT DELETE TUPLE BECAUSE IT IS IMMUTABLE
tup = (0,1,2,3,4,5)
del tup                 # deletes the tuple 


# Unpacking with asterisk
tup = (1,2,3,4,5,6)
a , *b , c = tup
print(a)
print(b)
print(c)
