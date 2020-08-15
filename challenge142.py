"""You're given a string consisting solely of (, ), and *. * can represent 
either a (, ), or an empty string. Determine whether the parentheses are balanced.
For example, (()* and (*) are balanced. )*( is not balanced."""

def is_balanced(s: str):
    opened = 0
    closed = 0
    stars = 0
    stars_needed = []
    for i in range(len(s)):
        char = s[i]
        if char == ")":
            if opened > 0:
                opened -= 1
                stars_needed.pop()
            else:
                if stars > 0:
                    stars -= 1
                    closed -= 1
                else:
                    return False
        elif char == "(":
            opened += 1
            stars_needed.append(i)
        else:
            stars +=1
    if len(stars_needed) > stars:
        return False
    for i in stars_needed:
        if "*" not in s[i+1:]:
            return False
    return True

if __name__ == "__main__":
    assert is_balanced("(()*)") == True
    assert is_balanced("(*)") == True
    assert is_balanced(")*(") == False
    assert is_balanced("***((()") == False