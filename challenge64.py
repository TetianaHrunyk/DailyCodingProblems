"""
A knight's tour is a sequence of moves by a knight on a chessboard such that
 all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N 
chessboard.
"""

def isSafe(x, y, board):
    if(x >= 0 and y >= 0 and x < len(board) and y < len(board) and board[x][y] == -1): 
        return True
    return False

def solve_helper(board, curr_x, curr_y, move_x, move_y, pos, ways):
    if (pos == (len(board)**2)):
        return True
    for i in range(8): 
        new_x = curr_x + move_x[i] 
        new_y = curr_y + move_y[i] 
        if(isSafe(new_x,new_y,board)): 
            board[new_x][new_y] = pos 
            
            if(solve_helper(board,new_x,new_y,move_x,move_y,pos+1, ways)): 
                ways+=1
                return ways
              
            board[new_x][new_y] = -1
            
    return False

def solve(n):
    board = [[-1 for i in range(n)]for i in range(n)] 

    move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
    move_y = [1, 2, 2, 1, -1, -2, -2, -1] 
    
    board[0][0] = 0
    pos = 1
    ways = 0
    
    res = solve_helper(board, 0, 0, move_x, move_y, pos, ways)
    if(not res): 
        print("Solution does not exist") 
    else: 
        print(res)
        
if __name__ == "__main__":
    solve(5)