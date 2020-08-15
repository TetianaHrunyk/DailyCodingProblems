"""Given an N by N matrix, rotate it by 90 degrees clockwise.
For example, given the following matrix:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?"""

def rotate90deg(m, i=0):
    if i == 0:
        m = m[::-1]
    n = len(m)-i
    if n == 1:
        return 
    if n == 2:
        m[1+i][i], m[i][1+i] = m[i][1+i], m[1+i][i]
        return   
    for j in range(i, n):
        m[i][j], m[j][i] = m[j][i], m[i][j]
    
    rotate90deg(m, i+1)
    return m
    
if __name__ == "__main__":
    assert rotate90deg([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == \
                        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
                        
    
    assert rotate90deg([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) \
                   == [[13, 9, 5, 1], [14, 10, 6, 12], [15, 11, 7, 3], [16, 2, 8, 4]]
        