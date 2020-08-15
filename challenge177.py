"""Given a linked list and a positive integer k, rotate the list to the right by k places.
For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, 
it should become 3 -> 5 -> 7 -> 7.
Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 2, 
it should become 3 -> 4 -> 5 -> 1 -> 2."""

from linked_list import LinkedList

def rotate_list(l, k):
    tail = l.head
    while tail.next:
        tail = tail.next
    for _ in range(k):
        end = l.head
        l.head = l.head.next
        end.next = None
        tail.next = end              
        tail = tail.next




if __name__ == "__main__":
    l = LinkedList()
    l.append(7)
    l.append(7)
    l.append(3)
    l.append(5)
    l.printList()
    rotate_list(l, 2)
    l.printList()
    
    print()
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.printList()
    rotate_list(l, 2)
    l.printList()