class Student:
	def set(self,n,r,m):
		self.name=n
		self.rollno=r
		self.mark=m
	def disp(self):
		print("name=",self.name)
		print("rollno=",self.rollno)
		print("mark=",self.mark)
s=Student()
s.set("abhi",1,90.50)
s.disp()
s1=Student()
s1.set("ayush",2,80.50)
s1.disp()
