class Node: 
    def __init__(self, data=None): 
        self.next = None
        self.prev = None  
        self.data = data 
        
class DoublyLinkedList: 

    def __init__(self): 
        self.head = None
        self.tail = None

    def push(self, new_data): 
        new_node = Node(new_data) 
        if self.head == None:
            self.head, self.tail = new_node, new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def append(self, new_data):
        new_node = Node(new_data) 
        if self.head == None:
            self.head, self.tail = new_node, new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def print_list(self):
        start = self.head
        while start:
            print(start.data, end = " -> ")
            start = start.next
        print("None")
        
if __name__ == "__main__":
    dlist = DoublyLinkedList()
    dlist.push(3)
    dlist.push(2)
    dlist.push(1)
    dlist.append(4)
    dlist.append(5)
    dlist.print_list()