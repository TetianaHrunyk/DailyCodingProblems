"""Given a binary tree, find a minimum path sum from root to a leaf.
For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1                 """
     
class Node:
    def __init__(self,val):
        self.val = val
        self.right, self.left = None, None
        
def min_path_sum(root: Node, curr_sum=0):
    if root:
        curr_sum += root.val
        if root.right == None and root.left == None:
            return curr_sum
        if root.left == None:
            return min_path_sum(root.right, curr_sum)
        if root.right == None:
            return min_path_sum(root.left, curr_sum)
        return min(min_path_sum(root.right, curr_sum), min_path_sum(root.left, curr_sum))
            
    
if __name__ == "__main__":
    a = Node(10)
    b = Node(5)
    b1 = Node(45)
    b.left = b1
    a.left = b
    c = Node(2)
    b.right = c
    d = Node(5)
    a.right = d
    e = Node(1)
    d.right = e
    f = Node(-1)
    e.left = f
    
    assert min_path_sum(a) == 15
    assert min_path_sum(b) == 7
    