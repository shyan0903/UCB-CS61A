# 2.1
def paths(x, y):
    if x == y:
        return [[x]]
    elif y < 2 * x: # elif x > y: return []
        return [[x] + each for each in paths(x + 1, y)]
    else:
        a = [[x] + each for each in paths(x + 1, y)]  # a = paths(x + 1, y)
        b = [[x] + each for each in paths(x * 2, y)]  # b = paths(x * 2, y)
        return a + b  # [[x] + each for each in a + b]


# 3.1
def long_paths(tree, n):
    path = []
    if n <= 0 and tree.is_leaf():
        path += [Link(tree.label)]
    for b in tree.branches:
        for p in long_paths(b, n - 1):
            path += [Link(tree.label, p)]
    return path
    # def helper(tree, n, len):
    #     if tree.is_leaf():
    #         return [Link(tree.label)] if n <= len else []
    #     else:
    #         paths = []
    #         if n >= len:
    #             for b in tree.branches:
    #                 paths += helper(b, n, len + 1)
    #     if paths:
    #         paths = [Link(tree.label, p) for p in paths]
    #     return paths
    # return helper(tree, n, 0)

# 4.1
(define (merge s1 s2)
    (if (<= (car s1) (car s2))
        (cons-stream (car s1) (merge (cdr-stream s1) s2))
        (cons-stream (car s2) (merge s1 (cdr-stream s2)))
))

# 4.2
(define (cycle start)
    (cons-stream start (cycle (modulo (+ 2 start) 5))))


# 5.1
def accumulate(iterable, f):
    it = iter(iterable)
    base = next(it)
    yield base
    for i in list(it):
        base = f(base, i)
        yield base

# 5.2
def repeated(f):
    g = lambda x: x
    while True:
        yield g
        g = (lambda g: lambda x: f(g(x)))(g)

# 6.1

# b.
SELECT SUM(count*amount) FROM (SELECT COUNT(*) as count, weight
    FROM cats GROUP BY weight), food WHERE weight = cat_weight;

# 7.1
# a.
(define-macro (when condition exprs)
    (list 'if condition (cons 'begin exprs) ''okay))
# (if condition (cons begin exprs) 'okay)

# b.
(define-macro (when condition exprs)
    `(if ,condition ,(cons 'begin exprs) 'okay))


# 7.2
(define-macro (zero-cond clauses)
    (cons 'cond
        (map
         (lambda (clause)
            (cons `(not (= 0 ,(car clause))) (cdr clause))) clauses)))

# cond (map (lambda (lst) (cons (if (= 0 (car lst)) #f #t) (cdr lst))) clauses)
# Linked List Class
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

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

t = Tree(3, [Tree(4), Tree(4), Tree(5)])
left = Tree(1, [Tree(2), t])
mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
whole = Tree(0, [left, Tree(13), mid, right])
