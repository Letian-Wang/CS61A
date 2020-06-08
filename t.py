def reverse(lst):
    if len(lst) <= 1:
        return lst
    return reverse(lst[1:]) + [lst[0]]
lst = [1, [2, 3], 4]
rev = reverse(lst)
# print(rev)

def map_mut(f, L):
    for i, j in enumerate(L):
        L[i] = f(j)

def path(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return path(m-1, n) + path(m, n -1)

def merge(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return s1 + s2
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    elif s1[0] > s2[0]:
        return [s2[0]] + merge(s1, s2[1:])

def mario_number(level):
    if level[0] == 'P':
        return 0
    if len(level)-1 == 0:
        return 0
    if len(level)-1 == 1:
        return 1
    if len(level)-1 == 2:
        if 'P' in level :
            return 1
        else:
            return 2
    else:
        return mario_number(level[1:]) + mario_number(level[2:])

level = '----P---P--P--P-P'
level = '----'
level = '----P----'
print(mario_number(level))
