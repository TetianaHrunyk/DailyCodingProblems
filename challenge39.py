"""
Conway's Game of Life takes place on an infinite two-dimensional board of
 square cells. Each cell is either dead or alive, and at each tick, 
 the following rules apply:

    Any live cell with less than two live neighbours dies.
    Any live cell with two or three live neighbours remains living.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.

A cell neighbours another cell if it is horizontally, vertically, 
or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized 
with a starting list of live cell coordinates and the number of steps 
it should run for. Once initialized, it should print out the board state 
at each step. Since it's an infinite board, print out only the relevant 
coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""


class ConwayGame:
    
    def __init__(self, live_coords: list):
        self.rows = max([i[0] for i in live_coords])+1
        self.cols = max([i[1] for i in live_coords])+1
        self.board = []
        for row in range(self.rows):
            temp = []
            for col in range(self.cols):
                if [row, col] in live_coords:
                    temp.append("*")
                else:
                    temp.append(".")
            self.board.append(temp)
        
    def printSolution(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.board[row][col], end = ' ')
            print()
            
    def exploreNeighbors(self, coord):
        steps = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        neighbors = []
        for step in steps:
            nrow = coord[0] + step[0]
            ncol = coord[1] + step[1]
            #print(f"Exploring neighbors: [{nrow},{ncol}]", end = ' ')
            if nrow >= 0 and nrow < self.rows and ncol >= 0 and ncol < self.cols: 
                neighbor = self.board[nrow][ncol]
                #print(neighbor)
                neighbors.append(neighbor)

        return neighbors
    
    def update(self):
        copy = []
        for row in range(self.rows):
            temp = []
            for col in range(self.cols):
                temp.append(".")
            copy.append(temp)
        for row in range(self.rows):
            for col in range(self.cols):
                cell_neighbors = self.exploreNeighbors([row, col])
                #print(f"row{row}, col{col}, neigh = {cell_neighbors}")
                if cell_neighbors.count("*") < 2:
                    copy[row][col] = "."
                elif cell_neighbors.count("*") >= 4:
                    copy[row][col] = "."
                elif cell_neighbors.count("*") == 3:
                    copy[row][col] = "*"
                else:
                    copy[row][col] = self.board[row][col]
        self.board = copy
        
    def run(self, steps):
        print("Initial state: ")
        self.printSolution()
        for i in range(steps):
            self.update()
            print("Iteration #", i+1)
            self.printSolution()
            
if __name__ == "__main__":
    live = [
            [1, 2], [3, 5], [2, 2], [4, 4],
            [0,2], [1, 1], [1, 3], [2, 1],
            [3, 4], [2, 5], [4, 5], [3,2],
            [3, 4], [4, 1], [0, 4], [4,3],
            [4, 4], [0, 2], [0,3], [0,4]
           ]
    game = ConwayGame(live)
    game.run(1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        