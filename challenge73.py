"""Given the head of a singly linked list, reverse it in-place."""
from linked_list import LinkedList, Node

class DoubleNode:
    def __init__(self, val = None):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList_rev:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def push(self, val):
        new_node = DoubleNode(val)
        if self.tail == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
    def print_list(self):
        head = self.head
        while head:
            print(head.val, end = "->")
            head = head.next
        print("None")
        
    def get_reversed(self, slist):
        head = slist.head
        while head:
            self.push(head.data)
            head = head.next


            
if __name__ == "__main__":
    dlist = DoublyLinkedList()
    slist = LinkedList()
    for i in range(10):
        slist.append(i)    
    slist.printList()
    
    dlist.get_reversed(slist)
    dlist.print_list()
    
