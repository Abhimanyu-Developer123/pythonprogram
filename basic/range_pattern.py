


#11
#121
#1231
#12341



for i in range(1,5,1):
	for j in range(1,i+1,1):
		print(j,end="")
	print("1")

print("\n")

#11
#112
#1123
#11234

for i in range(1,5,1):
	print("1",end="")
	for j in range(1,i+1,1):
		print(j,end="")
	print()


print("\n")


for i in range(1,5,1):
	print(i,end="")
	for j in range(1,i+1,1):
		print(j,end="")
	print()

#11
#212
#3123
#41234
print("\n")

#   1
 # 12
 #123
#1234

for i in range(1,5,1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	print()

#1234
# 123
 # 12
  # 1


print("\n")




for i in range(4,0,-1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	print()


#1234321
 #12321
  #121
   #1

print("\n")

for i in range(4,0,-1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")	
	print()


print("\n")

#1234321
 #12321
  #121
   #1
   #1
  #121
 #12321
#1234321

for i in range(4,0,-1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()
for i in range(1,5,1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")	
	print()


print("\n")

#ABCDCBA
 #ABCBA
  #ABA
   #A

for i in range(68,64,-1):
	for j in range(68-i,0,-1):
		print(end=" ")
	for j in range(65,i+1,1):
		print(chr(j),end="")
	for j in range(i-1,64,-1):
		print(chr(j),end="")
	print()