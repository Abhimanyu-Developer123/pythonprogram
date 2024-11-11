def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is about to be called.")
        result = func(*args, **kwargs)  
        print("Function has been called.")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Abhimanyu")
