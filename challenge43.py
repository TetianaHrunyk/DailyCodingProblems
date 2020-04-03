"""
Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack.
    If there are no elements in the stack, then it should throw an error or
    return null.
    max(), which returns the maximum value in the stack currently. 
    If there are no elements in the stack, then it should throw an error or
    return null.

Each method should run in constant time.
"""

class Stack:
    
    def __init__:
        self.data = []

    def push(self, val):
        self.data = [val] + self.data
        return True

        
    def pop(self):
        if self.data:
            p = self.data[0]
            self.data = self.data[1:]
            return p
        else:
            return None
        
    def max_val(self):
        if self.data:
            return max(self.data)
        else:
            return None