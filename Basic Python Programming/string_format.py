animal = "cat"
item = "box"

#print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal,item))
print("The {0} jumped over the {1}".format(animal,item)) #positional argument
print("The {animal} jumped over the {item}".format(animal = "cow",item = "bed")) #keyword  argument
txt = "The {} jumped over the {}"
print(txt.format(animal,item))
print()

num = 3.14159
x = 1000
y = 1234
print("The number pi is {:.2f}".format(num)) # .2f print 2 digits after decimal
print("The number x is {:,}".format(x)) # this will display a , after 1
print("Binary of y = {:b}".format(y)) # convert to binary
print("Binary of y = {:o}".format(y)) # convert to octal
print("Binary of y = {:x}".format(y)) # convert to hex
print("Binary of y = {:e}".format(y)) # convert to scientific notation


