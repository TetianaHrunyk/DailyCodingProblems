"""Given an array of integers, return a new array where each element in the new array
 is the number of smaller elements to the right of that element
 in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0]"""

def smaller_right(arr):
    new_arr = []
    for i in range(len(arr)-1):
        smaller = 0
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                smaller += 1
        new_arr.append(smaller)
    new_arr.append(0)
    return new_arr

if __name__ == "__main__":
    assert smaller_right([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]