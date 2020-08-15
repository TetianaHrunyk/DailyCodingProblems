"""Given a 2D board of characters and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
For example, given the following board:
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, 
exists(board, "ABCB") returns false.
"""

def is_option(board, pos, char):
    options = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    res = []
    for option in options:
        try:
            if board[pos[0]+option[0]][pos[1]+option[1]] == char:
                res.append(option)
        except:
            pass
    return res

def exists_helper(board, s, index, pos, origin):
    if index == len(s):
        return True
    options = is_option(board, pos, s[index])
    for option in options:
        pos[0] += option[0]
        pos[1] += option[1]
        if origin != pos:
            origin = pos.copy()
            origin[0] -=  option[0]
            origin[1] -=  option[1]
            index += 1
            if exists_helper(board, s, index, pos, origin):
                return True
            index -= 1
            pos[0] -= option[0]
            pos[1] -= option[1]
    return False

def exists(board, s):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == s[0]:
                if exists_helper(board, s, 1, [i, j], [i, j]) == True:
                    return True
    return False
        



if __name__ == "__main__":
    board = [
              ['A','B','C','E'],
              ['S','F','C','S'],
              ['A','D','E','E']
            ]
    
    assert exists(board, "ABCCED") == True
    assert exists(board, "SEE") == True
    assert exists(board, "ABCB") == False
    
    
        