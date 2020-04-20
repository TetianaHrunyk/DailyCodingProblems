"""
There is an N by M matrix of zeroes. Given N and M, write a function to count 
the number of ways of starting at the top-left corner and getting to
 the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are 
two ways to get to the bottom-right:

    Right, then down
    Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right."""

def isSafe(pos, step, size):
    a = (pos[0] + step[0])
    if a >= 0 and a <= size[0]:
        b = (pos[1] + step[1])
        if b >= 0 and b <= size[1]: 
            return True
    return False

def matrix_traversal_helper(row_count, col_count, curr_row, curr_col):

    if curr_row == row_count - 1 and curr_col == col_count - 1:
        return 1

    count = 0
    if curr_row < row_count - 1:
        count += matrix_traversal_helper(row_count, col_count,
                                         curr_row + 1, curr_col)
    if curr_col < col_count - 1:
        count += matrix_traversal_helper(row_count, col_count,
                                         curr_row, curr_col + 1)

    return count


def get_matrix_traversals(row_count, col_count):
    if not row_count or not col_count:
        return None
    count = matrix_traversal_helper(row_count, col_count, 0, 0)
    return count


assert not get_matrix_traversals(1, 0)
assert get_matrix_traversals(1, 1) == 1
assert get_matrix_traversals(2, 2) == 2
assert get_matrix_traversals(5, 5) == 70
    
    
    
    
    
    
    
    