"""Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""
from doubly_linked_list import Node, DoublyLinkedList
from linked_list import LinkedList
from challenge46 import longestPalindrome

def doubly_palindrom(dlist):
    head = dlist.head
    tail = dlist.tail
    while head != tail:
        if head.data != tail.data:
            return False
        head = head.next
        tail = tail.prev
    return True

def singly_palindrom(slist):
    head = slist.head
    vals = ""
    while head:
        vals += str(head.data)
        head = head.next
    if len(longestPalindrome(vals)) == len(vals):
        return True
    return False
        
    

if __name__ == "__main__":
#__________FOR DOUBLY LINKED LIST_______________
    dlist = DoublyLinkedList()
    dlist.append(1)
    dlist.append(2)
    dlist.append(3)
    dlist.append(2)
    dlist.append(1)
    assert doubly_palindrom(dlist) == True
    
    dlist = DoublyLinkedList()
    dlist.append(1)
    dlist.append(4)
    assert doubly_palindrom(dlist) == False
    
#__________FOR SINGLY LINKED LIST_______________
    slist = LinkedList()
    slist.append(1)
    slist.append(2)
    slist.append(3)
    slist.append(2)
    slist.append(1)
    assert singly_palindrom(slist) == True
    
    slist = LinkedList()
    slist.append(1)
    slist.append(4)
    assert singly_palindrom(slist) == False
    
    
    
    
    