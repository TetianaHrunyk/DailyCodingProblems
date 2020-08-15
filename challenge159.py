"""Given a string, return the first recurring character in it, or null if there 
is no recurring character.
For example, given the string "acbbac", return "b". Given the string "abcdef", 
return null.
"""

def first_recurring(s: str):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return s[i]
    return None

if __name__ == "__main__":
    assert first_recurring("acbbac") == "b"
    assert first_recurring("abcdef") == None