s = 'Hello'
s.upper()
s.lower()
s.swapcase()
s
''' string is object'''
from unicodedata import name, lookup
print(lookup('WHITE SMILING FACE'))
print(lookup('WHITE FROWNING FACE'))
lookup('SNOWMAN')
lookup('SOCCER BALL')
lookup('BABY').encode()

''' Mutation Operations '''
suits = ['coin', 'string', 'myriad']
original_suits = suits
suits.pop()                                 # delete the last one
suits.remove('string')
suits
suits.append('cup')
suits.extend(['sword', 'club'])

mutable type: lists, dictionaries, sets
inmutable type: tuple

numerals = {'I':1, 'V':5, 'X':10}
numerals['X'] = 11
numerals['L'] = 50                          # add
numerals.pop('X')

four = [1, 2, 3, 4]
def mystery(s):
    s.pop()
    s.pop()
mystery(four)
len(four)
def another_mystery():
    four.pop()
    four.pop()
another_mystery()

''' Tuples '''
# inmutable content
(3, 4, 5, 6)
3, 4, 5, 6
()
tuple([3, 4, 5])
2,
(2,)
(3, 4) + (5, 6)
5 in (3, 5, 6)

{(1,2):3}                           # tuples can be used as keys of dictionary

# but name can be changed
s = (2,5,8)
s = (8,6,7)

# imutable element can be changed
s = ([1,2], 3)
s[0] = 4                            # Error
s[0][0] = 4                         # Work

''' Sameness and Change '''
''' Identity and Equality '''
a = [10]
b = a
a == b                              # True

a = [10]
b = [10]
a == b                              # True

# Defaul is dangerous
def f(s=[]):
    s.append(3)
    return len(s)
f()
f()
f()


