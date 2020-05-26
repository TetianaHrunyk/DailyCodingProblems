"""Given two singly linked lists that intersect at some point, 
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
 return the node with value 8.

In this example, assume nodes with the same value are the 
!!!!!!!!!!EXACT SAME NODE OBJECTS!!!!!!!!!!!!.

Do this in O(M + N) time (where M and N are the lengths of the lists)
 and constant space.
"""

class Node:
    def __init__(self, val, n = None):
        self.val = val
        self.next = n

def intersect(a_head, b_head):
    #Since the nodes with the same value are exact same objs 
    #and the lists are non-cyclical,
    #there cannot be two objs that have the same value but
    #point to different nodes.
    #This means that each value in the list is unique.
    #It follows that if there are two nodes with the same value
    #in A and B, that must be the intersection node.

    a_nodes = []
    while a_head:
        a_nodes.append(a_head)
        a_head = a_head.next
    while b_head:
        if b_head in a_nodes:
            return b_head
        b_head = b_head.next
    return None
    

if __name__ == '__main__':
    inter = Node(8, Node(10))
    A = Node(3, Node(7, inter))
    B = Node(99, Node(1, inter))
    assert intersect(A, B) == inter
