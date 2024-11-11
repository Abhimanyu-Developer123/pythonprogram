def factorial(no):
	r=1
	while no>0:
		r=r*no
		no=no-1
	return r


print("Enter a number")
no = int(input())
result = factorial(no)
print("Factorial =", result)
