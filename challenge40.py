"""
Given an array of integers where every integer occurs three times except 
for one integer, which only occurs once, find and return the non-duplicated 
integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], 
return 19.

Do this in O(N) time"""

def findUnique(l: list) -> int:
    seen_once, seen_twice = set(), set()
    for num in l:
        if num in seen_once:
            seen_once.remove(num)
            seen_twice.add(num)
        elif num in seen_twice:
            pass
        else:
            seen_once.add(num)
    return seen_once.pop()
        
if __name__ == "__main__":

    assert findUnique([6, 1, 3, 3, 3, 6, 6]) == 1
    assert findUnique([13, 19, 13, 13]) == 19