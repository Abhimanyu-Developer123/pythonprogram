#wap take emp sal from keyboad if sal>=5000 da=30% hra=20% if sal<5000 da=20% hra=10%
#then display basic sal da hra totalsal
print("enter a salary ")
sal=float(input())
if sal>=5000:
    da=sal*0.3
    hra=sal*0.2
else:
    da=sal*0.2
    hra=sal*0.1
total=sal+da+hra
print("basic salary=",sal)
print("da=",da)
print("hra=",hra)
print("total sal=",total)