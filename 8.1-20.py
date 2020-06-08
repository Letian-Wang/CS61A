''' Linked list '''
Link(3, Link(4, Link(5, Link.empty)))
class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

s = Link(3, Link(4, Link(5)))
s.first
s.rest.first
s.rest.rest.first
s.rest.rest.rest is Link.empty

s.rest.first = 7

Link(3, Link(7, Link(5)))
Link(8, s.rest)

''' Property methods '''
@property decorator

class Link:
    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

''' Tree Class '''
Recursion description
Relative description
class Tree:
    def
