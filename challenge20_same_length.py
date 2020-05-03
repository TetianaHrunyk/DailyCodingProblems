"""
Given two singly linked lists that intersect at some point, 
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
 return the node with value 8.

In this example, assume nodes with the same value 
are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists)
 and constant space.
"""

from linked_list import *

def intersect(A, B):
    ahead = A.head
    a = A.head
    b = B.head
    intersect = None
    while ahead:
        while a and b:
            if a.data == b.data:
                intersect = a.data
                return intersect 
            a = a.next
            b = b.next
        ahead = ahead.next
        a = A.head
        b = B.head
        
if __name__ == '__main__':
#_______Testcase1_______________
    print('Test 1')
    A = LinkedList()
    A.append(3)
    A.append(7)
    A.append(8)
    A.append(10)
    A.printList()
    
    B = LinkedList()
    B.append(99)
    B.append(1)
    B.append(8)
    B.append(10)
    B.printList()
    
    print(intersect(A, B))
    print()
    
#_______Testcase2_______________
    print('Test 2')
    A = LinkedList()
    A.append(10)
    A.printList()
    
    B = LinkedList()
    B.append(99)
    B.append(1)
    B.append(10)
    B.append(23)
    B.printList()
    
    print(intersect(A, B))
    print()
    
#_______Testcase3_______________
    print('Test 3')
    A = LinkedList()
    A.append(3)
    A.append(7)
    A.append(8)
    A.append(10)
    A.printList()
    
    B = LinkedList()
    B.append(99)
    B.append(1)
    B.append(4)
    B.append(23)
    B.printList()
    
    print(intersect(A, B))
    print()
    