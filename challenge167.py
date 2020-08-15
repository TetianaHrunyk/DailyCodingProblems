"""Given a list of words, find all pairs of unique indices such that 
the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], 
return [(0, 1), (1, 0), (2, 3)]."""

def is_palindrom(word):
    if word == word[::-1]:
        return True
    return False

def palindrom_pairs(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and is_palindrom(arr[i]+arr[j]):
                pairs.append((i, j))
    return pairs

if __name__ == "__main__":
    assert palindrom_pairs(["code", "edoc", "da", "d"]) == [(0, 1), (1, 0), (2, 3)]