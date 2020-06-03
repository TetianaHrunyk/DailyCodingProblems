"""Given two strings A and B, return whether or not A can be shifted some number
 of times to get B.
For example, if A is abcde and B is cdeab, return true. 
If A is abc and B is acb, return false.
"""

def can_get_by_shifting(A, B):
    for i in range(len(A)):
        A = A[1:] + A[0]
        if A == B:
            return True
    return False

if __name__ == "__main__":
    assert can_get_by_shifting("abcde", "cdeab") == True
    assert can_get_by_shifting("abc", "acb") == False
    assert can_get_by_shifting("abc", "abc") == True
        