#wap take a number from keyboad check no is 2 digit number
print("enter a number ")
no=int(input())
if no>9 and no<100:
    print("2 digit number ")
elif no>=100:
	print("3 or more than 3 digit number")
else:
	print("1 digit number")