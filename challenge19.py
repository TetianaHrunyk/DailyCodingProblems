"""
A builder is looking to build a row of N houses that can be 
of K different colors. He has a goal of minimizing cost while 
ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column
 represents the cost to build the nth house with kth color, 
 return the minimum cost which achieves this goal.
"""

import sys
def minCost(costs):
    N = len(costs)
    K = len(costs[0])
    
    prev_min, prev_min2, prev_min_index = 0, 0, -1
    
    for i in range(N):
        cur_min, cur_min2, cur_min_index = sys.maxsize, sys.maxsize, -1
        
        for j in range(K):

            val = costs[i][j] + (prev_min if  j != prev_min_index else prev_min2)
            
            if cur_min_index == -1:
                cur_min = val
                cur_min_index = j
            elif val < cur_min:
                cur_min2 = cur_min
                cur_min = val
                cur_min_index = j
            elif val < cur_min2:
                cur_min2 = val
                
        print()
        prev_min = cur_min
        prev_min2 = cur_min2
        prev_min_index = cur_min_index
        
    return prev_min

if __name__ == "__main__":
    costs = [[12, 3, 4], [11, 3, 5], [23, 45, 6]]
    print(costs, "\nMin cost: ", minCost(costs))
    
    costs = [[12, 3, 4], [11, 3, 20], [23, 45, 6]]
    print(costs, "\nMin cost: ", minCost(costs))
    
    costs = [[12, 3, 56], [11, 3, 3], [23, 45, 6]]
    print(costs, "\nMin cost: ", minCost(costs))
    
        
        
        
                
        