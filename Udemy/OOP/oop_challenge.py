"""
For this challenge, create a bank account class that has two attributes:
owner
balance
and two methods:
deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""


class Account:

    def __init__(self, owner, balance=0):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit {amount} Accepted"

    def withdraw(self, amount):
        res = ''
        if self.balance >= amount:
            self.balance -= amount
            res = f"Withdraw {amount} Accepted"
        else:
            res = "Sorry not enough funds!"
        return res

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'


acct1 = Account('Jose', 100)
print(acct1)

print(acct1.owner)
print(acct1.balance)

print(acct1.deposit(50))
print(acct1.withdraw(75))
