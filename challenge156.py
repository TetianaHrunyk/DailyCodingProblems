"""Given a positive integer n, find the smallest number of squared integers which
 sum to n.

For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9."""
import math

def sqared_int(n: int):
    res = 0
    i = math.floor(math.sqrt(n))
    while True:   
        if n-i**2 == 0:
            return res + 1
        if n-i**2 >0:
            res += 1
            n-=i**2
        else:
            i -= 1
    
if __name__ == "__main__":
    assert sqared_int(13) == 2
    assert sqared_int(27) == 3
    assert sqared_int(81) == 1