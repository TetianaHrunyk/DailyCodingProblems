"""You have a large array with most of the elements as zero.
Use a more space-efficient data structure, SparseArray, that implements 
the same interface:
    init(arr, size): initialize with the original large array and size.
    set(i, val): updates index at i with val.
    get(i): gets the value at index i. """
    
class SparceArray:
    
    def __init__(self, arr, size):
        self.arr = {i: arr[i] for i in range(len(arr)) if arr[i]!= 0}
        self.size = size
        
    def set_val(self, i, val):
        if i > self.size:
            raise IndexError
        self.arr[i] = val
            
    def get(self, i):
        if i > self.size:
            raise IndexError
        if i in self.arr.keys():
            return self.arr[i]
        return 0
            
            
if __name__ == "__main__":
    sp_arr = SparceArray([0, 0, 0, 0, 8, 0, 0, 8, 0, 0, 1, 0, 0], 50)
    sp_arr.set_val(2, 7)
    assert sp_arr.get(2) == 7
    assert sp_arr.get(40) == 0
    assert sp_arr.get(1) == 0
    assert sp_arr.get(4) == 8  
    try:
        sp_arr.get(100)
    except:
        print("Index error raised")
    try:
        sp_arr.set_val(100, 8)
    except:
        print("Index error raised")
    sp_arr.set_val(45, 7)
    assert sp_arr.get(45) == 7