try:
    age = int(input("Enter your age: "))
    assert age >= 18, "Age must be 18 or above"
    print("You are eligible.")
except AssertionError as e:
    print("Error:", e)