def make_adder(x):
    return lambda k: k + x
make_adder(2)(3)


''' Decorator: Transform a function to another one with the same name '''
@trace1
def triple(x):
    return 3 * x

def triple(x):
    return 3 * x
triple = trace1(triple)


''' Review '''
# 1. what would python print
def delay(arg):
    print('delayed')
    def g():
        return arg
    return g
delay(delay)()(6)()

def square(x):
    return mul(x, x)
def pirate(arggg):
    print('matey')
    def pluner(arggg):
        return arggg
    return plunder
add(pirate(3)(square)(4), 1)
pirate((pirate(pirate)))(5)(2)


 