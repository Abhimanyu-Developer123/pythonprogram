print("enter a number")
no=int(input())
c=0
d=2
if no==0 or no==1:
	print(no,"not prime")
else:
	while d<=no//2:
		if no%d==0:
			c=c+1
			break
		d=d+1
	if c==0:
		print(no,"is prime number")
	else:
		print(no,"is not prime number")