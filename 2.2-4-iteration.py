''' iteration '''
def fib(n):
    """ Compute fibonachi number """
    pred, curr = 0, 1
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

Function:
1. exactly one job
2. no repeatation
3. generally

python -i file.py

assert 3 > 2, "Math is broken"

''' Use a function name '''
def cube(x) : 
    return pow(x, 3)
def summation(n, term):
    total, k = 0 ,1
    while k < 10:
        total, k = total + term(k), k + 1 
    return total
summation(2,cube)

'''fuction returns a function'''
def make_adder(n):
    def adder(k):
        return k + n
    return adder
make_adder(1)(2)


