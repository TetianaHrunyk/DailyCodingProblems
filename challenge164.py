"""You are given an array of length n + 1 whose elements belong to the set 
1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate. 
Find it in linear time and space.
"""


def find_duplicate(arr, n):
    expected_sum = int((n * (n+1)) / 2)
    actual_sum = sum(arr)

    return actual_sum - expected_sum


if __name__ == "__main__":

    assert find_duplicate([1, 1, 2], 2) == 1
    assert find_duplicate([1, 2, 3, 3], 3) == 3
    assert find_duplicate([1, 2, 3, 4, 3], 4) == 3