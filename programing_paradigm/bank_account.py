class BankAccount():

    def __init__(self):
        self.account_balance = 0.0

    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
        
        else:
            print(f"Insufficient funds")
            

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")


