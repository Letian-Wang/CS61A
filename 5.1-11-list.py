''' list '''
digit = [1,5,8,6]
digit2 = digit * 2      # replicate
len(digit)
digit[0]
digit + digit * 2
pairs = [[10, 20], [30, 40]]
pairs[0][1]

''' Containers '''
1 in digit
'1' in digit
5 not in digit
[1,8] in digit

''' For statements
for <name> in <expression>: '''
def count(s, value):
    total, index = 0, 0
    # while index < len(s):
        # element = s[index]
    for element in s:                       #
        if element == value:
            total +=  1                     #
        index += 1
    return total

''' unpack sequence '''
pairs = [[1, 2], [2, 3], [2, 2], [4, 8]]
same_count = 0
for x, y in pairs:                          # 
    if x == y:  
        same_count += 1

''' Range '''
range(-2, 2)                                # [-2, 2)
list(range(-2, 2))
list(range(4))                              # start with 0

for i in range(3):
for _ in range(3):                          # simple repeatation

''' List Comperhensions '''
letters = list(set('abcdefg'))
[i+1 for i in range(5)]
[i+1 for i in range(5) if 25%i == 0]

''' Strings '''
'curry = lambda f: lambda x: lambda y: f(x,y)'
exec('curry = lambda f: lambda x: lambda y: f(x,y)')        # define a function

city = 'Berkeley'
len(city)
city[1]
'here' in "where's Waldo"









