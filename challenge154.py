"""Implement a stack API using only a heap. A stack implements the following methods:

    push(item), which adds an element to the stack
    pop(), which removes and returns the most recently added element 
    (or throws an error if there is nothing on the stack)

Recall that a heap has the following operations:

    push(item), which adds a new key to the heap
    pop(), which removes and returns the max value of the heap
"""

import sys
from heapq import heappush, heappop


class Stack:

    def __init__(self):
        self.counter = sys.maxsize
        self.stack = list()

    def push(self, item):
        heappush(self.stack, (self.counter, item))
        self.counter -= 1

    def pop(self):
        if not self.stack:
            raise ValueError

        _, item = heappop(self.stack)
        return item


if __name__ == "__main__":
    stk = Stack()
    stk.push(1)
    stk.push(7)
    stk.push(4)
    assert stk.pop() == 4
    stk.push(2)
    assert stk.pop() == 2
    assert stk.pop() == 7
    assert stk.pop() == 1
    try:
        stk.pop()
    except:
        assert sys.exc_info()[0] == ValueError
