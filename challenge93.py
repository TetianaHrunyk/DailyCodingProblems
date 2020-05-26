"""Given a tree, find the largest tree/subtree that is a BST.
Given a tree, return the depth of the largest tree/subtree that is a BST."""

class Node:
    def __init__(self, data, right = None, left = None):
        self.data = data
        self.right = right
        self.left = left

from challenge80 import returnDeepestNode
from challenge89 import is_valid

def largest_valid_subtrees(root, sub_right, sub_left):
    try:
        is_valid(root)
    except:
        largest_valid_subtrees(root.left, sub_right, root.left)
        largest_valid_subtrees(root.right, root.right, sub_left)
    return (sub_right, sub_left)

def determine_largest(root):
    roots = largest_valid_subtrees(root, root, root)
    right = returnDeepestNode(roots[0], 0)
    left = returnDeepestNode(roots[1], 0)
    return max(right[1], left[1])
        
if __name__ == "__main__":
    a = Node(3)
    b = Node(2)
    c = Node(6)
    d = Node(1)
    e = Node(3)
    f = Node(4)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    print(determine_largest(a))
        
    
