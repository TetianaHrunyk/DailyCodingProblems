"""You are given an M by N matrix consisting of booleans 
that represents a board.
 Each True boolean represents a wall. Each False boolean represents a tile
 you can walk on.

Given this matrix, a start coordinate, and an end coordinate, 
return the minimum number of steps required to reach 
the end coordinate from the start. If there is no possible path, 
then return null. You can move up, left, down, and right. 
You cannot move through walls. You cannot wrap around the edges of the board
"""

def shortestPath(board, start, end):
    if start == end:
        return 0
    
    rows = len(board)-1
    cols = len(board[0])-1
    
    paths = [[0, start] * 4]
    steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while len(paths) != 0:
        #print("here")
        p = paths[0]
        paths.pop(0)
        if p not in paths:
            print("removed")
        for step in steps:
            #print("stepping")
            p[-1][0] += step[0]
            p[-1][1] += step[1]
            if p[-1][0] >= 0 and p[-1][0] <=rows and p[-1][1] >= 0 and p[-1][1]<=cols:
                #print(p[-1][0], ' ', p[-1][1])
                if board[p[-1][0]][p[-1][1]] == 'f':
                    p[0] += 1
                    paths.append(p)
                else:
                    continue
            if p[-1] == end:
                return p[0]
    return None
            
if __name__ == "__main__":
    board = [['f', 'f', 'f', 'f'],
            ['t', 't', 'f', 't'],
            ['f', 'f', 'f', 'f'],
            ['f', 'f', 'f', 'f']]
    print(shortestPath(board, [3, 0], [0, 0]))