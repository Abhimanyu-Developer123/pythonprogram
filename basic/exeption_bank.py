class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance."""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit successful! New balance: {self.balance}")

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientFundsError("\nInsufficient funds! Withdrawal not allowed.\n")
            self.balance -= amount
            print(f"\nWithdrawal successful! New balance: {self.balance}")
        except InsufficientFundsError as e:
            print("Error:", e)

# Creating a bank account with ₹5000 balance
account = BankAccount(10000)

# Trying to withdraw ₹7000 (more than balance)
account.withdraw(7000)  # This should raise an exception

# Trying to withdraw ₹3000 (valid transaction)
account.withdraw(3000)  # Successful transaction

# Depositing ₹2000
account.deposit(20000)
