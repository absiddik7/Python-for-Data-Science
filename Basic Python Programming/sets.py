# set is a collection which is unordered, unindexed. Duplicate values will be ignored

meal = {"rice","carry","fish","water","lemon"}
fruits = {"apple","orange","lemon","banana"}

meal.add("sweet") # add new item in the set
meal.remove("water") # remove the given item
#meal.clear() # clear the set
#meal.update(fruits) # add item of fruits set to meal set

dinner_menu = meal.union(fruits) # create new set by join 2 sets
for i in dinner_menu:
    print(i)

print()
for i in meal:
    print(i)

print(meal.difference(fruits)) # what do meal have that fruits doesn't
print(meal.intersection(fruits)) # find the common item from both
print(len(meal)) # print the length of the set
print(type(meal)) # print the data type of the set

# Using set() constructor to make a set
newset = set(("cherry","mango"))
print(newset)

