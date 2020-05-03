"""
Given an array of numbers, find the length of the longest increasing subsequence 
in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array
 [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
 the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15
"""

def RightSubSequence(s: list) -> int:
    lonest_sub = []
    for i in range(len(s)):
        if i > 0:
            if s[i] > s[i-1]:
                continue
        if s[i] in lonest_sub:
            continue
        cur_sub = []
        for j in range(i+1, len(s)):
            if len(cur_sub) == 0:
                if len(lonest_sub) > 0:
                    if s[i] < lonest_sub[0]:
                        continue
                cur_sub.append(s[i])
            elif s[j] > cur_sub[-1]:
                cur_sub.append(s[j])
            else:
                continue
            if len(cur_sub) > len(lonest_sub):
                lonest_sub = cur_sub
    return len(lonest_sub)

def LeftSubSequence(s: list) -> int:
    cur_sub = []
    for j in range(len(s)):
        if len(cur_sub) == 0:
            cur_sub.append(s[j])
        elif s[j] < cur_sub[-1]:
            cur_sub.append(s[j])
        else:
            continue
    return len(cur_sub)

def longestSubSequence(s: list) -> int:
    longest = 0
    for i in range(len(s)):
        cur = LeftSubSequence(s[i::-1]) + RightSubSequence(s[i:])
        if cur > longest:
            longest = cur
    return longest-1
    
    

if __name__ == "__main__":
    assert longestSubSequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6