"""
Given a singly linked list and an integer k,
 remove the kth last element from the list. 
 k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass."""
from linked_list import LinkedList

class eLinkedList (LinkedList):
    
    def removeK(self, k):
        pointer = self.head
        pre_kpointer = self.head
        while pointer != None:
            #print("Pointer: ", pointer.data)
            pointer = pointer.next            
            if k == -1:
                #print("pre_k: ", pre_kpointer.data)
                pre_kpointer = pre_kpointer.next
            else:
                #print("k: ", k)
                k -= 1
        print("Node with the value {} will be deleted".format(pre_kpointer.next.data))
        skip_k = pre_kpointer.next.next
        pre_kpointer.next = skip_k
        
if __name__ == "__main__":
    llist = eLinkedList()
    llist.append(1)
    llist.append(3)
    llist.append(6)
    llist.append(2)
    llist.append(8)
    llist.append(9)
    llist.printList()
    
    llist.removeK(3)
    
    llist.printList()
    