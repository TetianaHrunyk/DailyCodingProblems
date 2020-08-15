"""Given a set of closed intervals, find the smallest set of numbers that covers 
all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers
that covers all these intervals is {3, 6}.
"""

def smallest_set(intervals: list):
    sorted_by_opening = sorted(intervals)
    sorted_by_closing = sorted(intervals, key=lambda x: x[1])
    return {sorted_by_closing[0][1], sorted_by_opening[-1][0]}

if __name__ == "__main__":
    assert smallest_set([[0, 3], [2, 6], [3, 4], [6, 9]]) == {3, 6}