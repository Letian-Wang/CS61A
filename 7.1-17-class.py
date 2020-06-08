''' Classes '''
class Clown:
    nose = 'big and red'
    def dance(self):
        return 'No thanks'

''' Object construbtion '''
class Account:
    def __init__(self, account_holder):         # Construbtor
        self.balance = 0
        self.holder = account_holder

a = Account('Jim')
b = Account('Jack')
c = a
c is a

''' Methods '''
class Account:
    def __init__(self, account_holder):         # Construbtor
        self.balance = 0                        # Instance attributes
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient fund'
        self.balance = self.balance - amount
        return self.balance

''' Invoking methods '''
tom_account = Account('Tom')
tom_account.deposit(100)

''' Dot expressions '''

''' Attributes '''
john = Account('John')
john.balance
getattr(john, 'balance')
hasattr(john, 'balance')

''' Methods and Functions '''
type(Account.deposit)                   # function
type(tom_account.deposit)               # method
Account.deposit(tom_account, 1001)
tom_account.deposit(1000)

''' Class attributes '''
class Amount:
    interest = 0.02                     # class attributes, shared in all instances
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
