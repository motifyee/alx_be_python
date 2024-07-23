
class BankAccount:
    def __init__(self, account_balance=0.0) -> None:
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        self.account_balance -= amount
        return self.account_balance >= amount

    def display_balance(self):
        print(f"Current Balance: ${round(self.account_balance, 2)}")
