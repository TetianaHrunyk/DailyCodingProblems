"""Given a binary tree where all nodes are either 0 or 1, prune the tree so 
that subtrees containing all 0s are removed. For example, given the following tree:
   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
should be pruned to:
   0
  / \
 1   0
    /
   1
We do not remove the tree at the root or its left child because
 it still has a 1 as a descendant."""
 
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def prune(root, parent):
    if root: 
        if root.right == None and root.left == None and root.val == 0:
            if root == parent.left:
                parent.left = None
            else:
                parent.right = None
        prune(root.left, root)
        prune(root.right, root)
        
if __name__ == "__main__":
    a = Node(0)
    b = Node(1)
    c = Node(0)
    a.left = b
    a.right = c
    d = Node(1)
    e = Node(0)
    c.left = d
    c.right = e
    f = Node(0)
    h = Node(0)
    d.left = f
    d.right = h
    prune(a, a)
    assert a.right.right == None
    assert a.right.left.right == None
    assert a.right.left.left == None
    assert a.left.val == 1
    
    
    
    
    
    
    