
from abc import ABC, abstractmethod

# Define an abstract class
class Animal(ABC):
    @abstractmethod
    def speak(self):
        """Abstract method that must be implemented by subclasses"""
        pass

    def sleep(self):
        """Concrete method available to all subclasses"""
        print("Sleeping...")

# Subclass implementing the abstract method
class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Subclass implementing the abstract method
class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Example Usage
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
    animal.sleep()
