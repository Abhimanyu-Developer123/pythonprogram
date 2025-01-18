
class Square:
    def __init__(self, side):  
        self.side = side  
    def show(self):  
        print("Side =", self.side)
    def area(self): 
        print("Area of square =", self.side*self.side)
    def perimeter(self):  
        print("Perimeter =", 4 * self.side)

print("enter square side:")
s=Square(float(input()))
s.show()  
s.area()  
s.perimeter()