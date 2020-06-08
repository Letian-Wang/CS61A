''' Mutable Functions '''
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance            # Declare the name 'balance' nonlocal at the top of the body of the function in which it is re-assighed
        if amount > balance:
            return 'Insufficient funds'
        balance -= amount           # Re-bind balance in the first non-local frame in which it was bound previously
        return balance
    return withdraw
withdraw = make_withdraw(100)
withdraw(10)

''' Non-local Assignment '''
# refers to first non-local frame
def make_withdraw(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] -= amount           # Re-bind balance in the first non-local frame in which it was bound previously
        return balance
    return withdraw
withdraw = make_withdraw(100)
withdraw(10)

''' Referential Transparency '''
# Expressions are referentially transparent if substituting an expression with its value does not change the meaning of a program
def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x += 1
            return x + y + z
        return h
    return g
a = f(1)
b = a(2)
total = b(3) + b(4)




