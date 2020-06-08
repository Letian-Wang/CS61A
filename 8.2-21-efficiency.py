''' Measuring Efficiency '''
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

''' Memorization '''
def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized

''' Exponentialtion '''                         
def exp(b, n):                                                  # Linear Time
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)

def exp_fast(b, n):                                             # Logarithmic time   
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b, n-1)
def square(x):
    return x * x

''' Orders of Growth '''
Exponential Time
Quadartic Time              # Memorization
Linear Growth               # Exponentialization
Logarithmic Growth
Constant Growth

''' Order of Growth Notation '''

''' Space '''