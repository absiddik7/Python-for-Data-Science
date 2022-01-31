import random

x = random.randint(1,5) # randmon int num between 1 to 5
k = random.randrange(2,6) # randmon int num between range
y = random.random() # randmon float num 


print(x)
print(y)
print(k)

myList = ["apple","water","cherry","banana"]
z = random.choice(myList) #randomly choose from the list
print(z)

cards = [1,2,3,4,5,6,"a","b","c"]
random.shuffle(cards) #shuffle the list 
print(cards)

for i in range(10):
    print(random.randint(2,8))


