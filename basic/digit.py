print("enter number")
no=int(input())
if no<10:
	print("single digit")
elif no<100:
	print("double digit")
elif no<1000:
	print("triple digit")
else:
	print("other digit")
