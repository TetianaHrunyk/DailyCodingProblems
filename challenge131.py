"""Given the head to a singly linked list, where each node also has a “random” 
pointer that points to anywhere in the linked list, deep clone the list."""
import random

class Node:   
    def __init__(self, val):
        self.val = val
        self.next = None
        self.rand = None
        
    def copy(self):
        return Node(self.val)
        
class SList_with_random_pointer:
    def __init__(self):
        self.head = None
        self.nodes = []
        self.tail = None
        
    def append(self, val):
        new_node = Node(val)
        self.nodes.append(new_node)
        if self.head == None: 
            self.head, self.tail = new_node, new_node
        else:
            self.tail.next = new_node
            new_node.rand = random.choice(self.nodes)
            self.tail = new_node
            
    def print_list(self):
        pointer = self.head
        while pointer:
            print(pointer.val, end = "->")
            pointer = pointer.next
        print("None")
            
    def shuffle(self):
        """"This method makes the pointers less predictable
        and deals with the fact that the initial node has
        random pointer to None, and the second node points to itself"""
        pointer = self.head
        while pointer:
            pointer.rand = random.choice(self.nodes)
            pointer = pointer.next
        
            
def deep_copy_list(a):
    head = a.head
    randoms = []
    copy = SList_with_random_pointer()
    while head:
        copy.append(head.val)
        randoms.append(head.rand)
        head = head.next
    copy_head = copy.head
    for node in randoms:
        copy_head.rand = copy.nodes[a.nodes.index(node)]
        copy_head = copy_head.next
    return copy


if __name__ == "__main__":
    a = SList_with_random_pointer()
    a.append("a")
    a.append("b")
    a.append("c")
    a.append("d")
    a.shuffle()
    a.print_list()
    
    
    c = deep_copy_list(a)
    c.print_list()
    
    assert a.head.rand.val == c.head.rand.val
    assert a.head.next.rand.val == c.head.next.rand.val
    assert a.head.rand.rand.val == c.head.rand.rand.val
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    