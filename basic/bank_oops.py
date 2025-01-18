class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):  # Constructor
        self.account_number = account_number  # Account number
        self.account_holder = account_holder  # Account holder name
        self.balance = initial_balance  # Initial balance

    def deposit(self, amount):  # Deposit method
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):  # Withdraw method
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):  # Check balance method
        print(f"Current balance: ₹{self.balance}")

# Example Usage
account = BankAccount(123456789, "John Doe", 10000)  # Create an account with initial balance ₹1000

print("\n--------- Banking System ---------")
account.check_balance()  # Check initial balance
account.deposit(5000)  # Deposit ₹5000
account.withdraw(2000)  # Withdraw ₹2000
account.withdraw(2000)  
account.check_balance()  # Check final balance
