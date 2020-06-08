12e12
print(repr(12e12))

from fractions import Fraction
half = Fraction(1,2)
half
repr(half)
print(half)
str(half)
eval(repr(half))

''' Polymorphic Function '''
class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d
    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)
    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)
half = Ratio(1, 2)
print(half)
half

''' Special Method names: built-in behaviors ''''
__init__
__repr__
__add__
__boo__
__float__
zero, one, two = 0, 1, 2
one + two
bool(zero), bool(one)
one.__add__(two)
zero.__bool__()

def gcd(n,d):
    while n != d:
        n, d = min(n, d), abs(n-d)
    return n

def make_dder_inc(n):
    def adder(x):
        nonlocal n
        value = n + c
        n += 1
        return value
    return adder

def make_fib():
    cur, next = 0, 1
    def next_fib():
        nonlocal cur, next
        cur, next = next, cur + next 
    return next_fib

def naturals():
    i = 1
    while True:
        yield i
        i += 1


''' Solutions and homework '''
def scale(it, multiplier):
    for elem in it:
        yield elem * multiplier
def scale(it, multiplier):
    yield from map(lambda x:x*multiplier,it)    

def is_min_heap(t):
    for b in branches(t):
        if label(t) > label(b) or not is_min_heap(b):
            return False
    return True
def largest_product_path(tree):
    if is_leaf(tree):
        return label(tree)
    return max([label(tree)*largest_product_path(b) for b in branches(tree)])

def make_max_finder():
    max_sofar = 0
    def max_finder(lst):
        nonlocal max_sofar
        max_sofar = (max(lst) if max(lst) > max_sofar else max_sofar)
        return max_sofar
    return max_finder

class VendingMachine:
    def __init__(self, product, price):
        self.product = product
        self.stock = 0
        self.price = price
        self.balance = 0
    def vend(self):
        if self.stock < 1:
            return 'Machine is out of stock'
        if self.balance < self.price:
            return 'You must add more funds'.format(self.price - self.balance)
        difference = self.balance - self.price
        message = 'Here is your {0}'.format(self.product)
        if difference > 0:
            message += ' and ${1} change'.format(difference)
        self.stock -= 1
        self.balance = 0
        return message
    def add_funds(self, fund):
        if self.stock < 1:
            return self.vend() + 'Here is your ${0}'.format(fund)
        return 'Currernt balance: &{0}'.format(self.balance + fund)
    def restock(self, stock_number):
        self.stock += stock_number
        return 'Current {0} stock: {1}'.format(self.product, self.stock)
    
def preorder(t):
    if is_leaf(t):
        print(label(t))
    print(label(t))
    (preorder(b) for b in branches(t))

def store_digits(n):
    store = []
    if n < 10:
        store.append(n%10)
        return store
    store.extend([n%10, store_digits(n//10)])
    return store








