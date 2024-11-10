def display(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Calling with both positional and keyword arguments
display(1, 2, 3, name="Abhimanyu", age=13)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Abhimanyu', 'age': 13}