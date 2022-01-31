food = ["rice","water","chicken","pizza"] #list

# 11-methods of list
food.append("cake") # add item at the last index
food.remove("rice") # remove the item from the list
food.pop() # remove the last item from the list
food.insert(1,"burger") # inser item at given index
food.sort() # sort the list by Ascending order
food.reverse() # sort the list by Descending order
#food.clear() # clear all the item from list

for i in food:
    print(i)


ind = food.index("chicken") # return the index of the value
x = food.count("water") # return the no of times the value appears
y = food.copy() # retun the copy of the list
print(ind) 
print(x) 
print(y) 


fruits = ["apple","banana","cherry"]

food.extend(fruits) # add fruits list to the food list

for i in food:
    print(i)

