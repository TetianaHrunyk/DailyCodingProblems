"""
Given a list of integers, return the largest product that can be made by
 multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since
 that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""
import numpy

def max_sum(l: list):
    if len(l) == 3:
        return numpy.prod(l)
    max_num = [max(l)]
    max_and_min = [max(l)]
    l.remove(max(l))
    for i in range(2):   
        local_max = max(l)
        local_min = min(l)
        
        if local_max == local_min:
            l.remove(local_max)   
        else:
            l.remove(local_max)
            l.remove(local_min)
        
        max_num.append(local_max)
        max_and_min.append(local_min)
        
    result1 = numpy.prod(max_num) 
    result2 = numpy.prod(max_and_min) 
    return max(result1, result2)

if __name__ == "__main__":
    assert max_sum([-10, -10, 5, 2]) == 500
    assert max_sum([-10, 5, 2]) == -100
    assert max_sum([-10, 4, 6, 5, 2]) == 120
    
        