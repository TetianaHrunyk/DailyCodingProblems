"""Implement division of two positive integers without using the division, 
multiplication, or modulus operators. Return the quotient as an integer, 
ignoring the remainder.
"""

def divide(a, b):
    if a < b:
        return 0
    res = 1
    c = b
    while c < a:
        c+=b
        res+=1
        if c>a:
            res -= 1
    return res

if __name__ == "__main__":
    assert divide(4, 2) == 2
    assert divide(9, 2) == 4
    assert divide(9, 14) == 0
    
    
    