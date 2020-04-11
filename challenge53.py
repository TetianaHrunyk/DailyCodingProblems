"""
Implement a queue using two stacks. Recall that a queue is a FIFO 
(first-in, first-out) data structure with the following methods: 
    enqueue, which inserts an element into the queue, 
    and dequeue, which removes it.
"""

from challenge43 import Stack

class Queue:
    
    def __init__ (self):
        self.s1 = Stack()
        self.s2 = Stack()
        
    def enqueue(self, elem):
        self.s1.push(elem)
        return True
    
    def dequeue(self):
        if self.s1.length == 0:
            return None
        if self.s1.length == 1:
            return self.s1.pop()
        elem = self.s1.pop()
        while elem != None:
            self.s2.push(elem)
            elem = self.s1.pop()
        res = self.s2.pop()
        elem = self.s2.pop()
        while elem != None:
            self.s1.push(elem)
            elem = self.s2.pop()
        return res
    
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
            