"""
Given an array of time intervals (start, end) for classroom lectures 
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

def classRoomSchedule(classes):

    N = len(classes)
    if N==0:
        return 0
    if N==1:
        return 1
    start_times = [c[0] for c in classes]
    end_times = [c[1] for c in classes]
    start_times.sort()
    end_times.sort()
    i = 1
    j = 0
    num_classes = 1
    res = 1
    while i < N and j < N:
        if start_times[i] < end_times[j]:
            num_classes+=1
            if num_classes > res:
                res = num_classes
            i+=1
        else:
            num_classes-=1
            j+=1
    return res

if __name__ == '__main__':
    assert classRoomSchedule([(30, 75), (0, 50), (60, 150)]) == 2
    assert classRoomSchedule([(30, 75), (75, 100), (100, 150)]) == 1
    assert classRoomSchedule([(30, 75), (70, 120), (60, 150)]) == 3