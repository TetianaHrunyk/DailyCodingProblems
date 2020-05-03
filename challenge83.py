"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f

should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""
from binary_tree import Node, Tree

def invert_tree(root):
    if not root:
        return

    inverted_left = invert_tree(root.right)
    inverted_right = invert_tree(root.left)
    root.left = inverted_left
    root.right = inverted_right

    return root

if __name__ == "__main__":
    tree = Tree()
    tree.insert_left("a")
    tree.insert_left("b")
    tree.insert_left("d")
    tree.insert_right("d")
    tree.insert_right("e")
    tree.insert_left("f")
    inversed_tree = invert_tree(tree.root)
    
    print(inversed_tree.data)
    print(inversed_tree.right.data)

    