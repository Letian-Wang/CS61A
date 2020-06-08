''' Modular Design '''
# Seperation of Concerns
# Developed and tested independently

others.remove(self)
return sorted(others, key=lambda x:-similarity(self, r))

''' Set intersection '''
def fast_overlap(s, t):
    count, i, j = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count + 1, i+1, j+1 
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count

''' Sets '''
unrepeated
arbitrary order
s.union(set)
s.intersection(set)
