"""Given two non-empty binary trees s and t, check whether tree t has exactly the same 
structure and node values with a subtree of s. A subtree of s is a tree consists of a 
node in s and all of this node's descendants. The tree s could also be considered as 
a subtree of itself.
"""
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

def contains_exact_subtree(s, t):
    if s and t:
        if s.val == t.val:
            if s.left == None and s.right == None and t.left == None and t.right == None:
                return True
            return contains_exact_subtree(s.right, t.right) and contains_exact_subtree(s.left, t.left)
        else:
            return contains_exact_subtree(s.right, t) or contains_exact_subtree(s.left, t)
    return False

        
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
    
    assert contains_exact_subtree(a, e) == True
    assert contains_exact_subtree(a, b) == True 
    assert contains_exact_subtree(d, e) == False
    assert contains_exact_subtree(b, e) == False
        
        