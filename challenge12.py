"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can 
climb up either 1 or 2 steps at a time. Given N, 
write a function that returns the number of unique ways 
you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2
"""

def ClimbingStairs(n: int, step = [1, 2]) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return 1 + ClimbingStairs(n-1, step)
    
    
if __name__ == '__main__':
    assert ClimbingStairs(4) == 5
    assert ClimbingStairs(1) == 1
    assert ClimbingStairs(2) == 3