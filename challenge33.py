"""
Compute the running median of a sequence of numbers. 
That is, given a stream of numbers, print out the median of the
 list so far on each new element.

Recall that the median of an even-numbered list is the average 
of the two middle numbers.
"""

def median(l: list)->int:
    length = len(l)
    if length == 1:
        return l[0]
    else:
        mid = 0
        even = length % 2
        mid = length // 2
        if even == 0:
            median = (l[mid-1] + l[mid]) / 2 
            return round(median, 1)
        else:
            return l[mid]   

def runningMedian(s: list)->list:
    m = []
    for i in range(1, len(s)):
        sub = s[:i]
        m.append(median(sub))
    return m

if __name__ == "__main__":
    runningMedian([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 1, 3.0, 5, 6.0]