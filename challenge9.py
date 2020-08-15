"""Given a list of integers, write a function that returns the largest sum of 
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] 
should return 10, since we pick 5 and 5.
"""

def x_in_y(query, base):
    l = len(query)
    for i in range(len(base)):
        if base[i:i+l] == query:
            return True
    return False

def largest_non_adj_elem_sum(l: list):
    max_list = []
    l_sorted = sorted(l, reverse = True)
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            perm1 = x_in_y([l_sorted[i], l_sorted[j]], l)
            perm2 = x_in_y([l_sorted[j], l_sorted[i]], l)
            if (not perm1) and (not perm2):
                max_list.append(sum([l_sorted[i], l_sorted[j]]))
    max_list = sorted(max_list, reverse = True)
    if max_list:
        return max_list[0]
    return None

if __name__ == "__main__":
    assert largest_non_adj_elem_sum([2, 4, 6, 8]) == 12
    assert largest_non_adj_elem_sum([2, 4, 8, 6]) == 10
    assert largest_non_adj_elem_sum([7, 9, 8, 5]) == 15
        