"""Given a stack of N elements, interleave the first half of the stack with the
second half reversed using only one other queue. This should be done in-place.
Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.
For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3].
 If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].
Hint: Try working backwards from the end state."""
import math

class Stack:
    def __init__(self, elem=[]):
        self.elem = elem
        
    def pop(self):
        return self.elem.pop()
    
    def push(self, elem):
        self.elem.append(elem)
        
class Queue:
    def __init__(self, elem = []):
        self.elem = elem
        
    def enqueue(self, elem):
        self.elem.insert(0, elem)
        
    def dequeue(self):
        return self.elem.pop(0)


def interleave(s):
    half = math.floor(len(s)//2)
    