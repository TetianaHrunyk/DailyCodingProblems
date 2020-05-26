"""Given an unsorted array of integers, find the length of the longest consecutive 
elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element
 sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
def consecutive_len(s: list):
    cur_longest = [min(s)]
    longest = []
    s.remove(min(s))
    while len(s) > 0:
        char = min(s)
        
        if char not in cur_longest:
            if (cur_longest[-1]-char) == -1:
                cur_longest.append(char)
                if len(cur_longest) > len(longest):
                    longest = cur_longest
            else:
                cur_longest = []
        
        if len(cur_longest) == 0:
            cur_longest.append(char)
        s.remove(char)  
    return len(longest)

if __name__ == "__main__":
    assert consecutive_len([100, 4, 200, 1, 3, 2]) == 4
    assert consecutive_len([204, 100, 4, 200, 201, 1, 3, 2, 203, 205, 202]) == 6
    assert consecutive_len([1, 2, 2, 2, 2]) == 2