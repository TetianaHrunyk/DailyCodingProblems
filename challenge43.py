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
    def __init__(self):
        self.stack = []
        self.max_stack = []
        self.length = 0

    def push(self, val):
        self.stack.append(val)
        self.length += 1
        if not self.max_stack:
            self.max_stack.append(len(self.stack) - 1)
        else:
            try:
                if val > self.stack[self.max_stack[-1]]:
                    self.max_stack.append(len(self.stack) - 1)
            except:
                pass
        
    def pop(self):
        if not self.stack:
            return None
        if len(self.stack) - 1 == self.max_stack[-1]:
            self.max_stack.pop()
            self.length -= 1

        return self.stack.pop()

    def max(self):
        if not self.stack:
            return None
        return self.stack[self.max_stack[-1]]
    
if __name__ == "__main__":   
    s = Stack()
    s.push(1)
    s.push(3)
    s.push(2)
    s.push(5)
    assert s.max() == 5
    s.pop()
    assert s.max() == 3
    s.pop()
    assert s.max() == 3
    s.pop()
    assert s.max() == 1
    s.pop()
    assert not s.max()