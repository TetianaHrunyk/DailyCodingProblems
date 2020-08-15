"""Given a string of parentheses, write a function to compute the minimum number 
of parentheses to be removed to make the string valid (i.e. each open parenthesis
 is eventually closed).

For example, given the string "()())()", you should return 1. Given the string
 ")(", you should return 2, since we must remove all of them.
"""

def removeRedundantParenthesis(s: str):
    open_par = False
    redundant = 0
    for char in s:
        if char == "(":
            open_par = True
            redundant += 1
        elif char == ")" and (not open_par):
            redundant += 1
        elif char == ")" and open_par:
            redundant -= 1
            open_par = False
    return redundant

if __name__ == "__main__":
    assert removeRedundantParenthesis("()())()") == 1
    assert removeRedundantParenthesis(")(") == 2
    assert removeRedundantParenthesis(")((") == 3
    assert removeRedundantParenthesis("()") == 0