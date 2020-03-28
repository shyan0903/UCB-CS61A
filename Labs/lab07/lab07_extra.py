""" Optional Questions for Lab 07 """

from lab07 import *

def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    seen = []  # a list of Linked lists
    while link is not Link.empty:
        if link in seen:
            return True
        else:
            seen.append(link)
            link = link.rest
    return False


def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    # Floyd's Algorithm: space complexity is constant because only two nodes are needed
    slow, fast = link, link.rest
    while fast is not Link.empty:  # if the faster pointer comes to the end
        # without meeting the slower one, no cycle exist
        if slow == fast:  # if two pointers meet, then a cycle is found
            return True
        slow = slow.rest  # move by 1
        fast = fast.rest.rest  # move by 2
    return False


def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    def reverse_helper(t, to_reverse):
        reversed = [b.label for b in t.branches][::-1]  # reversed labels of odd level branches
        for i in range(len(t.branches)):  # for each subtree
            reverse_helper(t.branches[i], not to_reverse)  # reverse it if it's on the odd level
            if to_reverse:
                t.branches[i].label = reversed[i]  # reverse labels if needed
    return reverse_helper(t, True)
