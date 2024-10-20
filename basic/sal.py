#wap take emp sal from keyboad if sal>=5000 da=30% hra=20% 
#then display basic sal da hra totalsal
print("enter basic sal")
sal=float(input())
da,hra=0,0
if sal>=5000:
    da=sal*0.3
    hra=sal*0.2
total=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("totals al=",total)