nested_list = [[1, 2], [], [[3, False, None], [4, lambda: 5]]]

''' Slice '''
odds = [3, 5, 7, 9]
odds[1:3]
odds[:3]
odds[1:]
odds[:]

''' Processing Container Values '''
sum([2,3,5])
sum(['2', '3', '5'])                # Wrong
sum([2, 3, 4], 5)                   # Start with 5
sum([[2,3], [4]], [])               # Start with list
[] + [2, 3] + [4]

max(range(5))
max(0, 1, 2, 3, 4)
max(range(10), key=lambda x:7-(x-4)*(x-2))      # return the argument which makes the function maximum
def func1(x):
    return 7-(x-4)*(x-2)
max(range(10), key=func1)      # return the argument which makes the function maximum

all(range(5))                       # whether all is true

''' Tree '''

