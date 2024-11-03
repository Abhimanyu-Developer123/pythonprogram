import sys
print("enter a number")
no=int(input())
f=1
if no<0:
	print("-ve number not allowed")
	sys.exit()
while no>0:
	f=f*no
	no=no-1

print("factorial=",f)