"""
Given the root to a binary search tree,
 find the second largest node in the tree.
 """
 
from challenge24 import Node, Tree

class ExtendedTree (Tree):
    
    def findSecondLargest(self):
        
        def inner(head = self.root, largest = self.root.data, second_largest = self.root.data):
            if head:
                if head.data > largest:
                    second_largest = largest
                    largest = head.data
                return inner(head.right, largest, second_largest)
            else:
                return second_largest
            
        return inner()
    
if __name__ == "__main__":
    tree = ExtendedTree()
    tree.insert(6)
    tree.insert(2)
    tree.insert(4)
    tree.insert(7)
    tree.insert(9)
#    tree.printTree()
    
    assert tree.findSecondLargest() == 7