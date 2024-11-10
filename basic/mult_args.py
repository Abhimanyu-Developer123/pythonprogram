def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply(1))  
print(multiply(1, 2))             
print(multiply(1, 2, 3))     
print(multiply(1, 2, 3, 4))       
print(multiply(1, 2, 3, 4, 5)) 
print(multiply(1, 2, 3, 4, 5, 6))
print(multiply(1, 2, 3, 4, 5, 6, 7))
print(multiply(1, 2, 3, 4, 5, 6, 7, 8))
print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))