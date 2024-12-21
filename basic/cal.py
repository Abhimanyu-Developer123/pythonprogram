import math as m
print("Simple 2 digit Calculator!")
no1=int(input("Enter no1:"))
no2=int(input("Enter no2:"))
print("Choose a operation")
print("1.add(addition)")
print("2.sub(subtraction)")
print("3.mult(multiplication)")
print("4.div(division)")
print("5.power")
print("6.rem (remainder)")
op=str(input("Choose a number:"))
if op=="1":
	print(no1+no2)
elif op=="2":
	print(no1-no2)
elif op=="3":
	print(no1*no2)
elif op=="4":
	print(no1//no2)
elif op=="5":
	print(no1**no2)
else:
	print(no1%no2)
