"""Given a string and a set of characters, return the shortest substring containing 
all the characters in the set.
For example, given the string "figehaeci" and the set of characters {a, e, i}, 
you should return "aeci".
If there is no substring containing all the characters in the set, return null.
"""

def shortest_substr(s: str, chars: set):
    for char in chars:
        if char not in s:
            return None
    while s[0] not in chars:
        s = s[1:]
    while s[-1] not in chars:
        s = s[:-1]
    left = s[0]
    left_set = chars.copy()
    left_set.remove(s[0])
    right = s[-1]
    right_set = chars.copy()
    right_set.remove(s[-1])
    i = 1
    while True and i<30:
        left += s[i]
        if s[i] in left_set:
            left_set.remove(s[i])
        if len(left_set) == 0:
            return left
        right = s[-i-1] + right
        if s[-i-1] in right_set:
            right_set.remove(s[-1-i])
        if len(right_set) == 0:
            return right
        i+=1
        
if __name__ == "__main__":
    assert shortest_substr("figehaeci", {"a", "e", "i"}) == "aeci"
        