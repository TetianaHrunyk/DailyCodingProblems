"""
Given a string, find the palindrome that can be made by inserting 
the fewest number of characters as possible anywhere in the word.
 If there is more than one palindrome of minimum length that can be made, 
 return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace",
 since we can add three letters to it (which is the smallest
 amount to make a palindrome). There are seven other palindromes
 that can be made from "race" by adding three letters, but "ecarace" 
 comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""

#source: https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_034.py

def is_palindrome(s: str):
    return s == s[::-1]



def get_nearest_palindrome(s):

    if is_palindrome(s):
        return s

    if s[0] == s[-1]:
        return s[0] + get_nearest_palindrome(s[1:-1]) + s[-1]
    else:
        pal_1 = s[0] + get_nearest_palindrome(s[1:]) + s[0]
        pal_2 = s[-1] + get_nearest_palindrome(s[:-1]) + s[-1]

        if len(pal_1) > len(pal_2):
            return pal_2
        elif len(pal_1) < len(pal_2):
            return pal_1
        return pal_1 if pal_1 < pal_2 else pal_2

if __name__ == "__main__":
    assert get_nearest_palindrome("racecar") == "racecar"
    assert get_nearest_palindrome("google") == "elgoogle"
    assert get_nearest_palindrome("egoogle") == "elgoogle"
    assert get_nearest_palindrome("elgoog") == "elgoogle"
    assert get_nearest_palindrome("race") == "ecarace"




