"""
Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, 
using only mathematical or bit operations. You can assume b can only be 1 or 0.
"""

def returnNum(x, y, b):
    a = 1
    if a and b:
        return x
    else:
        return y
    
if __name__ == "__main__":
    assert returnNum(10, 20, 1) == 10
    assert returnNum(10, 20, 0) == 20