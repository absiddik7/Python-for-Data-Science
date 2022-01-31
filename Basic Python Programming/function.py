def sum(a,b):
    sum = a+b
    return sum

r = sum(20,45)
print(r)

def fruit_shop(fruit):
    for i in fruit:
        print(i)

all_fruits = ["apple","cherry","banana","mango"]
fruit_shop(all_fruits) # passing a list as an arguments


def hello(first,middle,last):
    print("Your name is: " +first+" "+middle+" "+last)

hello(middle ="Siddik", first="Abubakkar",last="Sajib") # keyword agruments

def nested_function(num): # nested function call
    x = abs(num)
    y = round(x)
    print(y)

nested_function(-3.14)

# Use *args if you don't know how many arguments that will be passed into your function
# This way the function will receive a Tuple of arguments

def add(*num): # use * for get the unknows numbers of arguments
    sum = 0
    for i in num:
        sum += i
    return sum

print(add(2,3,6,9))

# Use **args if you don't know how many keyword arguments that will be passed into your function
# This way the function will receive a dictionary of arguments

def phone(**details):
    print("About New Phone- " + "Brand: " + details["brand"] + ", Name: " + details["name"] + ", Price: " + str(details["price"]))

    for key,value in details.items():
        print(value,end=" ") # print all the value

phone(brand="apple", name="iPhone12", price = 990)


