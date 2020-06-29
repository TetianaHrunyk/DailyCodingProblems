"""Given a string which we can delete at most k, return whether you can make a palindrome.
For example, given 'waterrfetawx' and a k of 2, 
you could delete f and x to get 'waterretaw'.
"""
def is_palindrom(s: str):
    half = len(s)//2
    if len(s)%2 == 0:
        s = s[:half]+"m"+s[half:]
        print(s)
    if s[:half] == s[-1:half:-1]:
        return True
    return False


def can_get_palindrome(s: str, k: int):
    pass
                