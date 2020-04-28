"""

Given an array of integers, write a function to determine whether the array 
could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can 
modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify 
any one element to get a non-decreasing array.
"""

def canBeNonDecreasing(l: list):
    redundant = 0
    if (max(l) == l[0]):
        l = l[1:]
        redundant = 1
    prev = l[0] 
    for i in range(1, len(l)):
        if (l[i] < prev):
            redundant += 1
        else:
            prev = l[i]
        if redundant > 1:
            return False
    return True

if __name__ == "__main__":
    assert canBeNonDecreasing([10, 5, 7]) == True
    assert canBeNonDecreasing([10, 5, 1]) == False
    assert canBeNonDecreasing([10, 12, 14, 14, 14, 6]) == True
    assert canBeNonDecreasing([10, 12, 14, 14, 14, 6, 2]) == False
    