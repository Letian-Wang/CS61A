'''return'''
def print_all(x):
    print(x)
    return print_all
print_all(1)(5)(8)


def print_sum(x):
    print(x)
    def next_sum(y):
        return print_sum(x+y)
    return next_sum
print_sum(1)(5)(8)

'''control'''
x = 0
abs(1/x if x!=0 else 0)
