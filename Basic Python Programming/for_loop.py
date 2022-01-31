for i in range(0,9,1): # iritate from 0 to 9 and increment by 1 
    print(i)

name = "abubakkar siddik sajib"
for i in name:
    if "sajib" in name:
        print(i)

fruits = ["apple","banana","cherry"]
for i in fruits: 
    if i == "banana": # do not print banana
        continue
    print(i)

for i in range(1,9):
    print(i)
else:
    print("loop finished") # else estatment in for loop

color = ["red","yellow","pink"]
fruit = ["apple","banana","cherry"]

for x in color:
    for y in fruit:
        print(x,y)

number = "123-456-7890"
for i in number:
    if i == "-":
        continue # the number will print without the -
    print(i, end="")

for i in range(5,20):
    if i == 12:
        pass # the 12 will be skip
    else:
        print(i)