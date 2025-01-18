class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name:{self.name},Age:{self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, major):
        # Call the parent class constructor to initialize common attributes
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major

    def display_student_info(self):
        # Use parent class method to display common information
        self.display_info()
        print(f"Student ID: {self.student_id}, Major: {self.major}")

# Usage
student = Student("Alice", 20, "S12345", "Computer Science")
student.display_student_info()
