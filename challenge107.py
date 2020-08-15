"""Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should 
print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5"""
  
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def _print(self):
        print(self.val)
        if self.left:
            self.left._print()
        if self.right:
            self.right._print()
            
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
    
    a._print()