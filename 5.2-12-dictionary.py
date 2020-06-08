''' Data Abstaction '''
pair = [1,2]
x,y = pair                                              # Unpacking

pair[0]                                                 # Selection operator

from operator import getitem                            # Selection function
getitem(pair, 0)

from math import gcd                                    # 最大公约数

Abstraction Barriers
Data Representation

''' Dictionaries '''
# unordered
# lists and dictionaries cannot be keys
numerals = {'I':1, "V":5, 'X':10} 
numerals['X']
numerals.keys()
numerals.values()
numerals.items()

items = [('I', 1), ('V', 5), ('X', 10)]
dict(items)

'X' in numerals
numerals.get('X', 0)                                # Default 0

square = {x:x*x for x in range(10)}
square[7]


