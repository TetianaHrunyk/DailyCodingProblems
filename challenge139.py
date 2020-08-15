"""Given an iterator with methods next() and hasNext(), create a wrapper iterator, 
PeekableInterface, which also implements peek(). peek shows the next element that
 would be returned on next().
"""

class Peekable:
    def __init__(self, iterator):
        self.iterator = iterator
        self.next = None

    def peek(self):
        if self.next != None:
            return self.next
        if self.hasNext():
            return self.next
        else:
            return None

    def inext(self):
        if self.next != None:          
            res = self.next
        elif self.hasNext():
            res = self.next
        else:
            return None
        self.next = None
        return res 

    def hasNext(self):
        if self.next != None:
            return True
        try:
            self.next = next(self.iterator)
            return True
        except:
            return False
        
if __name__ == "__main__":
    i = Peekable(iter([i for i in range(3)]))
    assert i.hasNext()
    assert i.inext() == 0
    assert i.hasNext()
    assert i.hasNext()
    assert i.peek() == 1
    assert i.inext() == 1
    assert i.peek() == 2
    assert i.inext() == 2
    assert i.hasNext() == False
        