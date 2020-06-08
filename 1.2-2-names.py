from math import pi, sin, cos
from operator import add,mul

# assignment: bind names to values
a = 1
b = 2
b, a = a+b, b

''' assign function '''
max(1,2,3)
f = max
f(1,2,3)

max = 7 
f(1,2,3)

f = min
f = max
g, h = min, max
max = g
max( f(2, g(h(1, 5), 3)), 4)

##
//  # floor divide
%   # floor diveid,余数