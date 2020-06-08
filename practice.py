def product(n, f):
    total, cur = 1, 1
    while cur <= n:
        total, cur = total * f(cur), cur +1
    return total

def lambda_curry2(func):
    func1 = lambda arg2: lambda arg1 :func(arg1, arg2)
    return func1
from operator import add, mul, mod
curried_add = lambda_curry2(mul)
add_three = curried_add(3)
print(add_three(5))

def both_path(sofar="S"):
    print(sofar)
    def func1():
        both_path(sofar + "L")
    def func2():
        both_path(sofar + "R")

    return func1, func2

def compose1(f, g):
    def func1(x):
        return f(g(x))
    return func1
    # return lambda x: f(g(x))

def composite_identity(f,g ):
    def func1(x):
        return f(g(x))==g(f(x))
    return func1
    # return lambda x:f(g(x))==g(f(x))

def count_digits(n):
    count = 0
    while(n // 10 =！ 0):
        n = n // 10
        count

foo = lambda x: lambda y: lambda z:x+y+z

def square(x):
    return x*x
def high(fun):
    def func1(y):
        return fun(fun(y))
    return fun1

def func1(b):
    return b*b
def func2(f,a):
    return f(a)
a = func2(func1, 2)

def ordered_digits(x):
    last = 10
    while (x > 0 and last >= x % 10):
        now = x % 10
        if now < last:
            return False
        last = now
    return True

def num_sevens(x):
    if x > 0:
        return num_sevens(x//10) + (1 if x%10 == 7 else 0)
    else 
        return 0
    count = 0 
    while x > 0:
        if x % 10 == 7 :
            count = count + 1
        x = x // 10
    return count

def count_change(total):
    if total == 0:
        return 0
    if total == 1:
        return 1
     

    return 

def skip_add(n):
    if n <= 0:
        return 0
    else:
        return skip_add(n-2) + n 

def summation(n, f):
    if n == 0 :
        return 0
    else:
        return f(n) + summation(n-1, f)

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if a%b == 0:
        return b
    else
        return gcd(b, a%b)

def paths(m, n):
    if m == 1 or n == 1:
        return 1
    else 
        return paths(m-1, n) + paths(m, n-1)

def max_subseq(n, l):
    if l == 0 or n == 0:
        return 0
    
    
