class Student:
	def set(self):
		print("enter name rollno and mark ")
		self.name=input()
		self.rollno=int(input())
		self.mark=float(input())
	def disp(self):
		print("name=",self.name)
		print("rollno=",self.rollno)
		print("mark=",self.mark)
s=Student()
s.set()

s1=Student()
s1.set()
s.disp()
s1.disp()
