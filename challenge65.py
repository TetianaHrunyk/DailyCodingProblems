"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
"""

def clockwiseSpiral(m):
    if len(m) == 0:
        return
    print(*m[0], end = " ")
    m.pop(0)
    for i in range(len(m)-1):
        print(m[i][-1], end = " ")
        m[i].pop()
    h = m[-1]
    print(*h[::-1], end = " ")
    m.pop()
    for j in range(len(m)-1):
        print(m[-i][0], end = " ")
        m[-i].pop(0)
    clockwiseSpiral(m)
    
if __name__ == "__main__":
    m = [[1,  2,  3,  4,  5],
         [6,  7,  8,  9,  10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]]
    clockwiseSpiral(m)