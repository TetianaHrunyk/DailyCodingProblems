"""Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in 
the tree. Assume that each node in the tree also has a pointer to its parent.
According to the definition of LCA on Wikipedia: 
    “The lowest common ancestor is defined between two nodes v and w as the lowest node 
    in T that has both v and w as descendants (where we allow a node to be a descendant 
    of itself).”
"""

class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        
def lowest_common_ancestor(a, b):
    if a.parent and b.parent:
        lowest_common_ancestor(a.parent, b)
        lowest_common_ancestor(b.parent, a)
    if a.parent == None:
        return a
    else:
        return a.parent

if __name__ == "__main__":
    a = Node("a", None)
    b = Node("b", a)
    c = Node("c", a)
    a.left = b
    a.right = c
    d = Node("d", c)
    e = Node("e", c)
    c.left = d
    c.right = e
    g = Node("g", e)
    f = Node("f", e)
    e.left = g
    e.right = f
    assert lowest_common_ancestor(f, e) == e
    assert lowest_common_ancestor(a, a) == a
    assert lowest_common_ancestor(d, g) == c
        
            
    