"""You are given a 2-d matrix where each cell represents number of coins in that cell.
Assuming we start at matrix[0][0], and can only move right or down, find the maximum 
number of coins you can collect by the bottom right corner.

For example, in this matrix
0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins."""


def driver(board, a=0, b=0, cur_sum = 0):
    if a >= (len(board)-1) or b >= (len(board[0])-1):  
        cur_sum += board[a][b]
        return cur_sum
    cur_sum += board[a][b]    
    a1 = a+1
    b1 = b+1
    return max(driver(board, a1, b1, cur_sum), driver(board, a1, b, cur_sum), driver(board, a, b1, cur_sum))
    

def get_max_coins(board):
    a = len(board)
    b = len(board[0])
    if a > b:
        to_add = a-b
        for row in board:
            for _ in range(to_add):
                row.append(0)
    if b > a:
        to_add = b-a
        for _ in range(to_add):
            board.append([0 for _ in range(b)])
    return driver(board)
        

if __name__ == "__main__":
    board = [[0, 3, 1, 1],
            [2, 0, 0, 4],
            [1, 5, 3, 1]]
    assert get_max_coins(board) == 12