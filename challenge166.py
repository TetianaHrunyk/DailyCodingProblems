"""Implement a 2D iterator class. It will be initialized with an array of arrays,
 and should implement the following methods:

    next(): returns the next element in the array of arrays. If there are no 
    more elements, raise an exception.
    has_next(): returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next()
 repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty."""

class TwoDiterator:
    
    def __init__(self, arr):
        self.arr = arr
        self.next = [0, 0]
        
    def get_next(self):
        if self.has_next():
            res = self.arr[self.next[0]][self.next[1]]
            if self.next[1] < len(self.arr[self.next[0]])-1:
                self.next[1] += 1
            elif self.next[0] < len(self.arr)-1:
                while len(self.arr[self.next[0]+1]) == 0:
                    self.next[0] += 1
                self.next[0] += 1
                self.next[1] = 0
            else:
                self.next = None
            return res

    def has_next(self):
        if self.next == None:
            raise Exception
        return True
    
if __name__ == "__main__":
    it = TwoDiterator([[1, 2], [3], [], [4, 5, 6]])
    assert it.get_next() == 1
    assert it.has_next() == True
    assert it.get_next() == 2
    assert it.has_next() == True
    assert it.get_next() == 3
    assert it.has_next() == True
    assert it.get_next() == 4
    assert it.has_next() == True
    assert it.get_next() == 5
    assert it.has_next() == True
    assert it.get_next() == 6
    try:
        it.has_next()
    except:
        print("No more elements")
        
        
        