"""Determine whether a tree is a valid binary search tree.
A binary search tree is a tree with two children, left and right, and satisfies
 the constraint that the key in the left child must be less than or equal to the 
 root and the key in the right child must be greater than or equal to the root.
"""
from binary_search_tree import Node, Tree

def is_valid(root):
    if root:
        if root.right:
            right = root.right.data
            if right < root.data:
#                print("Right less than root")
                raise Exception
        else:
            right = None
        if root.left:
            left = root.left.data
            if left > root.data:
#                print("Left greater than root")
                raise Exception
        else:
            left = None
        if left and right:
            if right < left:
#                print("Left greater than right")
                raise Exception
    else:
        return True
    is_valid(root.right)
    is_valid(root.left)
    
if __name__ == "__main__":
    tree = Tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(10)
    tree.insert(6)
    try:
        is_valid(tree.root)
    except:
        print("Tree is invalid")
     
        
    invalid_root = Node(2)
    right = Node(4)
    left = Node(5)
    invalid_root.right = right
    invalid_root.left = left
    try:
        is_valid(invalid_root)
    except:
        print("The invalid tree was classified as is invalid")