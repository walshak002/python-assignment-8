"""
TASK: Create a BankAccount class.

Requirements:
1. Each account should have an owner name and a starting balance.
2. Provide a method to deposit money.
3. Provide a method to withdraw money (only if sufficient balance).
4. Provide a method to check current balance.

Example Usage:
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # 1300
"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposite_money(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount}. New balance: {self.balance}"
    def withdraw_money(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        if amount <= 0:
            return "Withdrawal amount must be positive"
        self.balance -= amount
        #return "Withdraw: {amount}. New balance is: {self.balance}"
    
    def get_balance(self):
        return f"Balance for {self.owner}: {self.balance}"

        
account1 = BankAccount("Alice", 1000)
print(account1.get_balance())

print(account1.deposite_money(500))
print(account1.withdraw_money(200))

print(account1.get_balance())
