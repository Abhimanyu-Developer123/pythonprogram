def revno(no):
    s=0
    while no!=0:
        r=no%10  
        s=s*10+r  
        no=no//10  
    return s

print("enter a number")
no = int(input())
print("revers number =", revno(no))
