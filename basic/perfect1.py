r=int(input("enter a number"))
for no in range(1,r+1,1):
	s=0
	d=1
	while d<=no//2:
		if no%d==0:
			s=s+d
		d=d+1
	if no==s:
		print(no,"is perfect number")
	else:
		print(no,"is not perfect number")