a=10
def show():
	global a
	a=30
	print(a) #global a display 30
def disp():
	print(a)  #30
	print("hi")
show()
disp()
print(a)   #30