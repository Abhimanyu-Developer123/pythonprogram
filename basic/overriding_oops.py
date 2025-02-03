class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Example Usage
animals = [Animal(), Dog(), Cat()]

for animal in animals:
    print(animal.speak())