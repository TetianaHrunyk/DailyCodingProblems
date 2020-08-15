"""Let's represent an integer in a linked list format by having each node 
represent a digit in the number. The nodes make up the number in reversed order.
For example, the following linked list:
1 -> 2 -> 3 -> 4 -> 5   is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.
For example, given
9 -> 9
5 -> 2
return 124 (99 + 25) as:
4 -> 2 -> 1
"""

from linked_list import Node, LinkedList

def add_lists(a: LinkedList, b: LinkedList):
    ahead = a.head
    bhead = b.head
    c = LinkedList()
    offset = 0
    while ahead and bhead:
        val = ahead.data + bhead.data + offset
        offset = val//10
        c.append(val%10)
        ahead, bhead = ahead.next, bhead.next
    if ahead:
        while ahead:
            val = ahead.data + offset
            offset = val//10
            c.append(val%10)
            ahead = ahead.next
    if bhead:
        while bhead:
            val = bhead.data + offset
            offset = val//10
            c.append(val%10)
            bhead = bhead.next
    if offset != 0:
        c.append(offset)
    return c

if __name__ == "__main__":
#__________________TEST1_____________________________
    a = LinkedList()
    a.append(9)
    a.append(9)
    
    b = LinkedList()
    b.append(5)
    b.append(2)
    
    c = add_lists(a, b)
    c.printList()
    
#__________________TEST2_____________________________
    a = LinkedList()
    a.append(9)
    a.append(9)
    a.append(9)
    
    b = LinkedList()
    b.append(5)
    b.append(2)
    
    c = add_lists(a, b)
    c.printList()
    
#__________________TEST2_____________________________
    a = LinkedList()
    a.append(9)
    a.append(9)
    
    b = LinkedList()
    b.append(5)
    b.append(2)
    b.append(2)
    
    c = add_lists(a, b)
    c.printList()