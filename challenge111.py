"""Given a word W and a string S, find all starting indices in S which are anagrams of W.
For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4
"""

def all_present(a, b):
    if len(a) != len(b):
        return False
    for achar in a:
        if achar not in b:
            return False
    return True

def anagrams_indices(w, s):
    indices = []
    wlen = len(w)
    for i in range(len(s)-wlen+1):
        if all_present(w, s[i:i+wlen]):
            indices.append(i)
    return indices

if __name__ == "__main__":
    assert anagrams_indices("ab", "abxaba") == [0, 3, 4]
    assert anagrams_indices("acd", "dca") == [0]
