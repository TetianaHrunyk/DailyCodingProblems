"""Given an array of integers, find the first missing positive integer in linear time 
and constant space. In other words, find the lowest positive integer that 
does not exist in the array. The array can contain duplicates and negative 
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""

def lowest_missing_int(l: list):
    lowest = max(l)                                 #O(n)
    for num in l:                                   #O(n)
        if num >= 1 and num <=lowest:               #O(1)
            if (num-1) not in l and (num-1) != 0:   #O(1)
                lowest = num-1                      #O(1)
            elif (num+1) not in l:                  #O(1)
                lowest = num+1                      #O(1)
            else:           
                pass
    return lowest                                   #2*O(n) * (O(1)* 7*O(1)) = O(n)

if __name__ == "__main__":
    assert lowest_missing_int([3, 4, -1, 1]) == 2
    assert lowest_missing_int([1, 2, 0]) == 3
    