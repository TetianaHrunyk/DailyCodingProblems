"""Given a string which we can delete at most k, return whether you can make a palindrome.
For example, given 'waterrfetawx' and a k of 2, 
you could delete f and x to get 'waterretaw'.
"""
def is_palindrom(s: str):
    half = len(s)//2
    if len(s)%2 == 0:
        s = s[:half]+"a"+s[half:]
    if s[:half] == s[-1:half:-1]:
        return True
    return False


def can_get_palindrome(s: str, k: int, counter = 0):
    if is_palindrom(s):
        return True
    if counter >= k:
        return False
    for i in range(len(s)):
        dropped = s[i]
        s = s[:i]+s[i+1:]
        if can_get_palindrome(s, k, counter+1):
            return True
        s = s[:i]+dropped+s[i:]
    return False

if __name__ == "__main__":
    assert can_get_palindrome('waterrfetawx', 2) == True
    assert can_get_palindrome('waterrfetawx', 3) == True
    assert can_get_palindrome('waterrfeetawx', 2) == False
    assert can_get_palindrome('waterrfeetawx', 3) == True
    
        
                