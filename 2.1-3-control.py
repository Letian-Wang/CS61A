print(print(1), print(2))

from operator import mod
mod(2019 / 10)

def divide_exact(n,d):
    return n // d, n % d
quotient, remainder = divide_exact(2013, 10)

def divide_exact(n,d=10):
    return n // d, n % d

python -m doctest - file.py             # run document test

if:
elif:
else:

False values in python : False, 0, '', None
True  values in python : anything else