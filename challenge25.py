"""
'.' Matches any single character.
'*' Matches zero or more  elements.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cs = 0
        cp = 0
        while cs < len(s):
            if p[cp] != s[cs] and cd < len(p):
                if p[cp] == '.':
                    if (not s[cs].islower()):
                        return False
                elif p[cp] == "*":
                    while s[cs] != p[cp] and cs < len(s):
                        cs += 1
                else:
                    return False
            cs += 1
            cp += 1
        if ('.' not in p) and ('*' not in p) and (len(p) < len(s)):
            return False
        return True

            
if __name__ == '__mian__':
    solver = Solution()
    
    s = "aa"
    p = "a"
    assert solver.isMatch(s, p) == False
    
    s = "aa"
    p = "a*"
    assert solver.isMatch(s, p) == True
    
    s = "ab"
    p = ".*"
    assert solver.isMatch(s, p) == True
    
    s = "mississippi"
    p = "mis*is*p*."
    assert solver.isMatch(s, p) == True