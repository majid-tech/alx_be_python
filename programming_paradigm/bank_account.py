
class BankAccount:
    def __init__(self,  account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
    
    def withdraw(self, amount):
        if self.account_balance > amount:
            self.account_balance -= amount
        else:
            return f'account balance is less than amount'

    def display_balance(self):
        print(f'Account balance: {self.account_balance}')

