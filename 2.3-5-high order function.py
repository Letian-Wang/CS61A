'''higher-order function: receive function or return function '''
def apply_twice(f, x):
    return f(f(x))
def sqaure(x):
    return x*x
apply_twice(sqaure, 3)

''' Example '''
def make_adder(n):
    def adder(k):
        return k + n
    return adder
add_three = make_adder(3)
add_three(4)

'''Example '''
def square(x):
    return x * x
def triple(x):
    return 3 * x
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
squiple = compose1(square, triple)
squiple(5)
squadder = compose1(square, make_adder(2))
squadder(3)
compose1(square, make_adder(2))(3)

''' lambda function '''
sqaure = lambda x: x * x
square(4)

b = lambda x: lambda: x
c = b(88)
c()

(lambda x: x + 1)(0)
(lambda: 3)()

func1 = lambda f: f(2)
func1(square)

no return, easy function, no loop