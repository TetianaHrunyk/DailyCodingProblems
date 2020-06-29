"""Given an array of integers in which two elements appear exactly once and all other 
elements appear exactly twice, find the two elements that appear only once.
For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8.
The order does not matter.

Follow-up: Can you do this in linear time and constant space?"""

def find_2_unique(l: list):
    """algorith with constant space, but O(N^2) time"""
    u = []
    for i in range(len(l)):
        if (l[i] not in l[:i]) and (l[i] not in l[i+1:]):
            u.append(l[i])
            if len(u) == 2:
                return u


if __name__ == "__main__":
    assert find_2_unique([2, 4, 6, 8, 10, 2, 6, 10]) == [4, 8]
    
    