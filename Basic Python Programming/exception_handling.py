
try:
    x = int(input("Enter a number to divide: "))
    y = int(input("Enter a number to divide by: "))
    result = x/y
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers")
except FloatingPointError as e:
    print(e)
    print("Enter only integer numbers")
except Exception as e:
    print(e)
    print("Something went wrong")
else: # if there is no exception then the result will print
    print(result)
finally:
    print("This will always execute")




