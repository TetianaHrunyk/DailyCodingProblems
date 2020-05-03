"""This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. 
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5)."""

from challenge48 import Node, Tree

def solve_graph(root):
    if root.data.isnumeric():
        return float(root.data)

    return eval("{} {} {}".format(solve_graph(root.left), root.data, solve_graph(root.right)))

if __name__ == "__main__":
    tree = Tree()
    tree.buildTree(["3","+", "2", "*", "4", "+", "5"], ["*", "+", "3", "2", "+", "4", "5"])
    assert solve_graph(tree.root)