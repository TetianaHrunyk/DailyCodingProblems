
# Node class 
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 
   
# Linked List class 
class LinkedList: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None

    # This function prints contents of linked list 
    # starting from head 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data, end = '->') 
            temp = temp.next
        print('None')
        
    def push(self, new_data): 
  
        # 1 & 2: Allocate the Node & 
        #        Put in the data 
        new_node = Node(new_data) 
              
        # 3. Make next of new Node as head 
        new_node.next = self.head 
              
        # 4. Move the head to point to new Node  
        self.head = new_node 
    
    
    # This function is defined in Linked List class 
    # Appends a new node at the end.  This method is 
    #  defined inside LinkedList class shown above */ 
    def append(self, new_data): 
     
       # 1. Create a new node 
       # 2. Put in the data 
       # 3. Set next as None 
       new_node = Node(new_data) 
     
       # 4. If the Linked List is empty, then make the 
       #    new node as head 
       if self.head is None: 
            self.head = new_node 
            return
     
       # 5. Else traverse till the last node 
       last = self.head 
       while (last.next): 
           last = last.next
     
       # 6. Change the next of last node 
       last.next =  new_node 
       
    def pop_head(self):
        if self.head:
            res = self.head.data
            self.head = self.head.next
            return res
        else:
            return None
