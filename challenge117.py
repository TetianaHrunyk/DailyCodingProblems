"""Given a binary tree, return the level of the tree with minimum sum."""

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

def min_sum_level(root, s = 0, level = 0):
    if root:
        s += root.val
        level += 1
        if root.left == None and root.right == None:
            return [s, level]
        return min(min_sum_level(root.left, s, level), min_sum_level(root.right, s, level))
              
    
    
    
if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    
    a.left = b
    a.right = c
    c.left = d
    c.right = e
    
    assert min_sum_level(a)[1] == 2
    assert min_sum_level(b)[1] == 1