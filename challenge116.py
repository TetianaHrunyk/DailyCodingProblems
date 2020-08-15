"""Generate a finite, but an arbitrarily large binary tree quickly in O(1).
That is, generate() should return a tree whose size is unbounded but finite.
"""
import random

class Node:
    #by instantiating a new node only the root is created, which takes O(1) time
    #to get left or the right node we use get_left and ger_right methods respectively
    
    def __init__(self, size = None):
        self.val = random.randint(1, 100)
        self.left = None
        self.right = None
        self.size = random.randint(1, 100) if size == None else size
        
    def get_left(self):
        if self.size > 0:
            self.size -= 1
            self.left = Node(self.size)
            return self.left
        else:
            #the size of the tree has been exhausted
            return None
    
    def get_right(self):
        if self.size > 0:
            self.size -= 1
            self.right = Node(self.size)
            return self.right
        else:
            #the size of the tree has been exhausted
            return None
        
    def get_val(self):
        return self.val
        
def generate():
    return Node()

if __name__ == "__main__":
    tree = generate()
    print(tree.get_val())
    print(tree.get_left().get_val())
    print(tree.get_left().get_left().val)
    print(tree.get_left().get_right().val)
        
        

        
    