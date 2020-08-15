"""Given a number represented by a list of digits, find the next greater permutation
 of a number, in terms of lexicographic ordering. If there is not greater permutation
 possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should
 return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory
 (disregarding the input memory)?
"""
import sys

def convert_to_num(l):
    num = 0
    base = len(l) - 1
    for i in range(len(l)):
        num += l[i]*(10**(base-i))
    return num

def next_greater_permutation(l: list):
    cur_res = l
    diff = - sys.maxsize
    for i in range(len(l)):
        for j in range(i+1, len(l)):           
            perm = l.copy()
            perm[i], perm[j] = perm[j], perm[i]
            cur_diff = convert_to_num(l) - convert_to_num(perm)
            if (cur_diff > diff) and (cur_diff < 0):
                cur_res = perm
                diff = cur_diff
            perm = perm[::-1]
            cur_diff = convert_to_num(l) - convert_to_num(perm)
            if (cur_diff > diff) and (cur_diff < 0):
                cur_res = perm
                diff = cur_diff
    if abs(diff) == sys.maxsize:
        return l[::-1]
            
    return cur_res

if __name__ == "__main__":
    assert next_greater_permutation([1,2,3]) == [1,3,2]
    assert next_greater_permutation([1,3,2]) == [2,1,3]
    assert next_greater_permutation([3,2,1]) == [1,2,3]