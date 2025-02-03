
def check_age(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old.")
    print("Access granted!")

try:
    check_age(int(input("Enter your age:")))
except ValueError as e:
    print("Error:", e)
