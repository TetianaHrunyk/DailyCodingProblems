"""
Given a string of round, curly, and square open and closing brackets,
 return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def balanced(s: str) -> bool:
    brackets = 0
    couples = {'(': ')', '[':']', '{':'}'}
    opened = []
    for char in s:
        for open_bracket in ["(", "[", "{"]:
            if char == open_bracket:
                opened.append(char)
                brackets += 1
                break
        for closed_bracket in [")", "]", "}"]:
            if char == closed_bracket:
                if couples[opened[-1]] != char or len(opened) == 0:
                    return False
                else:
                    opened.pop(-1)
                    brackets -= 1
                    break

    if brackets == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    assert balanced("([])[]({})") == True
    assert balanced("([)]") == False
    assert balanced("((()") == False
    
    
    
            