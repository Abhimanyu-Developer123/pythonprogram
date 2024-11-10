print("enter total amount")
am=int(input())
amount=am
print("enter deposit")
no1=int(input())
print("enter withdraw")
no2=int(input())
def deposit(amt):
	global amount
	amount=amount+amt 
	print(amt,"deposit")
def withdraw(amt):
	global amount 
	amount=amount-amt 
	print(amt,"withdraw")
print("balance=",amount)
deposit(no1)
withdraw(no2)
print("balance=",amount)