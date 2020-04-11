class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 
        
class Tree:
    
    def __init__(self, data = None):
        self.root = data
    
    def insert_left(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        else:
            node = self.root
        while node.left != None:
            node = node.left
        node.left = Node(data)
        
    def insert_right(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        else:
            node = self.root
        while node.right != None:
            node = node.left
        node.right = Node(data)
        
if __name__ == "__main__":
    tree = Tree("*")
    
