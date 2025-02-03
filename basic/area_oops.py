class Rectangle:
    def area(self, length, breadth):
        return length * breadth

class Circle:
    def area(self, radius):
        return 3.14 * radius ** 2

# Polymorphic Function
def print_area(shape, *args):
    print("Area:", shape.area(*args))

rect = Rectangle()
circle = Circle()

print_area(rect, 10, 20) 
print_area(circle, 5)     
