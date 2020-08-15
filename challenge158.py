"""You are given an N by M matrix of 0s and 1s. Starting from the top left corner,
how many ways are there to reach the bottom right corner?
You can only move right and down. 0 represents an empty space 
while 1 represents a wall you cannot walk through.
For example, given the following matrix:
[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:
    Right, down, down, right
    Down, right, down, right
The top left corner and bottom right corner will always be 0"""

steps = [[0, 1], [1, 0]]

def is_valid_step(step, a, b, rows, cols):
    if a+step[0]>=0 and a+step[0]<rows and b+step[1]>=0 and b+step[1]<cols:
        return True
    return False


def ways_to_get_down_helper(m, row, col, rows, cols):
    global ways
    if row == rows-1 and col == cols-1:
        return 1
    for step in steps:
        if is_valid_step(step, row, col, rows, cols):
            if m[row+step[0]][col+step[1]] == 0:
                row+=step[0]
                col+=step[1]
                if ways_to_get_down_helper(m, row, col, rows, cols) == 1:
                    ways += 1
                row-=step[0]
                col-=step[1]
   

def ways_to_get_down(m):
    global ways
    ways=0
    ways_to_get_down_helper(m, 0, 0, len(m), len(m[0]))
    return ways

if __name__ == "__main__":
    m = [[0, 0, 1],
         [0, 0, 1],
         [1, 0, 0]]
    assert ways_to_get_down(m) == 2
    
    m = [[0, 0, 1],
         [0, 0, 1],
         [1, 1, 0]]
    assert ways_to_get_down(m) == 0
    
    m = [[0, 0, 0, 1],
         [0, 0, 0, 1],
         [1, 1, 0, 0]]
    assert ways_to_get_down(m) == 3
    
    m = [[0, 0, 0, 1],
         [0, 0, 0, 1],
         [1, 0, 0, 0]]
    assert ways_to_get_down(m) == 5
    