"""Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14."""

def greatest_comm_dev(nums):
    cand = min(nums)
    while cand != 1:
        for i in range(len(nums)):
            if nums[i]%cand != 0:
                break
            if i == (len(nums)-1):
                return cand
        cand-=1
    return 1


if __name__ == "__main__":
    assert greatest_comm_dev([42, 56, 14]) == 14
    assert greatest_comm_dev([3, 5]) == 1
    assert greatest_comm_dev([9, 15]) == 3
            