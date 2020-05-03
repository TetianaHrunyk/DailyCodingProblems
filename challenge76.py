"""You are given an N by M 2D matrix of lowercase letters. Determine the minimum
 number of columns that can be removed to ensure that each row is ordered 
 from top to bottom lexicographically. That is, the letter at each column is 
 lexicographically later as you go down each row. It does not matter whether 
 each row itself is ordered lexicographically.
For example, given the following table:
cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second 
column to make it ordered:
ca
df
gi
So your function should return 1, since we only needed to remove 1 column.
As another example, given the following table:
abcdef
Your function should return 0, since the rows are already ordered 
(there's only one row).
As another example, given the following table:
zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order it.
"""

from challenge63 import transpose

def dropCols(m):
    mT = transpose(m)
    droppedCols = 0
    i, j = 0, 0
    while (i <= (len(mT)-1)) and len(mT) > 0:
        while (j <= (len(mT[0])-2)) and len(mT) > 0:
            if mT[i][j] > mT[i][j+1]:
                mT.pop(i)
                droppedCols += 1
                i-=1
                break
            j+=1
        j=0
        i+=1
    return droppedCols

if __name__ == "__main__":
    m = [["c", "b", "a"],
         ["d", "a", "f"],
         ["g", "h", "i"]]
    assert dropCols(m) == 1
    
    m = [["a", "b", "c", "d", "e", "f", "g"]]
    assert dropCols(m) == 0
    
    m = [["z", "y", "x"],
         ["w", "v", "u"],
         ["t", "s", "r"]]
    assert dropCols(m) == 3