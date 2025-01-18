class Rectangle:
    def __init__(self, a, b): 
        self.L = a  
        self.B = b  

    def show(self):  
        print("Length =", self.L)
        print("Breadth =", self.B)

    def area(self):  
        print("Area of rectangle =", self.L * self.B)

    def perimeter(self):  
        return 2 * (self.L + self.B)

r = Rectangle(5, 6)
r.show()  
r.area()
print("Perimeter =", r.perimeter()) 
