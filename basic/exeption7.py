
class NegativeNumberError(Exception):
    pass
class CharacterEnterError(Exception):
    pass 

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    
    print("Valid input:", num)
except NegativeNumberError as e:
    print("Error:", e)
