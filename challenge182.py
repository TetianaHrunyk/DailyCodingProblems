"""A graph is minimally-connected if it is connected and there is no edge that can
 be removed while still leaving the graph connected. For example, any binary tree
 is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected. 
You can choose to represent the graph as either an adjacency matrix or 
adjacency list."""

def is_min_connected(m):
    edges = 0
    for i in range(len(m)):
        ones = m[i].count(1)
        if ones == 0:
            return False
        edges += ones
    if edges / 2 == len(m) - 1:
        return True
    return False

if __name__ == "__main__":
    min_con = [[0, 1, 1],
               [1, 0, 0],
               [1, 0, 0]
              ]
    
    not_min_con= [[0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 0]
                 ]  
    
assert is_min_connected(min_con) == True
assert is_min_connected(not_min_con) == False