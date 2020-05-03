"""Given the root of a binary tree, return a deepest node. For example, in the
 following tree, return d.

    a
   / \
  b   c
 /
d
"""
from binary_tree import Node, Tree

def returnDeepestNode(root, depth):

    if root.left == None and root.right == None:
        return (root.data, depth)
    left_depth = depth
    right_depth = depth
    if root.left:
        left_deepest, left_depth = returnDeepestNode(root.left, depth + 1)
    if root.right:
        right_deepest, right_depth = returnDeepestNode(root.right, depth + 1)

    return (left_deepest, left_depth) if left_depth > right_depth \
        else (right_deepest, right_depth)


def returnDeepestNodeHelper(root):
    return returnDeepestNode(root, 0)
    
if __name__ == "__main__":
    tree = Tree()
    tree.insert_left("a")
    tree.insert_left("b")
    tree.insert_left("d")
    tree.insert_right("c")
    print(returnDeepestNodeHelper(tree.root))
    
    