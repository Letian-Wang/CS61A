'''  '''
# Methods is a function and a class attribute
#Instance attributes then Class attributes

''' Attribute Assignment '''
class Account:
    interest = 0.02             # Class interest
    def __init__(self, holder):
        self.holder = holder
        self.balance = 0
tom_account = Account('Tom')
Account.interest = 0.04                 # Class attributes assignment (affect all instances)
tom_account.interest = 0.08             # Instances attributes assignment (add an attribute to instance, not affect class attributes)


''' Inheritance '''
# Look up first in child class, then parent class
class CheckingAccount(Account):
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
a = Account('John')
b = CheckingAccount('Jack')
a.deposit(100)
b.deposit(100)
a.withdraw(10)
b.withdraw(10)

''' Object-oriented design '''

1. Don't repeat, using existing implementations
2. Attributes overridden are still accessible via class objects
3. Look up attributes on instances whenever possible

''' Inheritance and Composition '''
class Bank():
    def __init__(self):
        self.accounts = []
    def open_account(self, holder, amount, kind=Account)
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account) 
        return account
    def pay_interst(self):
        for a in self.accounts:
            a.deposit(a.balance*a.interest)
    def too_big_to_fail(self):
        return len(self.accounts) > 1

''' Attributes Lookup Practive '''

''' Multiple Inheritance '''

''' Compicated Inheritance '''



    
