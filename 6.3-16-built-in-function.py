''' Iterator '''
# iter()
# next()

s = [3, 4, 5] 
t = iter(s)
next(t)
list(t)

''' Dictionary iteration '''
# Python 3.6+:  Dicionary is ordered
# Python 3.5 and earlier: Dictionary is not ordered
d = {'one':1, 'two':2, 'three':3}
d["zero"] = 0
k = iter(d.keys())      # or iter(d)
next(k)
v = iter(d.values())
i = iter(d.items())

''' For statements '''
r = range(3, 6)
list(r)
for i in r:
    print(i)
ri = iter(r)
for i in ri:        # also move the iterator, during iteration, the structure cannot be changed
    print(i)

''' Built-in functions for iteration: lazy function(need to be called) '''
map(fuc, iterable)                      # Iterate over func(x) for x in iterable
bcd = ['b', 'c', 'd']
m = map(lambda x:x.upper(), bcd)
next(m)
list(m)

filter(func, iterable)                  # Iterate over x in iterable if func(x)
bcd = ['b', 'c', 'd']
m = filter(lambda x:x!='c', bcd)
next(m)
list(m)

zip(first_iter, second_iter)            # Iterate over co-indexed (x, y) pairs
d = {'a':1, 'b':2}
items = zip(d.keys(), d.values())
next()
for i in zip(d.keys(), d.values()):
    print(i)

reversed(sequence)                      # Iterate over x in a sequence in reverse order
t = [1,2,3,2,1]
m = reversed(t)

list(iterable)                          # Create a list containing all x in iterable
tuple(iterable)                         # Create a tuple containing all x in terable
sorted(iterable)                        # Create a sorted list containing x in iterable
b= [4,8,2,8,7,3]
sorted(b, key=lambda x:x) 

''' Generator ''' 
# Generator function can yield multiple times rather than return only once
# Return a iterator over yields
def plus_minus(x):
    yield x
    yield -x
t = plus_minus(3)
next(t)
for i in plus_minus(3):
    print(i)

''' Generators can yield from Iterator '''
def a_then_b(a, b):
    for x in a:
        yield x
    for x in b:
        yield x
def a_then_b(a, b):
    yield from a
    yield from b
list(a_then_b([3, 4], [5, 6]))

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)
    else:
        yield 'Blast off'
for k in countdown(3):
    print(k)        

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s
list(prefixes('both'))        

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
list(substrings('tops'))        