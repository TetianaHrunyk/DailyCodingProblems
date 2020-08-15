"""Given a start word, an end word, and a dictionary of valid words, 
find the shortest transformation sequence from start to end such that
 only one letter is changed at each step of the sequence, and each transformed
 word exists in the dictionary. If there is no possible transformation, return null. 
 Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat",
 and dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, r
eturn null as there is no possible transformation from dog to cat."""
import sys

def words_diff(w1, w2):
    diff = 0    
    for a, b in zip(w1, w2):
        if a!=b:
            diff+=1
    return diff

def shortest_path(w1, w2, d):
    global shortest
    shortest = []
    shortest_path_helper(w1, w2, d, [w1])
    if shortest:
        return sorted(shortest, key=lambda x: len(x))[0]
    else:
        return None

def shortest_path_helper(w1, w2, d, used):
#    print(used)
    if w1 == w2:
        shortest.append(used.copy())

    for dword in d:
        if words_diff(dword, w1) == 1:
            if dword not in used:
                used.append(dword)
                w1 = dword
                shortest_path_helper(w1, w2, d, used)
                used.pop()
                w1 = used[-1]
                

    
    
if __name__ == "__main__":
    assert shortest_path("dog", "cat", {"dot", "dop", "dat", "cat"}) == ['dog', 'dot', 'dat', 'cat']
    assert shortest_path("dog", "cat", {"dot", "tod", "dat", "dar"}) == None