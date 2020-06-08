a = set('absdfasdfasdz')
print(a)
b = '6456'
print(b[::-1])
c = [4,5,8,9,5]
print(c)
print(list(set(c)))

def couple(lst1, lst2):
    assert len(lst1) == len(lst2)
    return [[lst1[i], lst2[i]] for i in range(len(lst1))]

berkeley = make_city('Berkeley', 122, 37)
get_name(berkeley)
get_lat(berkeley)
get_lon(berkeley)

def distance(city1, city2):
    lat1, lon1 = get_lat(city1), get_lon(city1)
    lat2, lon2 = get_lat(city2), get_lon(city2)
    return sqrt( pow((lat1 - lat2), 2) + pow((lon1 - lon2), 2) )

def closer_city(lat, lon, city1, city2):
    new_city = make_city('arb', lab, lon)
    if distance(new_city, city1) > distance(new_city, city2):
        return get_name(city2)
    else:
        return get_name(city1)

def nut_finder(t):
    if label(t) == 'nut':
        return True
    else:
        for b in branches(t):
            if nut_finer(t):
                return True
    return false

def nut_finder(t):
    if label(t) == 'nut':
        return True
    else:
        return True in [nut_finder(b) for b in branches(t)]

def sprout_trees(t, values):
    if is_leaf(t):
        return [t, [tree(i) for i in values]]
    return [label(t), [sprout_trees(i, values) for i in branches(t)]] 
    
def planet(size):
    assert size > 0
    return ['planet', size]
def size(s):
    assert is_planet(s), "size must be called on a planet"
    return s[1]
def is_planet(s):
    return type(s)==list and len(s) == 2 and s[0] == 'planet':

def arm(length, planet_or_mobiel):
    assert is_mobiel(planet_or_mobiel) or is_planet(planet_or_mobiel)
    return ['arm', length, planet_or_mobiel]
def length(s):
    assert is_arm(s), "length must be called on an arm"
    return s[1]
def is_arm(s):
    return type(s)==list and len(s)==3 and s[0]=='arm'
def end(s):
    assert is_ram(s)， "end must be called on an arm"
    return s[2]

def mobile(left, right):
    assert is_arm(left) and is_arm(right)
    return ['mobile', left, right]
def is_mobiel(s):
    return type(s) == list and len(s) == 3 and s[0] == 'mobile'
def left(s):
    assert is_mobiel(s)
    return s[1]
def right(s):
    assert is_mobiel(s)
    return s[2]

def total_weight(m):
    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m)
        return total_weight(end(left)) + total_weight(end(right))

def balanced(m):
    if is_planet(m):
        return True
    assert is_mobiel(m)
    return balanced(end(left(m))) and balanced(end(right(m))) and total_weight(end(left(m)))*length(left(m)) == total_weight(end(right(m)))*length(right(m))

def totals_tree(m):
    if is_planet(m):
        return tree(size(m))
    branches = [totals_tree(end(f(m))) for f in [left, right]]
    return tree(sum([label(b) for b in branches]), branches)

def replace_leaf(t, old, replacement):
    if is_leaf(t) and label(t) == old:
        label(t) = replacement
        return tree(replacement)
    assert is_tree(t),'must be called on a tree'
    bs = replace_leaf(b, old, replacement) for b in branches(t)    
    return tree(label(t), bs)

def make_withdraw(balance, password):
    Attempts = []
    def withdraw(amount, password_attempt):
        nonlocal balance 
        if len(Attempts) == 3:
            return 'Your account is locked. Attempts: ' + str(Attempts)
        if password_attempt != password:
            Attempts.append(password_attempt)
            return 'incorrect password'
        if amount > balance:
            return 'insufficient fund'
        else:
            balance -= amount
            return balance
    return withdraw
def make_joint(withdraw, old_pass, new_pass):
    