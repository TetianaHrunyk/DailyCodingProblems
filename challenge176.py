"""Determine whether there exists a one-to-one character mapping from one string
 s1 to another s2.
For example, given s1 = abc and s2 = bcd, return true 
since we can map a to b, b to c, and c to d.
Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""

def exists_mapping(s1, s2):
    s1_count = sorted([s1.count(elem) for elem in s1])
    s2_count = sorted([s2.count(elem) for elem in s2])
    for s1c, s2c in zip(s1_count, s2_count):
        if s1c > s2c:
            return False
    return True

if __name__ == "__main__":
    assert exists_mapping("abc", "bcd") == True
    assert exists_mapping('foo', 'bar') == False
    assert exists_mapping('foo', 'baa') == True
    assert exists_mapping('food', 'braa') == True