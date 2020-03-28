""" Extra Questions for Lab 13 """

def num_splits(s, d):
    """Return the number of ways in which s can be partitioned into two
    sublists that have sums within d of each other.

    >>> num_splits([1, 5, 4], 0)  # splits to [1, 4] and [5]
    1
    >>> num_splits([6, 1, 3], 1)  # no split possible
    0
    >>> num_splits([-2, 1, 3], 2) # [-2, 3], [1] and [-2, 1, 3], []
    2
    >>> num_splits([1, 4, 6, 8, 2, 9, 5], 3)
    12
    """
    # Solution found online:
    # def num_splits_helper(s, n):
    #     if len(s) == 0:
    #         return 1 if abs(n) <= d else 0
    #     return num_splits_helper(s[1:], n + s[0]) + num_splits_helper(s[1:], n - s[0])
    # return num_splits_helper(s, 0) // 2

    diff = []

    def split_helper(s1, s2, s):
        # this helper function partitions s into two sublists s1 and s2 recursively
        # when s becomes empty, it calculates the differences of two sublists
        # and stores them in the diff list
        nonlocal diff
        if not s:
            diff += [abs(sum(s1) - sum(s2))]
        else:
            # s[0] either goes into the s1 or into s2
            split_helper(s1 + [s[0]], s2, s[1:])
            split_helper(s1, s2 + [s[0]], s[1:])
    split_helper([s[0]], [], s[1:])
    # returns the number of differences that are within d
    return len([i for i in diff if i <= d])


def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print(link)
    <1 2 3>
    >>> insert(link, 9001, 0)
    >>> print(link)
    <9001 1 2 3>
    >>> insert(link, 100, 2)
    >>> print(link)
    <9001 1 100 2 3>
    >>> insert(link, 4, 5)
    IndexError
    """
    if link.rest is Link.empty and index > 0:
        raise IndexError
    elif index == 0:
        link.rest = Link(link.first, link.rest)
        link.first = value
    else:
        insert(link.rest, value, index - 1)


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'