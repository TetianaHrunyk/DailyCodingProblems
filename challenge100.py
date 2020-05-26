"""You are in an infinite 2D grid where you can move in any of the 8 directions:
 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. 
Give the minimum number of steps in which you can achieve it. 
You start from the first point.
Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2

It takes 1 step to move from (0, 0) to (1, 1). 
It takes one more step to move from (1, 1) to (1, 2).
"""

def needed_steps(path: list, steps=0):
    if len(path) > 1:
        return steps + needed_steps(path[1:], max(abs(path[1][0]-path[0][0]), abs(path[1][1]-path[0][1])))
    return steps

if __name__ == "__main__":
    assert needed_steps([(0, 0), (1, 1), (1, 2)]) == 2
    assert needed_steps([(0, 0), (1, 2)]) == 2
    assert needed_steps([(0, 0), (1, 0), (1, 1), (1, 2)]) == 3