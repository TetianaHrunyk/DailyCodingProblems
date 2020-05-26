"""A unival tree (which stands for "universal value") is a tree where all nodes
 under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1          """
 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 

def is_unival(root):    
    if root.right or root.left:
        if root.right:
            if root.data != root.right.data:
                return False
        if root.left:
            if root.data != root.left.data:
                return False
        is_unival(root.right)
        is_unival(root.left)
    return True

def count_univals(root, univals=0):
    if root:
        if is_unival(root):
            univals +=1
        return count_univals(root.left, univals) + count_univals(root.right, univals)
    return univals
        

if __name__ == "__main__":
    a = Node(0)
    b = Node(1)
    c = Node(0)
    d = Node(1)
    f = Node(1)
    g = Node(1)
    e = Node(0)
    a.left = b
    a.right = c
    c.left = d
    c.right = e
    d.left = f
    d.right = g
    print(count_univals(c))
    print(count_univals(a))
