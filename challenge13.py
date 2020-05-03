"""
Given an integer k and a string s, find the length of the longest
 substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest 
substring with k distinct characters is "bcb".
"""

def distinct(string):
    return len(''.join(set(string)))

def longestStr(s: str, k: int) -> str:
    assert k >= 0
    longest = ''
    cur_longest = ''
    for char in s:
        cur_longest += char
        if distinct(cur_longest) <= k:
            if len(cur_longest) > len(longest):
                longest = cur_longest
        else:
            while distinct(cur_longest) > k:
                cur_longest = cur_longest[1:]
    return longest

if __name__ == '__main__':
    assert longestStr("abcba", 2) == 'bcb'
    assert longestStr("abcba", 3) == 'abcba'
    assert longestStr("abcba", 0) == ''
    assert longestStr("bbbbbbbb", 1) == 'bbbbbbbb'
    assert longestStr("bbbbbbbb", 4) == 'bbbbbbbb'
    assert longestStr("abgfjfjfjdkdkd", 3) == 'gfjfjfj'