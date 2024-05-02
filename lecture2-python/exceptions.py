import sys

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    sys.exit(1)

print(f"{x} divided by {y} is {result}")
