def perfect(no):
    s=0
    d=1
    while d<=no//2:
        if no%d==0: 
            s=s+d
        d=d+1  
    if no==s:
        return "perfect"
    else:
        return "not perfect"
    

print("Enter a number")
no=int(input())
result=perfect(no)
print(no,"is",result,"number.")
