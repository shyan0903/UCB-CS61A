""" Homework 2: Higher Order Functions"""

HW_SOURCE_FILE = 'hw02.py'

from operator import add, mul, sub

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

######################
# Required Questions #
######################

def make_adder(n):
    """Return a function that takes an argument K and returns N + K.

    >>> add_three = make_adder(3)
    >>> add_three(1) + add_three(2)
    9
    >>> make_adder(1)(2)
    3
    """
    return lambda k: n + k

def product(n, term):
    """Return the product of the first n terms in a sequence.
    n    -- a positive integer
    term -- a function that takes one argument

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'product', ['Recursion'])
    True
    """
    result = 1
    k = 1
    while k <= n:
        result *= term(k)
        k += 1
    return result

def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)  # 4 * 3 * 2 * 1
    24
    >>> factorial(6)  # 6 * 5 * 4 * 3 * 2 * 1
    720
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'factorial', ['Recursion', 'For', 'While'])
    True
    """
    return product(n, identity)

def accumulate( combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative, associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19      #(((2 + 1^2 + 1) + 2^2 + 1) + 3^2 + 1)
    """
    result, k = base, 1
    while (k <= n):
        result, k = combiner(result, term(k)), k + 1
    return result


def summation_using_accumulate(n, term):
    """Returns the sum of term(1) + ... + term(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    return accumulate(mul, 1, n, term)



###################
# Extra Questions #
###################

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def make_repeater(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times! 
    5
    """
    g = identity
    while n > 0:
        g = compose1(f, g)
        n -= 1
    return g

def make_repeater_simple(f, n):
    """Return the function that computes the nth application of f.

        >>> add_three = make_repeater(increment, 3)
        >>> add_three(5)
        8
        >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
        243
        >>> make_repeater(square, 2)(5) # square(square(5))
        625
        >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
        152587890625
        >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
        5
        """
    return accumulate(compose1, identity, n, f)


print(make_repeater(triple, 5)(1))
