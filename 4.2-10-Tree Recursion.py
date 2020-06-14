''' Order of recursion '''
def cascade(n):
    if n < 10:           # Base statement can help to understand
        print(10)
    else:
        print(n)
        cascade(n//10)
        print(n)

def cascade(n):
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)


''' Inverse cascade '''
def Inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)
def f_then_g(f, g, n):
    if n :
        f(n)
        g(n)
grow = lambda n:f_then_g(grow, print(n), n//10 )
shrink = lambda n:f_then_g(print, shrink, n//10)

''' Tree Recursion '''
def fiboncci(n):
    if n == 0:
        return 0
    elif n == 1 :
         return 1
    else:
        return fiboncci(n-2) + fiboncci(n-1)

''' Counting Patitions '''
def count_patitions(n,m):
    if n == 0:
        return 1
    elif n < 0 :
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_patitions(n-m , m)
        without_m = count_patitions(n, m - 1)
        return with_m + without_m
