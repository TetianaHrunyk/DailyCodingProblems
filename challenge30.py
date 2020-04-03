"""
You are given an array of non-negative integers that
 represents a two-dimensional elevation map where each element
 is unit-width wall and the integer is the height. 
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) 
time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of
 water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 
2 in the second, and 3 in the fourth index (we cannot hold 5 since it would
 run off to the left), so we can trap 8 units of water.
"""

def trappedUnits(emap: list) -> int:
    piece = [emap[0]]
    units = 0
    i = 1
    while i < len(emap):
        elem = emap[i]
        if elem >= piece[0] and len(piece) == 1:
            piece = [elem]
        elif elem >= piece[0]:
            piece.append(min(piece[0], elem))
            for j in range(len(piece)):
                units += (piece[0] - piece[j])
            piece = [elem]
        else:
            piece.append(elem)
        i+=1
    if len(piece) > 2:
        height = min(piece[0], piece[-1])
        piece[0], piece[-1] = height, height
        last_units = 0
        for j in range(len(piece)):
            last_units += (piece[0] - piece[j])
            if last_units > 0:
                units += last_units
    return units

if __name__ == "__main__":
    assert trappedUnits([2, 1, 2]) == 1
    assert trappedUnits([3, 0, 1, 3, 0, 5]) == 8
    assert trappedUnits([1, 2, 3, 0, 1, 3, 0, 5]) == 8
    assert trappedUnits([3, 0, 1, 3, 0, 5, 4, 3, 1]) == 8
    assert trappedUnits([3, 0, 1, 3, 0, 5, 2, 5, 7]) == 11     
    assert trappedUnits([3, 0, 1, 3, 3, 3, 0, 5]) == 8       
            
        
            