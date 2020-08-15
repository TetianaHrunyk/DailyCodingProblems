"""Given an array of numbers and an index i, return the index of the nearest 
larger number of the number at index i, where distance is measured in array indices.
For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.
If two distances to larger numbers are the equal, then return any one of them. 
If the array at i doesn't have a nearest larger integer, then return null."""

def larger_neighbor(arr: list, i: int):
    if arr[i] == max(arr):
        return None
    l = len(arr)
    step = 1
    while True:
        if i-step >= 0:
            if arr[i-step] > arr[i]:
                return i-step
        if i+step < l:
            if arr[i+step] > arr[i]:
                return i+step
        if i-step < 0 and i+step >= l:
            return None
        step += 1
        
if __name__ == "__main__":
    assert larger_neighbor([4, 1, 3, 5, 6], 0) == 3
    assert larger_neighbor([4, 1, 3, 5, 6], 4) == None
    assert larger_neighbor([4, 1, 3, 5, 6], 2) == 3
        