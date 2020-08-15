"""Implement a bit array.
A bit array is a space efficient array that holds a value of 1 or 0 at each index.
    init(size): initialize the array with size
    set(i, val): updates index at i with val where val is either 1 or 0.
    get(i): gets the value at index i.
"""

class BitArray:
    
    def __init__(self, size):
        self.size = size
        self.indices = set()
        
    def set_val(self, i, val):
        if i < 0 or i >= self.size:
            raise IndexError
        if val:
            self.indices.add(i)
        else:
            if i in self.indices:
                self.indices.remove(i)
    
    def get_val(self, i):
        if i < 0 or i >= self.size:
            raise IndexError
        if i in self.indices:
            return 1
        return 0
    
if __name__ == "__main__":
    arr = BitArray(40)
    arr.set_val(3, 1)
    assert arr.get_val(3) == 1
    assert arr.get_val(4) == 0
    arr.set_val(3, 0)
    assert arr.get_val(3) == 0
            