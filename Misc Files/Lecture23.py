
def morse(code):
    whole = Tree(None)
    for letter, signals in code.items(): # code is a dict
        # items() returns the key and value as pairs in a dict
        t = whole
        for s in signals:
            if s not in [b.label for b in t.branches]:
                new_tree = Tree(s)  # create a new tree with the s
                t.branches.append(new_tree)
                t = new_tree # update t
            else:
                t = [b for b in t.branches if b.label == s][0]
        t.branches.append(Tree(letter)) # add a node with the letter as a leaf
    return whole
        
        

def decode(signals, tree):
    """Decode signals into a letter.

    >>> t = morse(abcde)
    >>> [decode(s, t) for s in ['_..', '.', '-.-.', '.-', '-..', '.']]
    ['d', 'e', 'c', 'a', 'd', 'e']
    """
    for signal in signals:  # access single letters in a string
        tree = [b for b in tree.branches if b.label == signal][0]
    leaves = [b for b in tree.branches if b.is_leaf()]
    assert len(leaves) == 1
    return leaves[0].label

