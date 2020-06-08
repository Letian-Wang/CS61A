''' Recursion '''
def split(n):
    return n//10, n%10
def sum_digits(n):
    if n < 10:                                                  # Base condition
        return n
    else:                                                       # Recursion condition
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

Iteration: Using while 
Recursion: Using Recursion

''' Verify recursion '''
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
1. Verify the base case
2. Treat as a functional abstraction
3. Assume that fact(n-1) is correct
4. Verify that fact(n) is correct, assuming that fact(n-1) correct

'''Mutual recursion'''
def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last
def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digits = sum_digits(2 * last)
    if n < 10:
        return luhn_digits
    else:
        return luhn_sum(all_but_last) + luhn_digits

''' Converting Recuision to iteration '''
# Figure out what state must be maintained by the iterative fucntion
def sum_digits_iter(n):
    digit_sum = 0 
    while n > 0:
        n, last = split(n)
        digit_sum = digit_sum + last
    return digit_sum
''' Converting iteration to Recursion '''
# The state of an iteration can be passed as arguments
def sum_digits_rec(n, digit_sum):
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits_rec(n, digit_sum + last)