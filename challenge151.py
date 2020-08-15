"""Given a 2-D matrix representing an image, a location of a pixel in the 
screen and a color C, replace the color of the given pixel and all adjacent
 same colored pixels with C.
For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:
B B W
W W W
W W W
B B B
Becomes
B B G
G G G
G G G
B B B       """

class Recolor:
    
    def __init__(self, m):
        self.m = m
        self.steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.rows = len(self.m)
        self.cols = len(self.m[0])
        
    def needs_recoloring(self, a, b, color):
        if a >= 0 and a < self.rows and b >= 0 and b < self.cols:
            if self.m[a][b] == color:
                return True
        return False
    
    def recolor(self, loc: tuple, color: str):
        
        def recolor_rec(a, b, col, init_col):
            for step in self.steps:
                if self.needs_recoloring(a+step[0], b+step[1], init_col):
                    a += step[0]
                    b += step[1]
                    self.m[a][b] = col
                    recolor_rec(a, b, col, init_col)
                    a -= step[0]
                    b -= step[1]
                    
        recolor_rec(loc[0], loc[1], color, self.m[loc[0]][loc[1]])
        
    def print_pic(self):
        for row in self.m:
            print(row)
        print()
            
if __name__ == "__main__":
    m = [['B', 'B',  'W'],
        ['W',  'W', 'W'],
        ['W', 'W', 'W'],
        ['B', 'B', 'B']]
    solution = Recolor(m)
    solution.print_pic()
    solution.recolor((2, 2), 'G')
    solution.print_pic()
    
    
    
    
    
            
    