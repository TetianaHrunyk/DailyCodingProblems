"""Given k sorted singly linked lists, write a function to merge all the lists
 into one sorted singly linked list.
"""

from linked_list import Node, LinkedList

def mergeLists(*lists):
    merged_list = LinkedList()
    queue = []
    for l in lists:
        head_val = l.pop_head()
        if head_val is not None:
            queue.append(head_val)
    while len(queue):
        merged_list.push(max(queue))
        queue.remove(max(queue))
        for l in lists:
            head_val = l.pop_head()
            if head_val is not None:
                queue.append(head_val)            
    return merged_list

if __name__ == "__main__":
    l1 = LinkedList()
    for i in range(0, 20, 3):
        l1.push(i)
        
    l2 = LinkedList()
    for i in range(0, 30, 5):
        l2.push(i)
        
    l3 = LinkedList()
    for i in range(2, 20, 4):
        l3.push(i)
        
    l4 = LinkedList()
    for i in range(-10, 10, 5):
        l4.push(i)
        
    l1.printList()
    l2.printList()
    l3.printList()
    l4.printList()
    print("Result: ")
    l_merged = mergeLists(l1, l2, l3, l4)
    l_merged.printList()
    