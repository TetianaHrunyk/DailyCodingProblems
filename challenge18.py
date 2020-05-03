"""
Given an array of integers and a number k, where 1 <= k <= length 
of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, 
we should get: [10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. 
You can modify the input array in-place and you do not need to store 
the results. You can simply print them out as you compute them.
"""

def LocalMax(a: list, k: int) -> list:
    assert k > 0
    max_vals = []
    for i in range(len(a)):
        sub_arr = a[i:i+k]
        #print("Sub arr: ",sub_arr)
        if len(sub_arr) < k:
            break
        max_vals.append(max(sub_arr))        
        #print("Max: ", max_vals)
    return max_vals

if __name__ == '__main__':
    assert LocalMax([10, 5, 2, 7, 8, 7], 3) ==  [10, 7, 8, 8] 
    assert LocalMax([10, 5, 2, 7, 8, 7], 1) ==  [10, 5, 2, 7, 8, 7]
    assert LocalMax([10, 5, 2, 7, 8, 7], 4) ==  [10, 8, 8]
    assert LocalMax([10, 5, 2, 7, 8, 7], 6) ==  [10]  
    assert LocalMax([2, 2, 2, 2, 2, 2], 5) ==  [2, 2]       
        