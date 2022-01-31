#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

fruits = ("apple","banana","cherry","apple","cherry")
print(fruits)
print(len(fruits)) # print the length of the tuple

oneItemTuple = ("Orange",) # for 1 item tuple, the ',' is mandatory
print(type(oneItemTuple))

mixedTuple = ("abc",12,True,"apple") # tuple can store different data at a time
print(mixedTuple)

# Using tuple() method to make tuple
thisTuple = tuple(("apple","orange"))
print(thisTuple)