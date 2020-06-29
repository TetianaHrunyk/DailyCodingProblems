"""Given a node in a binary search tree, return the next bigger element, 
also known as the inorder successor.
For example, the inorder successor of 22 is 30.
   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer."""
import sys

class Node:
    
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.parent = None
        
def get_inorder_successor(root: Node, node: Node, left = [], right = []):
        if root.right or root.left:
            print(f"Root: {root.val}, Node: {node.val}")
            if root.left:
                print("went left")
                if root.val - node.val > 0 and node != root:
                    left.append( (root.val-node.val, root))
                else:
                    left.append( (sys.maxsize, root))
                
            if root.right:
                print("went right")
                if root.val - node.val > 0 and node != root:
                    right.append( (root.val-node.val, root))
                else:
                    right.append( (sys.maxsize, root)) 
            get_inorder_successor(root.left, node, right, left)
            get_inorder_successor(root.right, node, right, left)
        print("Check children: ", root.left, root.right)
        print("Left: ", left)
        print("Right: ", right)
        m =  min(*left, *right)
        print(m[0])
        if m[0] == sys.maxsize:
            return None
        else:
            return m[1]
            
        
    
if __name__ == "__main__":
    a = Node(10)
    b = Node(5)
    c = Node(30)
    b.parent, c.parent = a, a
    a.left = b
    a.right = c
    d = Node(22)
    e = Node(35)
    c.left = d
    c.right = e
    e.parent, d.parent = c, c

#    assert get_inorder_successor(a, d) == c
#    assert get_inorder_successor(a, b) == a
    print( get_inorder_successor(a, a).val)
    
        
    