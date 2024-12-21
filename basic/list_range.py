#way to using index concept
#(i)range(start,stop,step)
#(ii)range(start,stop)
#(iii)range(stop)

#(i)

L=[10,20,30,40,50,60,70,80,90,100]
for i in range(0,len(L),2):
  print(L[i])

#(ii)
L=[10,20,30,40,50,60,70,80,90,100]
for i in range(0,len(L)):
  print(L[i])


#(iii)
L=[10,20,30,40,50,60,70,80,90,100]
for i in range(0,):
  print(L[i])