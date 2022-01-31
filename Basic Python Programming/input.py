name = input("what is your name: ") #take input as string
age = int(input("what is your age: ")) # take int input
height = float(input("How tall are you: ")) # take float input


print("Your name is " + name)
print("your are " +str(age) + "years old")
print("You are " +str(format(height,'.2f')) + " inche tall") # format(height,'.2f') give 2 digits after the point
