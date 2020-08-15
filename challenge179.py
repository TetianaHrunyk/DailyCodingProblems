"""Given the sequence of keys visited by a postorder traversal of a binary search tree,
 reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the 
following tree:

    5
   / \
  3   7
 / \   \
2   4   8                   """

class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def construct_tree(self, s: list):
        self.root = Node(s.pop())
        while s:
            self.add_node(s.pop())
        
    def add_node(self, val):
        root = self.root
        while True:
            if  val < root.val:
                if root.left == None:
                    root.left = Node(val)
                    break
                else:
                    root = root.left
            else:
                if root.right == None:
                    root.right = Node(val)
                else:
                    root = root.right
                    break
                
    def print_tree_post(self):
        def print_rec(root):
            if root:
                print_rec(root.left)
                print_rec(root.right)
                print(root.val, end = ', ')
        print_rec(self.root)
        
        
                
if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.construct_tree([2, 4, 3, 8, 7, 5])
    tree.print_tree_post()
                