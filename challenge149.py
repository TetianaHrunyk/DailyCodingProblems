"""Given a list of numbers L, implement a method sum(i, j) which returns the sum 
from the sublist L[i:j] (including i, excluding j).
For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]),
which is 5.
You can assume that you can do some pre-processing. sum() should be optimized 
over the pre-processing step."""

class SumArray:
    
    def __init__(self, arr):
        self.arr = [sum(arr[:i+1]) for i in range(len(arr))]
        
    def arr_sum(self, i, j):
        if i > 0: 
            return self.arr[j-1]-self.arr[i-1]
        else:
            return self.arr[j-1]
        
if __name__ == "__main__":
    arr = SumArray([i for i in range(1, 15, 2)])
    assert arr.arr_sum(1, 4) == 15
    assert arr.arr_sum(0, 4) == 16
    