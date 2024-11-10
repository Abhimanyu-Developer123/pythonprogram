def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling with varying keyword arguments
print_info(name="Abhimanyu", age=13, city="Bhubaneswar")
# Output:
# name: Alice
# age: 30
# city: New York
print_info(vechical="Car",brand="BMW", model="X1", year=2024)
# Output:
#vechical:Car
# brand: Toyota
# model: Corolla
# year: 2020