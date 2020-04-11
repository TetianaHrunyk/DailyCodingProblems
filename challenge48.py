"""
Given pre-order and in-order traversals of a binary tree, 
write a function to reconstruct the tree.

For example, given the following preorder traversal:
[a, b, d, e, c, f, g]

And the following inorder traversal:
[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
"""
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 
        
class Tree:
    
    def __init__(self, data = None):
        self.root = None
    
    def buildTree(self, inorder, preorder):
        
        def build(inorder, preorder):
            if not preorder or not inorder:
                return None
        
            root_char = preorder[0]
            if len(preorder) == 1:
                return Node(root_char)
        
            root_node = Node(root_char)
            for i, char in enumerate(inorder):
                if char == root_char:
                    root_node.left = build(
                        preorder=preorder[1:i+1], inorder=inorder[:i])
                    root_node.right = build(
                        preorder=preorder[i+1:], inorder=inorder[i+1:])

            return root_node
        self.root = build(inorder, preorder)
        
    def preorder(self):
        
        def traverse(root):        
            if root:
                print(root.data, end = '->')
                traverse(root.left)
                traverse(root.right)
        traverse(self.root)  
        print()
        
    def inorder(self):
        
        def traverse(root):        
            if root:
                traverse(root.left)
                print(root.data, end = '->')
                traverse(root.right)
        traverse(self.root)  
        print()
        
if __name__ == "__main__":
    tree = Tree()
    tree.buildTree(["D", "B", "E", "A", "F", "C", "G"],["A", "B", "D", "E", "C", "F", "G"])
    tree.inorder()
    tree.preorder()