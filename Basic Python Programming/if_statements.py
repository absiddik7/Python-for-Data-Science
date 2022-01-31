age = int(input("How old are you?: "))

if age >= 18:
    print("you are an adult")
elif age < 0:
    print("you are no a human")
else: 
    print("you are a kid")

temp = int(input("what is the temp today?:"))

if (temp >= 0 and temp <= 30):
    print("The weather is good today.")
elif (temp < 0 or temp > 30):
    print("Bad weather")

name = "abu bakkar siddik sajib"
if "abu" in name:
    print("correct name")
else:
    print("worng name")