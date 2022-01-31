rows = int(input("how many rowa: "))
columns = int(input("how many columns: "))

for i in range(rows):
    for j in range(columns):
        print("*", end="")
    print()

k = 0
for i in range(1,5):
    for space in range(1, (5-i)):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()