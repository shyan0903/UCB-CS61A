""" Lab 04 Optional Questions """

from lab04 import *


this_file = __file__

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> check(this_file, 'hailstone',
    ...       ['While', 'For'])
    True
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    return 1 + hailstone(n)
