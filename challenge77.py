"""
Given a list of possibly overlapping intervals, return a new list of intervals
 where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return
 [(1, 3), (4, 10), (20, 25)].
"""

def mergeOverlapping(l:list):
    l.sort(key = lambda x:x[0])
    res = [l.pop(0)]
    i = 0
    while i < len(l):
        if res[-1][1] >= l[i][0]:
            if res[-1][1] < l[i][1]:
                res.append((res[-1][0], l[i][1]))
                res.pop(-2)
        else:
            res.append(l[i])
        i += 1
    return res

if __name__ == "__main__":
    assert mergeOverlapping([(1, 3), (5, 8), (4, 10), (20, 25)]) == [(1, 3), (4, 10), (20, 25)]
    assert mergeOverlapping([(1, 3), (5, 16), (4, 10), (20, 25)]) == [(1, 3), (4, 16), (20, 25)]
    assert mergeOverlapping([(1, 6), (5, 8), (4, 10), (20, 25)]) == [(1, 10), (20, 25)]