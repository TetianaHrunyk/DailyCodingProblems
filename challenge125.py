"""Given the root of a binary search tree, and a target K, 
return two nodes in the tree whose sum equals K.
For example, given the following tree and K of 20
    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15."""

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
def nodes_sum_equals(root, origin, k):
    if root and origin:
        if root.val+origin.val == k and root is not origin:
            return root.val, origin.val
        return nodes_sum_equals(root.left, origin, k) or nodes_sum_equals(root.right, origin, k) or nodes_sum_equals(root, origin.right, k) or nodes_sum_equals(root, origin.left, k)
    
if __name__ == "__main__":
    a = Node(10)
    b = Node(5)
    c = Node(14)
    a.left = b
    a.right = c
    
    d = Node(11)
    e = Node(15)
    c.left = d
    c.right = e
    
    assert nodes_sum_equals(a, a, 20) == (5, 15)
    assert nodes_sum_equals(a, a, 16) == (5, 11)