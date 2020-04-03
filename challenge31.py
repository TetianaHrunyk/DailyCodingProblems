"""
The edit distance between two strings refers to the minimum
 number of character insertions, deletions, and substitutions 
 required to change one string to the other. For example, 
 the edit distance between “kitten” and “sitting” is three:
 substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

def strDistance(s1, s2: str) -> int:
    assert (s1 or s2)
    ls1 = len(s1)
    ls2 = len(s2)
    if ls1 == ls2:
        distance = 0
        for a, b in zip(s1, s2):
            if a != b:
                distance += 1
    else:
        great = max(ls1, ls2)
        small = min(ls1, ls2)       
        distances = []
        if great == ls1:
            great_str = s1
            small_str = s2
        else:
            great_str = s2
            small_str = s1
        for i in range(0, (great-small)):
            distance = (great - small)
            sub_str = great_str[i:(small+i)]
            for a, b in zip(sub_str, small_str):
                if a != b:
                    distance += 1
            distances.append(distance)
        distance = min(distances)
    return distance

if __name__ == "__main__":
    assert strDistance("kitten", "sitting") == 3
    assert strDistance("asd", "") == 3
    assert strDistance("thisisatest", "simple") == 8
    
        
        