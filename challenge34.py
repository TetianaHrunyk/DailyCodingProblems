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

def makePalindrom(s: str, pivot) -> tuple:
    """
    The function takes a pivot value.
    If pivot is an int, it returns a tuple of palindrome around 
    the letter with that index in the string s and the number of characters
    that have bo be added to get it.
    If pivot is float, it will return a palindrome around the 'gap'
    between the top and bottom positions.
    To get the palindrome around the gap before first letter,
    use pivot in range (-1, 0).
    To get palindrom around the last letter, use pivot = len(s)-1.
    NOTE: indexing starts with 0, so to get palindrom around nth letter
    use pivot = n-1.
    """
    assert (type(pivot) == float) or (type(pivot) == int)
    assert pivot > -1 and pivot < len(s)
    import math
    added_chars = 0
    pivot_val = ""
    if pivot == 0:
        added_chars = len(s)-1
        res = s[::-1]+s[1:]
        return (res, added_chars)
    if type(pivot) == int:
        left = s[:pivot]
        pivot_val = s[pivot]
        right = s[(pivot+1):]
    else:
        left = s[:math.ceil(pivot)]
        right = s[math.ceil(pivot):]
    i = 0
    while left != right[::-1]:
        if i >= len(right):
            right += left[-i-1]
        elif i >= len(left):
            left = right[i] + left
        else:
            if left[-i-1] != right[i]:
                better = min(left[-i-1], right[i])
                if left[-i-1] == better:

                    right = right[:i] + better + right[i:]
                else:
                    left = left[::-1]
                    left = left[:i] + better + left[i:]  
                    left = left[::-1]
        i += 1
        added_chars += 1
    
    res = left + pivot_val +right
    return (res, added_chars)

def shortes1stAlphabeticallyPalindrom(s: str) -> str:
    best = makePalindrom(s, -0.8)
    i = 0
    for j in range(len(s)*2):
        print(i)
        palindrom = makePalindrom(s, i)
        print(f"Palindrom {palindrom}, best {best}")
        if (palindrom[0] <= best[0]) and (palindrom[1] <= best[1]):
            best = palindrom
        i += 0.5
    palindrom = makePalindrom(s, len(s) - 0.5)
    if (palindrom[0] <= best[0]) and (palindrom[1] <= best[1]):
        best = palindrom
    return best[0]    

if __name__ == "__main__":
    pass