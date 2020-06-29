"""Given an N by M matrix consisting only of 1's and 0's, 
find the largest rectangle containing only 1's and return its area.
For example, given the following matrix:
[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
Return 4."""
from challenge63 import transpose

def largest_rectangle_helper(m):
    max_area = 0
    for i in range(len(m)):
        row = m[i]
        for j in range(i+1, len(m)):                
            row = [a and b for a, b in zip(row, m[j])]
            
            ones = 0
            ones_clusters = []
            for r in range(len(row)):
                if row[r] == 1:
                    ones +=1
                else:
                    ones_clusters.append(ones)
                    ones = 0
            ones_clusters.append(ones)
            #if there are no more ones in the line, it makes no sense to continue checking
            if max(ones_clusters) == 0:
                break
            curr_area = max(ones_clusters)*(j-i+1)
            if curr_area > max_area:
                max_area = curr_area

    return max_area

def largest_rectangle(m):
    return max(largest_rectangle_helper(m), largest_rectangle_helper(transpose(m)))
        

        
if __name__ == "__main__":
    m = [[1, 0, 0, 0],
         [1, 0, 1, 1],
         [1, 0, 1, 1],
         [0, 1, 0, 0]]
    assert largest_rectangle(m) == 4
    
    m = [[1, 0, 0, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 0],
         [0, 1, 0, 0]]
    assert largest_rectangle(m) == 6
    
    m = [[0, 0, 0, 0],
         [1, 0, 1, 0],
         [1, 0, 1, 0],
         [1, 0, 1, 0]]
    assert largest_rectangle(m) == 3
    
    matrix = [[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1]]
    assert largest_rectangle(matrix) == 16
    
    matrix = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    assert largest_rectangle(matrix) == 0
    
    matrix = [[1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 0, 0],
              [0, 0, 0, 0]]
    assert largest_rectangle(matrix) == 8
    
    matrix = [[1, 1, 0, 0],
              [1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 0, 0, 0]]
    assert largest_rectangle(matrix) == 4

    
    
    
    
    
    