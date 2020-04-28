"""
Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.
"""

def countVals(n, val):
    count = 0
    for i in range(1, n+1):
        row = [i*j for j in range(1, n+1)]
        count += row.count(val)
        
    return count

if __name__ == "__main__":
    assert countVals(6, 12) == 4
    assert countVals(6, 1) == 1
    assert countVals(6, 45) == 0
    assert countVals(6, 10) == 2