def longestSubstring(s1, s2: str) -> str:
    cur_longest = ''
    longest = ''
    for char in s1:
        cur_longest += char
        if cur_longest in s2:
            if cur_longest > longest:
                longest = cur_longest
        else:
            cur_longest = char
    return longest
    
if __name__ == '__main__':
    assert longestSubstring("aaaa", "aab") == "aa"
    assert longestSubstring("typing", "sleeping") == "ping"
    
