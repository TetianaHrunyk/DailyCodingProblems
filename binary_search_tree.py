class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 
        self.locked = False
        
class Tree:
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        else:
            node = self.root
        while node.data != data:
            if node.data > data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    node = node.left                    
            else:
                if node.right is None:
                    node.right = Node(data)
                else:
                    node = node.right

    def printTree(self):
        def traverse(root):        
            if root:
                traverse(root.left)
                print(root.data, end = '->')
                traverse(root.right)
        traverse(self.root)  
        print()