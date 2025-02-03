
try:
    num_list = [10, 20, 30]
    print(num_list[5])  # IndexError
    try:
        print(10 // 0)  # ZeroDivisionError
    except ZeroDivisionError:
        print("Cannot divide by zero!")
except IndexError:
    print("Index out of range!")
    