import sys

try:
    x = int(input("x:  "))
    y = int(input("y:  "))
except ValueError:
    print("Error: Invalid input.")
    # exit the program
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # exit the program
    sys.exit(1)


print(f"{x} / {y} = {result}")