class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Example Usage
calc = Calculator()
print(calc.add(5))          # Calls add(5, 0, 0) -> Output: 5
print(calc.add(5, 10))      # Calls add(5, 10, 0) -> Output: 15
print(calc.add(5, 10, 20))  # Calls add(5, 10, 20) -> Output: 35