
class Bank:
    def __init__(self, bank_name, branch):
        self.bank_name = bank_name
        self.branch = branch

    def display_bank_info(self):
        print(f"Bank Name: {self.bank_name}")
        print(f"Branch: {self.branch}")

class Customer(Bank):
    def __init__(self, bank_name, branch, customer_name, account_number, balance=0):
        super().__init__(bank_name, branch)
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")

    def display_customer_info(self):
        self.display_bank_info()
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

# Usage
customer = Customer("Central Bank of Python", "Uptown", "Alice", "9988776655", 1000)
customer.display_customer_info()

customer.deposit(5000)
customer.withdraw(3000)
customer.withdraw(20000)
