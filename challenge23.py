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
    board_copy = board.copy()
    rows = len(board)
    cols = len(board[0])
    for i in range()
    
    
    
    
    
            
if __name__ == "__main__":
    board = [['f', 'f', 'f', 'f'],
            ['t', 't', 'f', 't'],
            ['f', 'f', 'f', 'f'],
            ['f', 'f', 'f', 'f']]
    print(shortestPath(board, [3, 0], [0, 0]))