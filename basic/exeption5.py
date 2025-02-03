
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x // y
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Enter a number.")
else:
    print("Result:", result)