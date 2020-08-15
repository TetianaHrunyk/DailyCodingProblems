"""Given an integer list where each number represents the number of hops you can make, 
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""

def reach_end(l: list):
    hops = 0
    for i in range(len(l)):
        hops += l[i]
        if hops == 0 and i < (len(l)-1):
            return False
        hops-=1
    return True

if __name__ == "__main__":
    assert reach_end([2, 0, 1, 0]) == True
    assert reach_end([1, 1, 0, 1]) == False