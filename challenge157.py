"""Given a string, determine whether any permutation of it is a palindrome.
For example, carrace should return true, since it can be rearranged to 
form racecar, which is a palindrome. daily should return false, 
since there's no rearrangement that can form a palindrome."""

def can_get_palindrom(s: str):
    letter_counts = dict()
    for letter in s:
        if letter in letter_counts.keys():
            letter_counts[letter]+=1
        else:
            letter_counts[letter]=1        
    odd = 0
    for value in letter_counts.values():
        if value%2 != 0:
            odd += 1
        if odd >1:
            return False
    return True

if __name__ == "__main__":
    assert can_get_palindrom("racecar") == True
    assert can_get_palindrom("racecara") == False
    
    