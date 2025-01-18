
class Rectangle:
	def __init__(s,p,q):  #constructor
		s.L=p   #L datamember
		s.B=q
	def show(s):  #show method
		print("length=",s.L)
		print("breadth=",s.B)
	def area(s):   #area Method
		print("area of rectangle=",s.L*s.B)
	def perimeter(s):  #method
		return 2*(s.L+s.B)
r=Rectangle(10,12)  # r object refernce 
r.show()
r.area()
print("perimeter=",r.perimeter())



