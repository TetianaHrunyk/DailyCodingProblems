"""
Given an undirected graph represented as an adjacency matrix and an integer k, 
write a function to determine whether each vertex in the graph can be colored
 such that no two adjacent vertices share the same color using at most k colors.
"""

def can_color_graph(m, k):
    max_adjacencies = 0
    for row in m:
        max_adjacencies = max(max_adjacencies, sum(row))

    return k > max_adjacencies
    
    
if __name__ == "__main__":
    m = [[1, 1, 0, 0],
         [1, 1, 1, 1],
         [0, 1, 1, 1],
         [0, 1, 1, 1]
        ]

    assert can_color_graph(m, 5) == True
    assert can_color_graph(m, 2) == False
    
            