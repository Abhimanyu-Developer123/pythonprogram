
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a // b)  # Possible ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
