"""Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3."""

class Node:
    
    def __init__(self, val, n = None):
        self.val = val
        self.next = n
        
    def __str__(self):
        string = "["
        node = self
        while node:
            string += "{} ->".format(node.val)
            node = node.next
        string += "None]"
        return string

def swap_nodes(s: Node):
    head = s
    while s is not None and s.next is not None:
        s.val, s.next.val = s.next.val, s.val
        s = s.next.next
    return head
        
        
        
    
if __name__ == "__main__":
    l = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    s = swap_nodes(l)
    print(s)
    