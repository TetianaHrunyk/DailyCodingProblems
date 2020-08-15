"""Given a string s and a list of words words, where each word is the same length,
find all starting indices of substrings in s that is a concatenation of every word 
in words exactly once.
For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"],
return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.
Given s = "barfoobazbitbyte" and words = ["dog", "cat"],
return [] since there are no substrings composed of "dog" and "cat" in s.
The order of the indices does not matter."""

def permute(A: set):
    if len(A)==1:
        return [list(A)]
    permutations = []
    for x in A:
        for y in permute(A-{x}):
            permutations.append([x]+y)
    return permutations

def concat_substr(s, words):
    ind = []
    perms = permute(set(words))
    for perm in perms:
        sub = "".join(perm)
        if s.find(sub) >= 0:
            ind.append(s.find(sub))
        else:
            return []
    return ind

if __name__ == "__main__":
    assert concat_substr("dogcatcatcodecatdog", ["cat", "dog"]) == [0, 13]
    assert concat_substr("barfoobazbitbyte", ["cat", "dog"]) == []
