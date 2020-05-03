"""Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
 A 1 represents land and 0 represents water, so an island is a group of 1s that 
 are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""
import math

class FindIsland:
    
    def __init__(self, board):
        self.board = board
        self.islands = []
        
    def get_land(self):
        land = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 1:
                    land.append([i, j])
        return land
    
    def get_islands(self):
        l = self.get_land()
        if len(l) == 0:
            return 0
        islands = 1
        self.islands.append([l[0]])
        for i in range(1, len(l)):
            add_new_island = True
#            print("Contemplated piece of land: ", l[i])
            for j in range(len(self.islands)):
                for z in range(len(self.islands[j])):
                    if math.isclose(self.islands[j][z][0], l[i][0], abs_tol = 1):
                        if math.isclose(self.islands[j][z][1], l[i][1], abs_tol = 1):
                            self.islands[j].append([l[i][0], l[i][1]])
                            add_new_island = False
#                            print("Expanded island: ", self.islands[j])
                            break
            if add_new_island:
#                print("New island is discovered: ", [l[i][0], l[i][1]])
                islands += 1
                self.islands.append([[l[i][0], l[i][1]]])
#            print()
#        print(self.islands)
        return islands
    
if __name__ == "__main__":
    board = [[1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [1, 1, 0, 0, 1]]
    set_for_island_search = FindIsland(board)
    assert set_for_island_search.get_islands() == 4
    
    board = [[1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [1, 1, 0, 0, 1]]
    set_for_island_search = FindIsland(board)
    assert set_for_island_search.get_islands() == 3
    
    board = [[1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [1, 1, 0, 0, 1]]
    set_for_island_search = FindIsland(board)
    assert set_for_island_search.get_islands() == 4
    
    board = [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]]
    set_for_island_search = FindIsland(board)
    assert set_for_island_search.get_islands() == 1
    
    
    
    
            