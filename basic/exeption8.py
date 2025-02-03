try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except (ValueError, ZeroDivisionError) as e:
    print("Error occurred:", e)
else:
    print("Result:", result)