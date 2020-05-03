"""Implement locking in a binary tree. 
A binary tree node can be locked or unlocked only if all of its 
ancestors are not locked.

Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, 
    then it should return false. Otherwise, it should lock it and return true.
    unlock, which unlocks the node. If it cannot be unlocked,
    then it should return false. Otherwise, it should unlock it
    and return true.

You may augment the node to add parent pointers or any other property
 you would like. You may assume the class is used in 
 a single-threaded program, so there is no need for
 actual locks or mutexes. Each method should run in O(h), 
 where h is the height of the tree.
"""

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
        
    def find_value(self, value):
        
        def find_inner(value, root = self.root):
            if root:
                if root.data < value:
                    return find_inner(value, root.right)
                if root.data > value:
                    return find_inner(value, root.left)
                else:
                    return root
        
        return find_inner(value)
                
        
    
    def is_locked(self, value):
        
        def is_locked_inner(value, root = self.root):
            if root:
                if root.data < value:
                    return is_locked_inner(value, root.right)
                if root.data > value:
                    return is_locked_inner(value, root.left)
                else:
                    if root.locked == True:
                        print("is_locked() says: Node {} is locked".format(value))
                        return True
                    else:
                        print("is_locked() says: Node {} is not locked".format(value))
                        return False
                
        return is_locked_inner(value)
    
    def lock(self, value):
        
        def lock_inner(value, root = self.root):
            if root:
                if root.locked == False:
                    if root.data < value:
                        return lock_inner(value, root.right)
                    if root.data > value:
                        return lock_inner(value, root.left)
                else:
                    return False
                return True

        if lock_inner(value):
            node = self.find_value(value)
            node.locked = True
            print("lock() says: Let's lock {}".format(value))
            return True
        else:
            print("lock() says: Locking {} certainly won't work".format(value))
            return False
            
    def unlock(self, value):
            
        def unlock_inner(value, root = self.root):
            if root:
                if root.locked == False:
                    if root.data < value:
                        return unlock_inner(value, root.right)
                    if root.data > value:
                        return unlock_inner(value, root.left)
                else:
                    if root.data == value:
                        return True
                    else:
                        return False
                print("unlock() says: This shuld not have happened")
                return False

        if unlock_inner(value):
            node = self.find_value(value)
            node.locked = False
            print("unlock() says: Let's unlock {}".format(value))
            return True
        else:
            print("unlock() says: Node {} cannot be unlocked".format(value))
            return False
        
if __name__ == "__main__":
    tree = Tree()
    tree.insert(6)
    tree.insert(2)
    tree.insert(4)
    tree.insert(7)
    tree.insert(9)
    tree.printTree()
    
    assert tree.lock(2) == True
    assert tree.is_locked(2) == True
    assert tree.lock(4) == False
    assert tree.is_locked(4) == False
    assert tree.unlock(2) == True
    assert tree.is_locked(2) == False
            
        
        
    