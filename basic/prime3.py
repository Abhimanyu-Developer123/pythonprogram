def prime(no):
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
			return "prime number"
		else:
			return "no prime number"


print("Enter a number")
no=int(input())
result=prime(no)
print(no,"is",result,"number.")