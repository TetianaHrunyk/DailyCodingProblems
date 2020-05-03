"""
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that 
returns whether the word can be found in the matrix by going left-to-right, 
or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost 
column. Similarly, given the target word 'MASS', you should return true,
 since it's the last row.
"""

def transpose(m):
    transposed = []
    for i in range(len(m[0])):
        transposed.append([])
    for i in range(len(m)):
        for j in range(len(m[0])):
            transposed[j].append(m[i][j])
    return transposed

def find_word(m, word):
    for i in range(len(m)):
        row = "".join(m[i])
        if word in row:
            return True
    mT = transpose(m)
    for i in range(len(mT)):
        row = "".join(mT[i])
        if word in row:
            return True
    return False
    
if __name__ == "__main__":
    m = [['F', 'A', 'C', 'I'],
         ['O', 'B', 'Q', 'P'],
         ['A', 'N', 'O', 'B'],
         ['M', 'A', 'S', 'S']]
    assert find_word(m, "FOAM") == True
    assert find_word(m, "MASS") == True