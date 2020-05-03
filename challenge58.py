"""
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than 
linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, 
return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""

def findIndex(arr, elem, start, end):
   # print(arr[start:end])
    if start == end:
        return None
    mid = start + ((end - start) // 2)
    if arr[mid] == elem:
        return mid
    elif arr[mid] > elem:
        if arr[start] >= elem:
            return findIndex(arr, elem, start, mid)
        else:
            return findIndex(arr, elem, mid, end)
    elif arr[mid] < elem:
        if arr[start] <= elem:
            return findIndex(arr, elem, start, mid)
        else:
            return findIndex(arr, elem, mid, end)
            
        
def findIndexmain(arr, elem):
    end = len(arr)
    start = 0
    return findIndex(arr, elem, start, end)
    
    
    
        
if __name__ == "__main__":
    assert findIndexmain([13, 18, 25, 2, 8, 10], 2) == 3
    print()
    assert findIndexmain([13, 18, 25, 2, 8, 10], 8) == 4
    print()
    assert findIndexmain([25, 2, 8, 10, 13, 18], 8) == 2
    print()
    assert findIndexmain([8, 10, 13, 18, 25, 2], 8) == 0
            
    